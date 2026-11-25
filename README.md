# E-commerce Sales & Customer Behavior Analysis
## Project Overview

This project analyzes e-commerce sales data to identify revenue drivers, product performance, sales trends, and customer behavior.
The analysis was conducted using Python and SQL, with visualizations to communicate key business insights.

## Business Questions
1. Which product categories generate the most revenue?
2. Which products are the top revenue contributors?
3. How does revenue change over time?
4. Which cities generate the highest revenue?
5. Which payment methods contribute the most revenue?
6. How do discount levels relate to average revenue?
7. Who are the highest-value customers?

## Tools
- Python
- Pandas
- NumPy
- Matplotlib
- SQL
- SQLite
- VS Code

## Key Findings
### 1. Electronics is the main revenue driver

Electronics generated approximately ¥10.34 million in revenue, representing 40.39% of total revenue.

### 2. Power Bank is the top revenue-generating product

Power Bank generated approximately ¥22.16 million in revenue, making it the highest-revenue product in the dataset.

### 3. Revenue varies across cities

The analysis shows differences in total revenue across cities, indicating that geographic performance varies across the market.

### 4. Higher discount levels are associated with lower average transaction revenue

Average revenue per transaction decreased as the discount level increased. For example, transactions with no discount had an average revenue of approximately ¥23,182, compared with approximately ¥18,843 for transactions with a 20% discount.

This represents an association in the observed data and does not establish causation.

### 5. Customer spending varies significantly

Customer analysis identified different spending levels, allowing customers to be grouped into Low Value, Medium Value, and High Value segments.

## Methodology
1. **Data Preparation**
   - Loaded the e-commerce dataset using Pandas.
   - Checked data types, missing values, and duplicate records.
   - Reviewed descriptive statistics to identify potential data quality issues.

2. **Exploratory Data Analysis**
   - Analyzed revenue by category, product, city, and payment method.
   - Examined monthly revenue trends.
   - Evaluated the relationship between discount levels and transaction revenue.

3. **SQL Analysis**
   - Used SQLite to perform business-oriented queries.
   - Analyzed total revenue, transaction volume, average order value, and customer spending.

4. **Customer Segmentation**
   - Grouped customers based on their total spending.
   - Classified customers into Low Value, Medium Value, and High Value segments.

5. **Data Visualization**
   - Created charts using Matplotlib to communicate key findings and business insights.
