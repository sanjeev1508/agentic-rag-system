from agents.agent import AgentExecutor

class ControllerAgent:
    def __init__(self):
        self.agent = AgentExecutor()

    def run(self, query: str):
        return self.agent.run(query)