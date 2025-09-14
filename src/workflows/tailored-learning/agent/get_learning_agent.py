from agents import Agent, HostedMCPTool
from typing import List
from .tools import create_pdf, send_pdf_to_kindle
from .prompts.system_prompt import system_prompt

def get_learning_agent(page_count: List[int] = [3, 7]) -> Agent:
    return Agent(
        name = "Tailored Learning Agent",
        instructions=system_prompt(page_count[0], page_count[1]),
        tools = [
            HostedMCPTool(
                tool_config={
                    "type": "mcp",
                    "server_label": "NotionMCP",
                    "server_url": "https://mcp.notion.com/mcp",
                    "require_approval": "never",
                }            ),
            create_pdf,
            send_pdf_to_kindle
        ]
    )