import asyncio
from dotenv import load_dotenv
from agents.mcp import MCPServerStreamableHttp, MCPServerStreamableHttpParams, MCPServer
import os

from agents import Runner
from workflows.tailored_learning.agent.get_learning_agent import get_learning_agent
from workflows.tailored_learning.agent.mcp_servers.mcp_registry import initialize_all, dispose_all, mcp_servers

class TailoredLearningWorkflow:
    def __init__(self,
                number_of_pages_low: int = 15,
                number_of_pages_high: int = 25,
                number_of_documents: int = 1):
        self.page_counts = [number_of_pages_low, number_of_pages_high]
        self.document_count = number_of_documents
        self.agent = get_learning_agent(mcp_servers, self.page_counts)

    async def run(self):
        await initialize_all()
        print("Beginning run...")
        result = await Runner.run(self.agent, input="Create a personalized learning lesson based on my profile and interests")
        print("Agent completed pdf.")
        await dispose_all()

    async def initialize(self):
        await self.mcp_servers.initalize_all()

if __name__ == "__main__":
    load_dotenv()
    workflow = TailoredLearningWorkflow()
    asyncio.run(workflow.run())
    dispose_all()
