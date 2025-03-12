from mesa import Agent
import random

class SocialAgent(Agent):
    def __init__(self, unique_id, model, agent_type):
        super().__init__(unique_id, model)
        self.agent_type = agent_type  # "Human" or "Bot"
        self.influence_score = 0

    def step(self):
        if self.agent_type == "Bot":
            self.post_content()
            self.influence_others()
        elif self.agent_type == "Human":
            self.react_to_content()

    def post_content(self):
        self.influence_score += random.randint(1, 3)
        self.model.datacollector_dict["posts"].append((self.unique_id, self.influence_score))

    def influence_others(self):
        neighbors = self.model.network.neighbors(self)
        for neighbor in neighbors:
            if isinstance(neighbor, SocialAgent) and neighbor.agent_type == "Bot":
                neighbor.influence_score += 1

    def react_to_content(self):
        self.influence_score += random.randint(0, 1)
