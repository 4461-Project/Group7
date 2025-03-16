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
   Navigate to the source directory and execute the script:
   ```
   cd src
   python run.py
   ```
   After running, the simulation will generate:
   - **A visualization** of the social network.
   - **`interaction_log.csv`**, which logs agent interactions.

## Code Overview

The project follows an **Agent-Based Modeling (ABM) structure**, implemented using `Mesa`.

### **Key Components:**
- `UserAgent`: Represents human users and bots, each with unique behavior.
- `SocialNetworkModel`: The core simulation model managing agent interactions and scheduling.
- `RandomActivation`: Ensures agents take actions in a randomized sequence to simulate realistic interaction.
- `interaction_log.csv`: Captures engagement data at each simulation step.

## Directory Structure
<pre>
project_root/
│── src/               # Source code
│   ├── run.py        # Main simulation script
│── docs/              # Documentation
│── notebooks/         # Jupyter Notebooks (if any analysis needed)
│── requirements.txt   # Python dependencies
│── README.md          # Project documentation (this file)
│── interaction_log.csv # Data logs of interactions
</pre>

## Simulation Output

### **Example: `interaction_log.csv`**
```
timestep,user_id,interaction_type,target_id
1,Human_1,like,Bot_3
2,Bot_2,retweet,Human_5
3,Human_4,share,Bot_1
```
This dataset helps analyze bot influence over time.

## Limitations & Planned Improvements

### **Current Features**

- ✅ Basic social network graph with human users and bots.
- ✅ Simulated content interactions (likes, shares, retweets).
- ✅ Algorithm-based prioritization (exponential bot influence growth).
- ✅ Data logging of interactions.
- ✅ Visualization of agent interactions and engagement trends.

### **Planned Improvements**

- 🔹 Improve bot behavior (targeting influential users more effectively).
- 🔹 Advanced visualization (interactive network & detailed metrics).
- 🔹 Enhanced data analysis (user engagement patterns, sentiment impact).
- 🔹 Implement adaptive bot strategies to simulate real-world behavior more accurately.
