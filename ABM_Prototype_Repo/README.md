# Coordinated AI Bot Influence - ABM Prototype

## Overview
This project simulates the influence of AI-driven social bots in online social networks using an Agent-Based Modeling (ABM) approach with the Mesa framework. The goal is to explore how bots amplify engagement, manipulate discussions, and influence human users through algorithmic prioritization.

## Key Features
- ✅ **Social Network Graph**: Humans (blue) and Bots (red) interact in a dynamic network.
- ✅ **Content Interaction Simulation**: Simulates likes, shares, and retweets.
- ✅ **Algorithmic Influence**: Shows how bots boost engagement through platform algorithms.
- ✅ **Data Logging**: Records interactions in `interaction_log.csv`.
- ✅ **Agent-Based Modeling**: Uses **Mesa** for simulation and interaction scheduling.
- ✅ **Visualization**: Generates network graphs, interaction charts, and engagement trend analysis.

## How to Run

1. **Install dependencies**  
   Ensure you have Python 3.8+ installed, then install required packages:
   ```
   pip install -r requirements.txt
   ```
2. **Run Simulation**  
    ```
    cd src
    python run.py
    ```

# Directory Structure
<pre>
project_root/
│── src/               # Source code
│── docs/              # Documentation
│── notebooks/         # Jupyter Notebooks (if any analysis needed)
│── requirements.txt   # Python dependencies
│── README.md          # Project documentation (this file)
│── interaction_log.csv # Data logs of interactions
</pre>

# Limitations & Planned Improvements

## Current Features

- ✅ Basic social network graph with human users and bots.
- ✅ Simulated content interactions (likes, shares, retweets).
- ✅ Algorithm-based prioritization (exponential bot influence growth).
- ✅ Data logging of interactions.
- ✅ Visualization of agent interactions and engagement trends.

## Planned Improvements

- 🔹 Improve bot behavior (targeting influential users more effectively).
- 🔹 Advanced visualization (interactive network & detailed metrics).
- 🔹 Enhanced data analysis (user engagement patterns, sentiment impact).
- 🔹 Implement adaptive bot strategies to simulate real-world behavior more accurately.
