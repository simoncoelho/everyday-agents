import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from agents import function_tool


@function_tool
def send_pdf_to_kindle(pdf_path: str, title: str = "Generated Lesson") -> str:
    """
    Sends a PDF file to Kindle via email.

    Args:
        pdf_path: Path to the PDF file to send
        title: Subject line for the email (optional)

    Returns:
        str: Success or error message
    """
    # Kindle and sender email addresses
    kindle_email = os.getenv("KINDLE_EMAIL_ADDRESS")
    sender_email = os.getenv("AGENT_EMAIL_ADDRESS")

    # Get email password from environment variable
    email_password = os.getenv("GMAIL_APP_PASSWORD")
    if not email_password:
        return "Error: GMAIL_APP_PASSWORD environment variable not set"

    # Check if PDF file exists
    if not os.path.exists(pdf_path):
        return f"Error: PDF file not found at {pdf_path}"

    try:
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = kindle_email
        msg['Subject'] = title

        # Add email body
        body = f"Automated delivery of: {title}"
        msg.attach(MIMEText(body, 'plain'))

        # Attach PDF file
        with open(pdf_path, 'rb') as pdf_file:
            pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
            pdf_attachment.add_header(
                'Content-Disposition',
                f'attachment; filename="{os.path.basename(pdf_path)}"'
            )
            msg.attach(pdf_attachment)

        # Connect to Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Enable encryption
        server.login(sender_email, email_password)

        # Send the email
        server.send_message(msg)
        server.quit()

        return f"Successfully sent {os.path.basename(pdf_path)} to Kindle"

    except Exception as e:
        return f"Error sending email: {str(e)}"
