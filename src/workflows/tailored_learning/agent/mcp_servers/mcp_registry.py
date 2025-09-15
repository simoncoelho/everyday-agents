from agents.mcp import MCPServer, MCPServerStdio, MCPServerStdioParams
import os
from dotenv import load_dotenv

load_dotenv()

notion_mcp = MCPServerStdio(
    MCPServerStdioParams(
        command="npx",
        args=["-y", "@notionhq/notion-mcp-server"],
        env={"NOTION_TOKEN": os.environ["NOTION_API_TOKEN"]},
    )
)

mcp_servers = [
    notion_mcp
]


async def initialize_all():
    for _ in mcp_servers:
        await _.connect()

async def dispose_all():
    for _ in mcp_servers:
        await _.cleanup()
