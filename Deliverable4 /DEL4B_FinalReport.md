# Deliverable 4: Coordinated Bot Influence in Media Ecosystems

## §1. Phenomenon Overview

### 1.1 Context & Significance  
Our project simulates how groups of coordinated bots can manipulate content visibility, shape public opinion, and change the flow of information within digital media ecosystems. Inspired by **Boid Flocking Theory**, we apply principles like alignment, cohesion, and separation to simulate bot coordination strategies. Bots in our model amplify narratives and suppress opposing viewpoints, creating an illusion of organic popularity. This phenomenon challenges the fairness and authenticity of online conversations by distorting algorithmic visibility and public perception.

### 1.2 Problem Statement  
The simulation examines how bots influence human engagement and content visibility. Bots increase likes or comments on targeted content, skewing what humans see and engage with. We explore how varying the ratio of bots to humans affects overall influence.

### 1.3 Why Agent-Based Modeling (ABM)  
- **Individual Decision-Making**: Models both humans and bots as independent agents.  
- **Emergent Behavior**: Captures complex group outcomes from simple rules.  
- **Scenario Flexibility**: Enables testing of bot-to-human ratios in a controlled environment.

### 1.4 Visual Illustration of the Phenomenon
![Figure A](./images/1.png)
- **Figure A** – Timestep 0: Bots (Orange) and humans (Green) actively interact.
![Figure B](./images/2.png) 
- **Figure B** – Timestep 14: Deactivated bots shown in gray after step 10.
![Figure C](./images/3.png) 
- **Figure C** – Graph: Demonstrates a feedback loop where bots initiate content engagement, and humans amplify it further, resulting in rising engagement on both sides.
![Figure B](./images/4.png)  
- **Figure D** – Graph: Initial bot influence is higher; human influence rises after bots are removed.
![Figure B](./images/5.png)  
- **Figure E** –
![Figure B](./images/6.png)  
- **Figure F** –

---

## §2. Simulation Design & Implementation

### 2.1 System Overview  
Simulated media ecosystem with two agent types:
- **Bots**: Amplify specific content.
- **Humans**: Passively engage, biased toward visible content.  
Network consists of:
- **Nodes**: Agents (bots/humans).  
- **Edges**: Potential interactions, with weighted influence strength.

### 2.2 Simulation Environment  
- **Frameworks**: Mesa (agent-based modeling), NetworkX (graph structure).  
- **Features**:
  - Erdős-Rényi graph model  
  - Dynamic edge weights (0.1–1.0)  
  - Visualized with agent color and edge thickness  
- **Parameters**:
  - Total agent count  
  - Bot/human ratio  
  - Bot removal after step 10  
  - Influence depends on random draw < edge weight

### 2.3 Agent Design

**Bot Agents** (inspired by Boid Theory):
- **Alignment**: Bots synchronize strategies.
- **Cohesion**: Cluster near humans for visibility.
- **Separation**: Avoid oversaturation by spreading out strategically.

**Human Agents**:
- Passively engage with amplified content.
- More likely to interact with boosted items.

**Simplifications**:
- One interaction per step  
- No content veracity/fact-checking

### 2.4 Interaction Dynamics  
- **RandomActivation** scheduler: Random agent order each step  
- **Bot-to-Human**: Influence via edge weight probability  
- **Bot-to-Bot**: Create reinforcement loops (amplification patterns)  
- **Post-step-10**: Bots removed

### 2.5 Data Collection & Visualization  
- **Metrics**:
  - Total Engagement (bots vs humans)  
  - Average Influence per agent  
- **Visualization Tools**:
  - Network graph (agent type & edge weight)  
  - Engagement chart (bot vs human over time)  
  - Influence chart  
- **Challenges**:
  - Accurate influence scaling  
  - Visualization clarity with large agent counts

---

## §3. Observations & Results

### 3.1 Key Findings  
- **Amplification Disparity**: Bots have higher influence per agent.  
- **Initial Surge**: Bots dominate in early steps.  
- **Removal Effect**: Human engagement increases after bot deactivation.  
- **Bot Clustering**: Enhances effectiveness by embedding near humans.

### 3.2 Data Highlights  
- **Chart 1**: Bots dominate engagement early; humans catch up post-removal.  
- **Chart 2**: Higher bot influence; gradual rise in human influence.  
- **Network Graphs**:
  - Step 5: Bots dispersed  
  - Step 10: Bots begin clustering  
  - Step 15: Shift post-removal

### 3.3 Unexpected Behaviors  
- **Echo Chambers**: Repeated targeting of the same users  
- **Influence Imbalance**: Some bots dominate due to edge weight

### 3.4 Interpretations  
- Algorithms can be manipulated by fake engagement.  
- Even small bot groups can shift content visibility.  
- Bot influence lingers post-removal, delaying normalization.

---

## §4. Ethical & Societal Reflections

### 4.1 Ethical Considerations  
- Bots manipulate engagement metrics.  
- Simulations could be misused for malicious strategy testing.  
- While no real data is used, simulated influence demonstrates potential public manipulation.

