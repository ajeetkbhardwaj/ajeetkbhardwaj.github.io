---
title: 'Machine Learning Systems by '
date: 2025-08-03
permalink: /posts/2025/08/blog-post-1/
tags:
  - cool posts
  - category1
  - category2
---
**What does it mean to master machine learning systems—not just design models?**

Machine Learning Systems

- a discipline that combines the science of learning with the practical realities of deployment at scale on infrastructure.
- It extends beyond model development to encompass the full lifecycle of intelligent systems—from data to deployment, from theory to engineering practice.
- It's used for building AI systems that are powerfull, realiable, efficient and grounded in the real-world constraints.

**What are the AI Systems Pervasiveness in Human History, Today ?**

19th century - Industrial Revolution shaped by Power of physical energy through steam power and mechaization transfromation

20th centuray - Digital Revolution, where the computer and internet transformed how we process and share information.

21th century - AI Revolution, according to leading thinkers in tech evolutions.

AI Systems

1. Manages traffic flows in Cities
2. Optimize power distribution across electical grids
3. Enable billions of wireless devices to communicate seamlessly.
4. Helps doctors to diagnose diseases, via providing insight from anaysis of medical images.
5. Accelerates scientific discovery by simulations and processing of vast amount of scientific data in research labs.
6. Helps rovers to nevigate distant planets and telescopes to detect new celestial object or events, in  space exploration.

We aspire to create systems that can work alongside humanity, enhancing our problem-solving capabilities and accelerating scientific progress.

Systems that understand consciousness, decode the complexities of complex biological systems or uncover the mystries of dark matter and dark energy.

Systems that can help adressing global challenges like climate change, disease or sustainable energy production.

Thus, Build AI systems is not only about automation or efficiency but it's also about how boundaries of human knowledge and capabilities can be expanded ?

AI Revolution operates at multiple scales Thus, poses multiple implications today such as

1. Individual Level -
2. Organizational Level -
3. Societal Level -
4. Government Level -
5. Global Level -

AI Revolution Challenge - Learning to Master, how to build systems that can learn, reason and potentially achieve superhuman capabilities in specific domains.

**What are the fundamentals of AI and ML Systems ?**
How can we create these intelligent capabilities ? We first needed to understand the relationship between AI and ML Systems that provides not only theoretical but also practical framework to adress such questions.

AI Systems - Understand and replicate intelligent behaviour such as capcity to learn, reason and adapt new situations.

AI : Nature of Intelligence, Knowledge and Learning
How do we recognize patterns ?
How do we learn from experiance ?
How do we adapt our behaviour based on new information ?

Explores these questions in different fields such as cognitive science, psychology, neuroscience and computer science.

ML Systems - Creating systems that demonstrats intelligent behaviour. Building systems that utilizes data and optimization techniques to identify patterns and relationships automatically rather than some predefined set of rules.

Biological Systems <=> ML Systems

1. Human Visual Learning Process - Object Recognition
2. Human Language - NLP to process textual data

### Case Studies 

#### Uber - Demand and ETR Forecast at Airports


1. **Business Problem Statement**

Airports represent a critical node in Uber’s operations, with large concentrations of available drivers often waiting in FIFO queues for trip requests. Imbalances occur when the supply of drivers doesn’t match passenger demand:  
- **Undersupply**: Too few drivers mean longer rider wait times and missed opportunities for Uber to fulfill trips, leading to poor customer experience and potential revenue loss.  
- **Oversupply**: Too many drivers lead to long idle times, decreased earnings satisfaction among drivers, and reduced driver retention.  
Currently, drivers lack visibility into queue conditions, resulting in inefficient supply allocation and worsening the problem.  
**The business goal is to optimize the driver supply at airports by providing actionable insights, improving trip fulfillment rates for passengers, and maximizing productive time and satisfaction for drivers.**

***

2. **Machine Learning Problem Statement**

**How can we accurately forecast “Estimated Time to Request (ETR)” for each driver entering an airport queue, based on real-time and historical data, so drivers can make informed positioning decisions?**  
This involves predicting the wait time before a driver receives a trip request at a given airport, given features such as:
- Current queue length (number of waiting drivers)
- Recent trip request rates (demand)
- Arrival rates of new drivers
- Flight arrival schedules
- Day of week, time of day, holidays, weather, etc.  
The output is a continuous variable: the predicted wait time (ETR) for a driver.

***

3. **ML Solution Idea and Model**

**Solution Approach** : 
Train a regression model to predict ETR at specific airports, leveraging historical queue, demand, and contextual data.

0.  **Model Workflow**
1. **Data Collection**
   - Historical trips and driver queue data at airports.
   - Real-time driver supply and trip demand metrics.
   - External features: flight schedules, weather, local events.

2. **Feature Engineering**
   - Queue position, current queue length.
   - Recent driver arrival/departure rates.
   - Recent passenger demand trends.
   - Temporal features: hour, day, seasonality.
   - External dependencies: major event schedules, delays.

3. **Model Selection**
   - **Supervised regression algorithms**: Choices could include Random Forest, Gradient Boosting (e.g., XGBoost), or Neural Networks if the data is large and complex.
   - Models trained to minimize error between predicted and actual wait times.

4. **Prediction and Deployment**
   - Model generates dynamic ETR estimates for every driver in the airport queue.
   - ETR exposed in the driver app, allowing drivers to see current and projected wait times.

5. **Iterative Improvement**
   - Continuous retraining with new data.
   - Feedback loop: evaluate model impact on wait times, queue sizes, and rider/driver satisfaction.

***

- Summary Table

| Step | Business Focus        | ML Implementation                |
|------|----------------------|----------------------------------|
| 1    | Align supply/demand  | Collect queue & demand data      |
| 2    | Improve wait times   | Build wait-time regression model |
| 3    | Guide drivers        | Show ETR in driver app           |
| 4    | Continuous optimize  | Retrain, monitor, update         |

***

By forecasting ETR and sharing that insight, Uber can **balance driver supply at airports, boost rider fulfillment rates, and improve driver satisfaction**—all through an actionable, ML-powered solution.



### References

[1]. [Uber- Demand and ETR Forecast at Airports](https://www.uber.com/en-GB/blog/demand-and-etr-forecasting-at-airports/)
