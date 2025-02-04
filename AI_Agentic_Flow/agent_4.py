from agent_1 import DocumentSummarizer
from agent_2 import QueryResponder
from agent_3 import InternetConnectedAgent

class ManagerAgent:
    def __init__(self):
        self.summarizer = DocumentSummarizer()
        self.responder = QueryResponder()
        self.internet_agent = InternetConnectedAgent()

    def decide_agent(self, user_input):
        if "summarize" in user_input.lower() or "keyword" in user_input.lower():
            return ["Agent1"]
        elif "query" in user_input.lower() and "internet" not in user_input.lower():
            return ["Agent2"]
        elif "internet" in user_input.lower() or "fetch" in user_input.lower() or "latest" in user_input.lower():
            return ["Agent3"]
        else:
            return ["Agent1", "Agent2"]

    def process(self, user_input, documents=None):
        selected_agents = self.decide_agent(user_input)
        responses = {}
        for agent in selected_agents:
            if agent == "Agent1":
                responses["Agent1"] = self.summarizer.process(documents)
            elif agent == "Agent2":
                responses["Agent2"] = self.responder.respond(user_input, documents)
            elif agent == "Agent3":
                responses["Agent3"] = self.internet_agent.fetch_information(user_input)
        return {
            "manager_agent": {
                "decision": f"Selected agents: {', '.join(selected_agents)} based on user input.",
                "selected_agents": selected_agents
            },
            "agent_responses": responses
        }