from agents import Agent, gen_trace_id, trace
from agents.mcp import MCPServerStreamableHttp, MCPServerStreamableHttpParams, MCPServer
from typing import List
from .tools import create_pdf, send_pdf_to_kindle
from .prompts.system_prompt import system_prompt
import os

def get_learning_agent(page_count: List[int] = [3, 7]) -> Agent:
    mcp = MCPServerStreamableHttp(
                MCPServerStreamableHttpParams(
                    url="https://mcp.notion.com/mcp",
                    headers={"Authorization": f"Bearer {os.environ["NOTION_API_KEY"]}"}
                )
             )
    
    mcp.connect()

    print(mcp.list_tools)

    return Agent(
        name = "Tailored Learning Agent",
        instructions=system_prompt(page_count[0], page_count[1]),
        mcp_servers=[
            mcp,
        ],
        tools = [
            create_pdf,
            send_pdf_to_kindle
        ],
    )