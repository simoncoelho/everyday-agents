import os
from datetime import datetime

from agents import function_tool
from markdown_pdf import MarkdownPdf, Section


@function_tool
def create_pdf(markdown_string: str, title: str) -> str:
    """
    Converts a markdown string to a PDF file and saves it.

    Args:
        markdown_string: The markdown content to convert to PDF
        title: The title of the markdown file

    Returns:
        str: Path to the created PDF file
    """
    # Create a MarkdownPdf instance
    pdf = MarkdownPdf(toc_level=2)

    # Add the markdown content as a section
    pdf.add_section(Section(markdown_string, toc=False))

    # Generate a filename with timestamp to avoid conflicts
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{title}_{timestamp}.pdf"

    # Create output directory if it doesn't exist
    output_dir = "generated_pdfs"
    os.makedirs(output_dir, exist_ok=True)

    # Full path for the PDF file
    pdf_path = os.path.join(output_dir, filename)

    # Save the PDF
    pdf.save(pdf_path)

    return pdf_path

