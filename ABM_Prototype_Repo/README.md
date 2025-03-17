# Coordinated AI Bot Influence - ABM Prototype

## Overview
This project simulates the influence of AI-driven social bots in online social networks using an Agent-Based Modeling (ABM) approach with the Mesa framework. The goal is to explore how bots amplify engagement, manipulate discussions, and influence human users through algorithmic prioritization.

## The core elements of the model:
- Two agent types: **Human agents** (blue) and **Bot agents** (red/gray)
- A **network structure**, where nodes represent agents and edges represent social media connections.
- **Bot agents** aim to increase influence by interacting with human agents and amplifying content visibility.
- **Human agents** respond organically and are influenced by bot interactions.
- After the 10th step of the simulation, a user-defined number of bots are **"removed"**, and the color of their nodes changes from **red to gray**. These bots no longer participate in interactions.
- A **RandomActivation scheduler** is used to model unpredictable real-world engagement patterns.
- The model supports **interactive sliders** to adjust:
  - Number of humans
  - Number of bots
  - Number of removed bots after step 10
- **Data collection and visualization** features are included:
  - Engagement data (bot vs human)
  - Average influence per agent type
  - Real-time network graph and influence charts

The prototype successfully demonstrates foundational interaction dynamics between bots and humans in a network environment.

---

## How to Run

1. **Install dependencies**  
   Ensure you have Python 3.7+ installed, then install required packages:
   ```
   pip install -r requirements.txt
   ```
2. **Run Simulation**  
   Navigate to the source directory and execute the script:
   ```
   python src/simulation.py
   ```
   After running, the simulation will generate:
   - **A real-time visualization** of the social network.
   - **Dynamic charts** showing engagement (bot vs human) and average per agent.

3. **Interface Usage**
   - Control the number of human agents, bot agents, and removed bots in the sliders.
   - Observe the **network graph** and **engagement/infulence charts**
   - Removed bots will be appear in **grey color** after step 10.


## Limitations & Planned Improvements

### **Limitations**

- Limited intervention modeling (only basic bot removal).
- No scenario comparison (bots vs. partial/no bots).
- Simple influence metrics (no duration or visibility tracking).
- Lack of visualizations for comparing engagement cases.
- Basic bot behavior (no clustering or adaptive strategies).

### **Planned Improvements**

- Test intervention models (e.g., filter bot engagement).
- Add scenario-based visualizations (bots / partial / no bots).
- Expand influence metrics (duration & visibility).
- Compare bot-boosted vs. human-generated content impact.
- Improve bot strategies (e.g., clustering, targeting).
  
## Directory Structure
<pre>
ABM_Prototype_Repo/
├── docs/                # Documentation
│   └── interim_report.md
│   └── images          
├── notebooks/           # Jupyter Notebooks (if any analysis needed)
├── src/                 # Source code
│   └── simulation.py    # Main simulation script
├── README.md            # Project documentation (this file)
├── requirements.txt     # Python dependencies
</pre>
