from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import NetworkGrid
from mesa.datacollection import DataCollector
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import NetworkModule, ChartModule
from mesa.visualization.UserParam import UserSettableParameter
import networkx as nx
import random

class SocialAgent(Agent):
    def __init__(self, unique_id, model, agent_type):
        super().__init__(unique_id, model)
        self.agent_type = agent_type
        self.influence = 0
        self.removed = False  # Indicates whether the bot is deactivated/removed

    def step(self):
        # Deactivated bots do nothing
        if self.agent_type == "bot" and self.removed:
            return

        neighbors = self.model.grid.get_neighbors(self.unique_id, include_center=False)

        if neighbors:
            target = self.random.choice(neighbors)
            self.model.grid.move_agent(self, target)

        if self.agent_type == "bot":
            self.influence += 1
            if neighbors:
                target = self.random.choice(neighbors)
                target_agent = self.model.grid.get_cell_list_contents([target])
                if target_agent and target_agent[0].agent_type == "human":
                    target_agent[0].influence += 1

        elif self.agent_type == "human":
            if neighbors:
                target = self.random.choice(neighbors)
                target_agent = self.model.grid.get_cell_list_contents([target])
                if target_agent and target_agent[0].agent_type == "bot":
                    self.influence += 1

class SocialModel(Model):
    def __init__(self, num_humans=10, num_bots=5, num_removed_bots=2):
        self.num_humans = num_humans
        self.num_bots = num_bots
        self.num_removed_bots = num_removed_bots
        self.G = nx.erdos_renyi_graph(n=num_humans + num_bots, p=0.3)
        self.grid = NetworkGrid(self.G)
        self.schedule = RandomActivation(self)
        self.current_step = 0
        self.removed_bots = set()

        for i, node in enumerate(self.G.nodes()):
            agent_type = "bot" if i < num_bots else "human"
            agent = SocialAgent(i, self, agent_type)
            self.schedule.add(agent)
            self.grid.place_agent(agent, node)

        self.datacollector = DataCollector({
            "Bot Engagement": lambda m: sum(a.influence for a in m.schedule.agents if a.agent_type == "bot"),
            "Human Engagement": lambda m: sum(a.influence for a in m.schedule.agents if a.agent_type == "human"),
            "Average Bot Influence": lambda m: (
                sum(a.influence for a in m.schedule.agents if a.agent_type == "bot") / max(1, len([a for a in m.schedule.agents if a.agent_type == "bot"]))
            ),
            "Average Human Influence": lambda m: (
                sum(a.influence for a in m.schedule.agents if a.agent_type == "human") / max(1, len([a for a in m.schedule.agents if a.agent_type == "human"]))
            )
        })

    def step(self):
        self.current_step += 1

        # Remove bots after step 10
        if self.current_step == 11:
            all_bot_agents = [a for a in self.schedule.agents if a.agent_type == "bot" and not a.removed]
            removed_bots = random.sample(all_bot_agents, min(self.num_removed_bots, len(all_bot_agents)))
            for agent in removed_bots:
                agent.removed = True
                self.removed_bots.add(agent.unique_id)

        self.schedule.step()
        self.datacollector.collect(self)

# Network portrayal function (color representation)
def network_portrayal(G):
    portrayal = {"nodes": [], "edges": []}
    for node in G.nodes():
        agent = next((a for a in model_instance.schedule.agents if a.unique_id == node), None)
        if agent:
            if agent.agent_type == "bot":
                color = "gray" if agent.removed else "red"
            else:
                color = "blue"
        else:
            color = "black"
        portrayal["nodes"].append({
            "id": node,
            "size": 10,
            "color": color
        })

    for edge in G.edges():
        portrayal["edges"].append({"source": edge[0], "target": edge[1]})
    return portrayal

# Model parameters (UI sliders)
model_params = {
    "num_humans": UserSettableParameter("slider", "Number of Humans", 10, 1, 50, 1),
    "num_bots": UserSettableParameter("slider", "Number of Bots", 5, 1, 30, 1),
    "num_removed_bots": UserSettableParameter("slider", "Number of Removed Bots After Step 10", 2, 0, 30, 1),
}

# Global variable to share model instance with the portrayal function
model_instance = None

def model_factory(**kwargs):
    global model_instance
    model_instance = SocialModel(**kwargs)
    return model_instance

# Visualization modules
network = NetworkModule(network_portrayal, 500, 500)
engagement_chart = ChartModule([
    {"Label": "Bot Engagement", "Color": "Red"},
    {"Label": "Human Engagement", "Color": "Blue"},
])

avg_influence_chart = ChartModule([
    {"Label": "Average Bot Influence", "Color": "Green"},
    {"Label": "Average Human Influence", "Color": "Purple"},
])

# Launch the server
server = ModularServer(
    model_factory,
    [network, engagement_chart, avg_influence_chart],
    "Social Media Influence Simulation",
    model_params
)
server.port = 8521
server.launch()
