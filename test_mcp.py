#!/usr/bin/env python3
"""Simple test script to check MCP connectivity"""

import asyncio
from dotenv import load_dotenv
from agents import Agent, HostedMCPTool, Runner

# Load environment variables
load_dotenv()

def create_test_agent():
    """Create a simple agent with only MCP to test connectivity"""
    import os

    # Check if token is available
    notion_token = os.getenv("NOTION_API_TOKEN")
    if not notion_token or notion_token == "your_notion_integration_token_here":
        print("⚠️  Warning: NOTION_API_TOKEN not set or still has placeholder value")
        print("   Please set your actual Notion integration token in .env file")

    return Agent(
        name="MCP Test Agent",
        instructions="You are a test agent. Just try to list available tools from Notion MCP.",
        tools=[
            HostedMCPTool(
                tool_config={
                    "type": "mcp",
                    "server_label": "NotionMCP",
                    "server_url": "https://mcp.notion.com/mcp",
                    "require_approval": "never",
                }
            )
        ]
    )

async def test_mcp():
    """Test MCP connection"""
    print("🔍 Testing MCP connection...")

    try:
        agent = create_test_agent()
        print("✅ Agent created successfully")

        # Try to run a simple test
        result = await Runner.run(
            agent,
            input="Hello, can you tell me what tools you have available?"
        )

        print("✅ MCP connection successful!")
        print(f"Response: {result.final_output}")

    except Exception as e:
        print(f"❌ MCP connection failed:")
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")

        # Check for common issues
        if "authentication" in str(e).lower() or "token" in str(e).lower():
            print("\n💡 This looks like an authentication issue.")
            print("You likely need to set up Notion API credentials.")

        elif "connection" in str(e).lower() or "network" in str(e).lower():
            print("\n💡 This looks like a network connectivity issue.")
            print("Check your internet connection and MCP server URL.")

        else:
            print(f"\n💡 Unknown error. Full traceback:")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_mcp())