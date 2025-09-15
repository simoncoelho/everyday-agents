import asyncio
import os
import shutil
import sys

from agents.mcp import MCPServerStdio, MCPServerStdioParams
from dotenv import load_dotenv

load_dotenv()


async def main():
    print("Creating MCP server...")
    mcp = MCPServerStdio(
        MCPServerStdioParams(
            command="npx",
            args=["-y", "@notionhq/notion-mcp-server"],
            env={"NOTION_TOKEN": os.environ["NOTION_API_TOKEN"]},
        )
    )

    try:
        print("Connecting to MCP server...")
        result = await mcp.connect()
        print(result)
        print("MCP server connected successfully!")

        print(mcp.list_tools())

    except Exception as e:
        print(f"Error connecting to MCP server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