### 4.2 Societal Implications  
- **Micro**: Users unknowingly engage with bot-promoted content.  
- **Meso**: Platforms amplify manipulated content, warping discourse.  
- **Macro**: Elections, protests, and public health debates can be distorted.  
- **Repurposing Risk**:  
  - Simulations can train detection or exploitation.  
  - Emphasizes need for algorithm transparency.

---

## §5. Lessons Learned & Future Directions

### 5.1 Design Reflections  
During the design and development of our simulation, we encountered a few challenges. One of the first was considering whether we should map edge weights to represent influence strength. Since we used a network model where agents interact via edges, we initially wanted these edges to carry dynamic weight values — such as levels of trust or exposure. However, implementing and updating weighted edges in real-time without cluttering the simulation is  complex and unnecessary since we wanted to show the clustering/flocking behavior of the bots . So, we opted to not display any edges to better display the movement of bots in a coordinated way. 
Another challenge we faced was , simulating strategic clustering behavior among bots. We wanted bots to show coordination by naturally flocking toward human clusters — not just randomly engaging. To achieve this, we used Boid-inspired movement patterns (alignment, cohesion, and separation), which required tuning to balance realism and performance.
We realized that as agents moved in real-time, the network display would become overwhelming. To address this, we focused on keeping the graph simple, using color-coded nodes to help users focus on core dynamics like clustering and influence spread.
Despite these challenges, we were  able to clearly visualize feedback loops through engagement and topic exposure charts, helping us connect simulated behavior to real-world social media platforms.


### 5.2 Limitations  
This simulation cannot perfectly replicate the real world, so it includes some simplified elements. One of the main simplifications is that both humans and bots behave in a very basic way. They follow simple rules, have limited memory, cannot deeply judge content, and do not consider emotions or social context.
In addition, all content was treated the same. Although bots spread various types of content, the simulation did not distinguish whether the content was true, false, or provocative. Because of this, we couldn’t explore how different types of information affect people in different ways.
Lastly, the way content spreads was also simplified. We only used direct sharing between people, and did not include other real-world methods like recommendation algorithms, trending boosts, or advertisements that are common in social media platforms.


### 5.3 Future Improvements  
To introduce a more realistic simulation, later versions of this simulation could include a variety of refinements. For example, we could include different types of content — e.g., truthful, misleading, inflammatory posts — and observe how they spread in different ways.
And finally, we'd like to incorporate resistance behaviors for human actors -- offering a way to challenge bot-influenced content based on individual difference, trust levels, or exposure fatigue.
We also see value in copying bot diversity. Not every bot in the real world behaves in the same way; there are spammers and infiltrators that behave exactly like humans. Including these as types would improve the simulation and provide information on which methods are most effective or dangerous.
Lastly, incorporating anonymized real-world data could make the simulation more representative of actual world dynamics. This would allow us to compare model behavior to actual world trends and more accurately see how interventions (e.g., bot removal or content warnings) impact network influence.


### 5.4 Future Applications  
The results from our simulation can be helpful in many real-world areas. First, for policy and platform management, the model can help find patterns in bot behavior, decide when to take action, and see what happens when bots are removed. For example, since people don’t stop engaging right after bots are removed, it shows that early detection and action are more important than reacting after the damage is done.

In terms of AI and digital safety, the simulation shows how important it is to set clear rules for how bots and automated systems can influence people. As bots get smarter, platforms also need tools to track and flag unusual behavior.
This simulation can also help with bot detection research. For example, it can be used to train programs to recognize bots by looking at patterns like bots grouping together, repeating the same content, or causing sudden spikes in engagement.

In short, even though our simulation is simple, it helps start important conversations about AI ethics, online safety, and the future of digital influence. With more improvements, it could be a useful tool for researchers, policymakers, and developers to build safer and more trustworthy online spaces.

---

## §6. References  
- Bessi, A., & Ferrara, E. (2016). *Social bots distort the 2016 U.S. presidential election online discussion*. First Monday, 21(11). [DOI](https://doi.org/10.5210/fm.v21i11.7090)  
- Stella, M., Ferrara, E., & De Domenico, M. (2018). *Bots increase exposure to negative and inflammatory content in online social systems*. PNAS, 115(49), 12435–12440.  
- Varol, O., Ferrara, E., Davis, C., Menczer, F., & Flammini, A. (2017). *Online human-bot interactions: Detection, estimation, and characterization*. ICWSM, 280–289.

---

## §7. Attestation  
We confirm all members contributed meaningfully to the report.

- **Sanchita Chowdhury (219195841)**  
  *Roles*: Conceptualization, Software, Writing - Original Draft, Visualization  
  *Contributions*: Developed simulation logic, refined visualizations, wrote and edited report  

- **Peng Qiu (218419598)**  
  *Roles*: Investigation, Writing - Review & Editing, Validation  
  *Contributions*: Literature research, simulation testing, results analysis, report editing  

- **Hyunji Yun (217968801)**  
  *Roles*: Formal Analysis, Data Curation, Project Administration  
  *Contributions*: Ran simulations, curated data and visuals, ensured content cohesion  
