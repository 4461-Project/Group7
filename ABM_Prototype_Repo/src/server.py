from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import NetworkModule
from .model import BotInfluenceModel

def network_portrayal(G):
    def node_portrayal(agent):
        portrayal = {
            "color": "red" if agent.agent_type == "Bot" else "blue",
            "size": 8,
            "tooltip": f"{agent.agent_type} ID:{agent.unique_id}, Score:{agent.influence_score}"
        }
        return portrayal
    return dict(nodes=[node_portrayal(agent) for agent in G.nodes],
                edges=[{"source": e[0], "target": e[1]} for e in G.edges])

network_module = NetworkModule(network_portrayal, 500, 500)
server = ModularServer(
    BotInfluenceModel,
    [network_module],
    "Coordinated Bot Influence",
    {"num_agents": 20, "bot_ratio": 0.3}
)
