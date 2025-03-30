# Coordinated Bot Influence Simulation

# Overview :

This simulation models **coordinated bot behavior** in digital media ecosystems, showing on how bots manipulate content visibility, public opinion, and engagement metrics. Inspired by **Boid Theory**, bots in the simulation follow simple coordination rules (alignment, cohesion, separation) to amplify specific narratives, dominate attention, and suppress alternative viewpoints.

The phenomenon being modeled is **engagement hijacking**, where bots collaborate to inflate content popularity and create the illusion of consensus. This behavior is especially relevant in platforms like X (formerly Twitter), Instagram, and Facebook, where recommendation algorithms amplify high-engagement content. 

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

# Key Findings: 

 Humans Amplify Bot Activity
Once bots boost a post, humans engage with it—creating self-reinforcing loops.


Human interaction makes bot-amplified content trend even more.
Bot Clustering is Strategic Amplification
Bots cluster around human nodes to maximize influence.


These coordinated behaviors mirror Boid Theory dynamics: alignment, cohesion, separation.
Echo Chambers Form
Repeated exposure to similar bot-driven content reduces information diversity.


Users see less alternative or opposing viewpoints.
Influence Remains Even After Bot Removal
Even after bots are deactivated, humans continue engaging with the content they boosted.


This shows residual manipulation, even with fewer active bots.


Engagement Cycles Repeat
Bot-driven spikes in engagement can return if bots reactivate or evolve.


This reflects cyclical amplification patterns seen in real-world misinformation waves.



