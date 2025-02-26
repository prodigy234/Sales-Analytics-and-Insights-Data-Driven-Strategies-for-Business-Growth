# Sales Analytics Project

## Overview
This project performs **sales analytics** on a dataset containing sales transactions. The analysis aims to provide insights into:
- Total sales trends over time
- Best-performing and underperforming products
- Regional sales performance
- Customer spending patterns
- Profitability analysis

Using **Python**, **Pandas**, **Matplotlib**, and **Seaborn**, this project visualizes key insights through bar charts, line plots, box plots, and histograms.

---

## Dataset Information
### **Filename:** `sales_data.csv`
### **Columns in the Dataset:**
- **Date**: The date of the transaction (converted to `datetime` format for time series analysis).
- **Product**: The name of the product sold.
- **Region**: The sales region where the transaction occurred.
- **Customer_ID**: A unique identifier for each customer.
- **Total_Sales**: The total sales amount for the transaction.

---

## Project Structure
```
Sales_Analytics_Project/
│-- sales_data.csv           # Sales dataset
│-- sales_analytics.ipynb    # Jupyter Notebook with code & analysis
│-- sales_analysis.py        # Python script version of the code
│-- README.md                # Project documentation (this file)
```

---

## **Code Explanation**

### **1. Importing Required Libraries**
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
- `pandas`: Handles data processing and aggregation.
- `matplotlib.pyplot`: Used for plotting graphs.
- `seaborn`: Provides enhanced visualization capabilities.

---

### **2. Loading and Cleaning the Dataset**
```python
df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df.columns = df.columns.str.strip()
```
- Reads the CSV file into a Pandas DataFrame.
- Converts the `Date` column into **datetime format** for time-based analysis.
- Ensures column names do not have extra spaces.

---

### **3. Total Sales Over Time**
```python
plt.figure(figsize=(12, 6))
daily_sales = df.groupby("Date")["Total_Sales"].sum()
daily_sales.plot()
plt.title("Total Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid()
plt.show()
```
- Groups data by **Date** and calculates daily **Total Sales**.
- Creates a **line chart** showing sales trends over time.

---

### **4. Top-Selling Products**
```python
top_products = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
top_products.plot(kind="bar", color="skyblue")
plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()
```
- Aggregates **Total Sales per Product**.
- Displays **a bar chart of top-selling products**.

---

### **5. Sales Distribution by Region**
```python
plt.figure(figsize=(8, 5))
sns.boxplot(x="Region", y="Total_Sales", data=df, palette="Set2", hue="Region", legend=False)
plt.title("Sales Distribution by Region")
plt.show()
```
- Uses a **box plot** to show **sales distribution across regions**.
- Helps identify **outliers and trends** within each region.

---

### **6. Total Sales by Region**
```python
plt.figure(figsize=(8, 5))
sns.barplot(x="Region", y="Total_Sales", data=df, palette="Set2", hue="Region", legend=False)
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()
```
- Displays a **bar chart comparing total sales across different regions**.

---

### **7. Customer Spending Distribution**
```python
customer_sales = df.groupby("Customer_ID")["Total_Sales"].sum()
sns.histplot(customer_sales, bins=20, kde=True, color="purple")
plt.title("Customer Spending Distribution")
plt.xlabel("Total Spending")
plt.ylabel("Number of Customers")
plt.show()
```
- Groups data by **Customer_ID** and calculates **total spending per customer**.
- Plots a **histogram to visualize spending patterns**.

---

### **8. Profitability Analysis**
```python
df["Profit"] = df["Total_Sales"] * 0.2
plt.figure(figsize=(10, 5))
profit_by_product = df.groupby("Product")["Profit"].sum().sort_values(ascending=False)
profit_by_product.plot(kind="bar", color="green")
plt.title("Profitability by Product")
plt.xlabel("Product")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)
plt.show()
```
- Assumes a **profit margin of 20%**.
- Groups data by **Product** and calculates total **profit per product**.
- Displays a **bar chart showing the most profitable products**.

---

## **Insights Generated**
1. **Best-Performing Products**: Identifies **top-selling products** by total revenue.
2. **Underperforming Regions & Opportunities**: Finds regions with **low sales** and potential market opportunities.
3. **Customer Behavior**: Analyzes **customer spending trends** to identify high-value customers.
4. **Sales Trends Over Time**: Detects **seasonal trends and growth patterns**.
5. **Profitability Analysis**: Determines **which products generate the highest profits**.

---

## **How to Run the Code**
### **Option 1: Using Jupyter Notebook**
1. Install required libraries:
   ```bash
   pip install pandas matplotlib seaborn
   ```
2. Open the notebook:
   ```bash
   jupyter notebook sales_analytics.ipynb
   ```
3. Run the cells step by step.

### **Option 2: Running as a Python Script**
1. Install required libraries (if not installed):
   ```bash
   pip install pandas matplotlib seaborn
   ```
2. Run the script:
   ```bash
   python sales_analysis.py
   ```

---

## **Possible Future Enhancements**
🔹 **Time Series Forecasting**: Predict future sales using ARIMA, LSTMs, or Facebook Prophet.
🔹 **Customer Segmentation**: Apply machine learning techniques (K-Means clustering) for better targeting.
🔹 **Interactive Dashboards**: Use Power BI, Tableau, or Plotly Dash for better visualization.
🔹 **Geospatial Analysis**: Utilize GeoPandas and Folium for a geographic sales heatmap.

---

## **Author**
- **Name:** Kajola Gbenga
- **Role:** Certified Data Scientist / Certified Data Analyst / Certified SQL Programmer
- **Email:** k.gbenga234@gmail.com
- **LinkedIn:** https://www.linkedin.com/in/kajolagbenga

📌 **If you found this project useful, give it a ⭐ on GitHub!** 🚀