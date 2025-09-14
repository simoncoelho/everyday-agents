import asyncio
from dotenv import load_dotenv

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
        for _ in range(self.document_count):
            print("Beginning run...")
            result = await Runner.run(self.agent, input="Create a personalized learning lesson based on my profile and interests")
            print("Agent completed first pdf.")
            print(result.final_output)
        print("Completed all runs.")



if __name__ == "__main__":
    load_dotenv()
    workflow = TailoredLearningWorkflow()
    asyncio.run(workflow.run())
