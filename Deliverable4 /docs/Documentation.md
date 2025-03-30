# Prototype Documentation

## Purpose

The purpose of this simulation is to explore how bots working together can make certain content more visible, influence how people react, and affect the overall flow of information online.  
The main goal is to study a behavior called **"engagement hijacking,"** where bots team up to boost specific messages, draw public attention to them, and hide other diverse opinions.

---

## Implementation Details

### Platform & Tools

- **Framework:** Mesa (Python-based ABM library)  
- **Network Engine:** NetworkX (Erdős–Rényi graphs for simulating connections)  
- **Visualization:** Mesa’s `NetworkModule` + `ChartModule`  
- **User Interface:** Sliders and dropdowns to control agent count and bot scenarios  
- **Data Collection:** Built-in `DataCollector` (tracks engagement, influence, etc.)

### Key Features

#### Two Agent Types

- **Bots:** Coordinate behavior to amplify chosen content  
- **Humans:** React to content, influenced by what’s already amplified

#### Dynamic Parameters

Users can vary the number of bots, humans, and removed bots after a certain time step to simulate moderation efforts.

#### Scenario Modes

- No Bots  
- Partial Bots  
- All Bots  

This allows comparison across varying levels of automation and coordination.

#### Boid-Inspired Bot Behavior

Bots exhibit simplified flocking behavior:

- **Alignment:** Bots mimic the most engaging peers  
- **Cohesion:** Bots cluster within human groups  
- **Separation:** Bots avoid overlapping efforts for maximum spread

### Metrics Collected

- Total & average engagement for bots vs. humans  
- Real-time network visuals  
- *(Upcoming)* Content diversity scores using entropy

---

## Preliminary Findings

### Bots Drive Engagement Early

Bots consistently show higher initial influence and engagement compared to humans. This means that bots inflate metrics to trigger algorithmic boosts.

### Content Exposure Becomes Skewed

As bots amplify certain content repeatedly, human agents increasingly engage with those same topics, limiting exposure to diverse ideas—this simulates how echo chambers form.

### Influence Gap Widens Over Time

Even when some bots are removed after a few steps, the remaining bots maintain enough momentum to continue dominating the feed. Human agents seldom regain visibility.

### Partial Bot Removal Is Not Enough

Removing a small number of bots slows amplification but does not stop it—suggesting that platform interventions need to be more comprehensive or systemic.
