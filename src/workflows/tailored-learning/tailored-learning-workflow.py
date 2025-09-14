from agents import Agent, HostedMCPTool, Runner
from typing import List
from .agent import tailored_lesson_agent
import asyncio


class TailoredLearningWorkflow:
    def __init__(self, 
                number_of_pages_low: int = 3,
                number_of_pages_high: int = 7,
                number_of_documents: int = 4):
        self.page_counts = [number_of_pages_low, number_of_pages_high]
        self.document_count = number_of_documents
        self.agent = tailored_lesson_agent.get_learning_agent(self.page_counts)

    async def run(self):
        for _ in range(self.document_count):
            print("Beginning run...")
            result = await Runner.run(self.agent)
            print("Agent completed first pdf.")
            print(result.final_output)
        print("Completed all runs.")



if __name__ == "__main__":
    workflow = TailoredLearningWorkflow
    asyncio.run(workflow.run())