from agents import Agent, HostedMCPTool, Runner
from typing import List
from .agent import tailored_lesson_agent


class TailoredLearningWorkflow:
    def __init__(self, 
                number_of_pages_low: int = 3,
                number_of_pages_high: int = 7,
                number_of_documents: int = 4):
        self.page_counts = [number_of_pages_low, number_of_pages_high],
        self.document_count = number_of_documents,
        self.agent = tailored_lesson_agent.get_learning_agent(page_counts)

    def run():
        range(self.document_count)

        Runner.run(self.agent, )