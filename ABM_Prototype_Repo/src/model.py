from mesa import Model
from mesa.time import StagedActivation
from mesa.space import NetworkGrid
import networkx as nx
from mesa.datacollection import DataCollector
from .agent import SocialAgent

class BotInfluenceModel(Model):
    def __init__(self, num_agents=20, bot_ratio=0.3):
        self.num_agents = num_agents
        self.num_bots = int(num_agents * bot_ratio)
        self.schedule = StagedActivation(self, stage_list=["step"])
        self.network = nx.erdos_renyi_graph(n=num_agents, p=0.2)
        self.grid = NetworkGrid(self.network)
        self.datacollector_dict = {"posts": []}

        for i, node in enumerate(self.network.nodes()):
            if i < self.num_bots:
                agent_type = "Bot"
            else:
                agent_type = "Human"
            agent = SocialAgent(i, self, agent_type)
            self.schedule.add(agent)
            self.grid.place_agent(agent, node)

    def step(self):
        self.schedule.step()
