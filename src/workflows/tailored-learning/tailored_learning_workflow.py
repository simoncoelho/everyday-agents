import asyncio
from dotenv import load_dotenv
from agents.mcp import MCPServerStreamableHttp, MCPServerStreamableHttpParams, MCPServer
import os

from agents import Runner

try:
    # Try relative import (works when running as module or imported)
    from .agent.get_learning_agent import get_learning_agent
except ImportError:
    # Fall back to absolute import (works when running as script)
    from agent.get_learning_agent import get_learning_agent


class TailoredLearningWorkflow:
    def __init__(self,
                number_of_pages_low: int = 3,
                number_of_pages_high: int = 7,
                number_of_documents: int = 4):
        self.page_counts = [number_of_pages_low, number_of_pages_high]
        self.document_count = number_of_documents
        self.agent = get_learning_agent(self.page_counts)

    async def run(self):
        await self.initialize()

        for _ in range(self.document_count):
            print("Beginning run...")
            result = await Runner.run(self.agent, input="Create a personalized learning lesson based on my profile and interests")
            print("Agent completed first pdf.")
            print(result.final_output)
        print("Completed all runs.")


    async def initialize(self):
        self.mcp = MCPServerStreamableHttp(
                MCPServerStreamableHttpParams(
                    url="https://mcp.notion.com/mcp",
                    headers={"Authorization": f"Bearer {os.environ["NOTION_API_KEY"]}"}
                )
             )
        self.mcp.create_streams()
        result = await self.mcp.connect()
        print("MCP servers intialized.")
        print(result)

if __name__ == "__main__":
    load_dotenv()
    workflow = TailoredLearningWorkflow()
    asyncio.run(workflow.run())
