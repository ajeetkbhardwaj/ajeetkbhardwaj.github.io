---
title: "Super-Market Analysis and Prediction using Python and MySQL Database"
excerpt: "Analyzing sales data from a supermarket MySQL database to uncover insights and predict customer behavior. It uses Python, , and machine learning techniques to preprocess data, perform exploratory analysis, and build predictive models for customer types.r 1<br/><img src='/images/supermarket-sales.jpeg'>"
collection: portfolio
url: https://github.com/ajeetkbhardwaj/full-stack-project-portfolio/tree/main/DataScience/SuperMarketSalesAnalysis
category: "Data Analysis"
---
> The Supermarket Sales Analysis and Prediction project is a comprehensive data science workflow that combines data analysis and machine learning to derive actionable insights and predictions from supermarket sales data. The project is divided into two main components:

##### 1. Supermarket Sales Analysis:

**Objective:** Analyze sales data to uncover trends and patterns.
**Technologies Used**: Python, MySQL, Pandas, Matplotlib.
**Key Features:**

* Run the MySQL database application as docker container and connect with the container using python connect and mysql client libraries.
* Connects to a MySQL database to fetch sales data.
* Performs exploratory data analysis (EDA) to identify trends, such as top-selling products, sales by branch, and customer demographics.
* Visualizes data using plots to provide insights into sales performance and customer preferences.

##### 2. Sales Prediction:

**Objective:** Predict customer types (e.g., "Member" or "Normal") based on sales data.
**Technologies Used:** Python, MySQL, Scikit-learn.
**Key Features:**

- Preprocesses data by encoding categorical variables and splitting it into training and testing sets.
- Trains a logistic regression model to predict customer types.
- Evaluates the model's performance using accuracy and classification reports.
- Simulates predictions on new data and stores the results in a MySQL table (sales_predictions).
- Exports predictions to a CSV file for further analysis.
