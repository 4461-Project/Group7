from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import NetworkGrid
from mesa.datacollection import DataCollector
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import NetworkModule, ChartModule
from mesa.visualization.UserParam import UserSettableParameter
import networkx as nx
import random
import math

# --- Agent Definition ---
class SocialAgent(Agent):
    def __init__(self, unique_id, model, agent_type):
        super().__init__(unique_id, model)
        self.agent_type = agent_type
        self.influence = 0
        self.removed = False
        self.promoted_topic = random.choice(["A", "B", "C"]) if agent_type == "bot" else None

    def step(self):
        if self.agent_type == "bot" and self.removed:
            return

        neighbors = list(self.model.G.neighbors(self.unique_id))
        if not neighbors:
            return

        # --- Boid-like Movement ---
        my_pos = (self.model.G.nodes[self.unique_id]["x"], self.model.G.nodes[self.unique_id]["y"])
        avg_x, avg_y = 0, 0
        count = 0

        for n in neighbors:
            n_pos = (self.model.G.nodes[n]["x"], self.model.G.nodes[n]["y"])
            avg_x += n_pos[0]
            avg_y += n_pos[1]
            count += 1

        if count > 0:
            avg_x /= count
            avg_y /= count
            dx = (avg_x - my_pos[0]) * 0.05 + random.uniform(-2, 2)
            dy = (avg_y - my_pos[1]) * 0.05 + random.uniform(-2, 2)
            new_x = max(0, min(500, my_pos[0] + dx))
            new_y = max(0, min(500, my_pos[1] + dy))
            self.model.G.nodes[self.unique_id]["x"] = new_x
            self.model.G.nodes[self.unique_id]["y"] = new_y

        # --- Influence Logic ---
        if self.agent_type == "bot":
            self.influence += 1
            target = self.random.choice(neighbors)
            target_agent = self.model.grid.get_cell_list_contents([target])
            if target_agent and target_agent[0].agent_type == "human":
                target_agent[0].influence += 1
                self.model.topic_counts[self.promoted_topic] += 1

        elif self.agent_type == "human":
            target = self.random.choice(neighbors)
            target_agent = self.model.grid.get_cell_list_contents([target])
            if target_agent and target_agent[0].agent_type == "bot":
                self.influence += 1

# --- Model Definition ---
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
        self.topic_counts = {"A": 0, "B": 0, "C": 0}

        for node in self.G.nodes:
            self.G.nodes[node]["x"] = random.randint(50, 450)
            self.G.nodes[node]["y"] = random.randint(50, 450)

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
            ),
            "A Topic Exposure": lambda m: m.topic_counts["A"],
            "B Topic Exposure": lambda m: m.topic_counts["B"],
            "C Topic Exposure": lambda m: m.topic_counts["C"],
        })

    def step(self):
        self.current_step += 1
        self.topic_counts = {"A": 0, "B": 0, "C": 0}

        if self.current_step == 11:
            all_bot_agents = [a for a in self.schedule.agents if a.agent_type == "bot" and not a.removed]
            removed_bots = random.sample(all_bot_agents, min(self.num_removed_bots, len(all_bot_agents)))
            for agent in removed_bots:
                agent.removed = True
                self.removed_bots.add(agent.unique_id)

        self.schedule.step()
        self.datacollector.collect(self)

# --- Network Portrayal (Dynamic Positions) ---
def network_portrayal(G):
    portrayal = {"nodes": [], "edges": []}
    for node in G.nodes():
        agent = next((a for a in model_instance.schedule.agents if a.unique_id == node), None)
        color = "black"
        if agent:
            if agent.agent_type == "bot":
                color = "gray" if agent.removed else "red"
            else:
                color = "blue"

        x = G.nodes[node].get("x", random.randint(0, 500))
        y = G.nodes[node].get("y", random.randint(0, 500))
        portrayal["nodes"].append({
            "id": node,
            "size": 10,
            "color": color,
            "x": x,
            "y": y
        })

    for edge in G.edges():
        portrayal["edges"].append({"source": edge[0], "target": edge[1]})
    return portrayal

# --- Model Parameters ---
model_params = {
    "num_humans": UserSettableParameter("slider", "Number of Humans", 10, 1, 50, 1),
    "num_bots": UserSettableParameter("slider", "Number of Bots", 5, 1, 30, 1),
    "num_removed_bots": UserSettableParameter("slider", "Number of Removed Bots After Step 10", 2, 0, 30, 1),
}

# --- Global Model Reference for Visualization ---
model_instance = None
def model_factory(**kwargs):
    global model_instance
    model_instance = SocialModel(**kwargs)
    return model_instance

# --- Visualization Modules ---
network = NetworkModule(network_portrayal, 500, 500)
engagement_chart = ChartModule([
    {"Label": "Bot Engagement", "Color": "Red"},
    {"Label": "Human Engagement", "Color": "Blue"},
])
avg_influence_chart = ChartModule([
    {"Label": "Average Bot Influence", "Color": "Green"},
    {"Label": "Average Human Influence", "Color": "Purple"},
])
topic_chart = ChartModule([
    {"Label": "A Topic Exposure", "Color": "Red"},
    {"Label": "B Topic Exposure", "Color": "Blue"},
    {"Label": "C Topic Exposure", "Color": "Green"}
])

# --- Launch Server ---
server = ModularServer(
    model_factory,
    [network, engagement_chart, avg_influence_chart, topic_chart],
    "Dynamic Bot-Human Network (Boid-like Simulation)",
    model_params
)
server.port = 8521
server.launch()
