# **Coordinated AI Bot Influence**

## **Team Members**
- Hyunji Yun
- Peng Qiu
- Sanchita Chowdhury

## **GitHub Repository**
[[GitHub Repo URL](https://github.com/4461-Project/Group7.git)]

---

## **Section 1: Phenomena of interest**
Inspired by the Coordinated AI Bot Influence model, we plan to simulate how social robots on social media platforms achieve collective goals through coordinated actions, such as promoting and amplifying specific information or hashtags to suppress opposing views. For example, social bots can strategically dilute and drown out opposing viewpoints by repeatedly posting and sharing information they like or liking relevant content. This behaviour shapes the information flow but also subconsciously influences people's perceptions because this will lead the users more easily to see and engage with the amplified content, which it also prevents users from seeing opposing views. This phenomenon is particularly prominent in mainstream social media platforms (such as X, and Instagram), where algorithmic recommendations and interactions between robots play a key role in content visibility and public opinion guidance. Through simulation, we hope to reveal how robot collaboration affects the dynamics of information dissemination and further explore its potential impact on public opinion formation.

## **Section 2: Phenomena of interest**
This study analyzes how social media bots distorted online discussions during the 2016 US presidential election. Using advanced detection algorithms, we found that 20% of the conversations were not human users, which are all social bots. The final results show that bots exacerbate political polarization and distort candidates' public image. They imitate the real user's content dissemination strategies and threaten the fairness of elections by amplifying the negative events.

Bessi, A., & Ferrara, E. (2016). Social bots distort the 2016 U.S. presidential election online discussion. First Monday, 21(11). https://doi.org/10.5210/fm.v21i11.7090

This study analyzed tweets during the 2017 Catalan referendum and found that nearly a third of the accounts were social media bots. These social bots spread a lot of negative content, such as police violence and dictatorship, targeting the views of independent leaders. Based on network analysis, it shows that social bots increased polarization by synchronizing negative replies. Based on sentiment analysis, it shows that social bots increased panic, fear, and condemnation during the voting period by promoting news headlines. As a result, the sentiment value of the pro-independence community plummeted. Therefore, this action changed public opinion and undermined the integrity and fairness during the referendum.

Stella, M., Ferrara, E., & De Domenico, M. (2018). Bots increase exposure to negative and inflammatory content in online social systems. Proceedings of the National Academy of Sciences, 115(49), 12435–12440. https://doi.org/10.1073/pnas.1803470115
## **Section 3: Describe the Core Components of the Simulation**

Our simulation is inspired by the Boid Flocking Model from NetworkX, which showcases how simple rules can cause coordinated group behavior. Just like how birds and fish move together in a group, social bots on media platforms coordinate actions like amplifying content, creating fake consensus, and diluting opposing views.

(3.1) Entities: Humans and Social Bots <br>
Humans: <br>
Role: Regular social media users who consume and interact with content. <br>
Behavior: Like, share, comment, and post original content. Their engagement influences algorithmic recommendations. <br>
Goal: Access information, express opinions, and participate in discussions.<br>

Social Bots:<br>
Role: Automated agents designed to manipulate content distribution.<br>
Behavior: Like, share, and post content in a coordinated manner to amplify specific sides of a story.<br>
Goal: Increase visibility of targeted content, limit/hide opposing views, and influence public opinion.<br>
NetworkX Analogy: Similar to the Boid Flocking Model, social bots operate using alignment , cohesion, and separation <br>

(3.2) Affordances of the Content
Tagging & Hashtags: Bots exploit hashtags to amplify specific topics. <br>
Sharing & Retweeting: Bots spread content in a quick manner to increase its visibility.<br>
Up/Down Voting: Bots manipulate engagement metrics <br>
Emotional Manipulation: Bots generate and spread content designed to promote strong reactions such as fear, anger etc. <br>
NetworkX Analogy: Similar to how a computer virus affects a network Model, by spreading across nodes, bots spread influence through interactions, boosting content visibility and controlling discourse. <br>

(3.3) Algorithms Involved
Recommendation Algorithms: Social media platforms prioritize content based on engagement. Bots artificially inflate engagement.<br>
Content Prioritization: Algorithms highlight trending content, which bots can manipulate.<br>
Filter Bubbles: Repeated interactions with bot-influenced content create echo chambers.<br>




## **Section 4: Simulation Anticipated Outcomes**
![Algorithms: Content Visibility Over Time](https://private-user-images.githubusercontent.com/96277611/413692384-3fe1abea-9788-434f-8da6-e5528cb05ff5.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzk3NjQ3NjgsIm5iZiI6MTczOTc2NDQ2OCwicGF0aCI6Ii85NjI3NzYxMS80MTM2OTIzODQtM2ZlMWFiZWEtOTc4OC00MzRmLThkYTYtZTU1MjhjYjA1ZmY1LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMTclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjE3VDAzNTQyOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWMyMTRkNzBiOWVkYzA5Mjk0Y2UxMmRlNjQ2NjkwY2M3Yjc4ZWIyZDQ5OGEzZWU5OWMxMjA2NzMzYWVjYWQyM2YmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.0P1MnLzTtBsXocbSIMa0647BP0Md7Tmk3mOiidfRT0o)


Below are simulation drafts of our phenomena of interest:
1st graph : Entities (Humans & Social Bots)
Red nodes  are social Bots
Blue nodes are human Users
Edges represent social interactions.
Bots form clusters, amplifying messages and manipulating discussions/engagements.
2nd graph : Affordances (Content Interaction)
Simulates social media actions (e.g., Liking, Sharing, Retweeting, Up/Down Voting).
Shows how content flows through the network.
Users interact based on platform affordances.
3rd graph: Algorithms (Prioritizing engagement)
Bot engagement grows exponentially (represented by the red dashed line on the graph).
Human engagement is growing much slower (represented by the Blue solid line).
This graph showcases how algorithms prioritize engagement amplified by bots, further reinforcing their influence.


