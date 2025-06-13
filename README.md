# 📊 Sales Analytics Dashboard

This project is a comprehensive **Sales Data Analysis Dashboard** built with **Streamlit**. It enables businesses to explore, visualize, and gain actionable insights from their sales data through intuitive filters, interactive plots, and predictive modeling.

---

## 📬 Author

**Gbenga Kajola**

[LinkedIn](https://www.linkedin.com/in/kajolagbenga)

[Certified_Data_Scientist](https://www.datacamp.com/certificate/DSA0012312825030)

[Certified_Data_Analyst](https://www.datacamp.com/certificate/DAA0018583322187)

[Certified_SQL_Database_Programmer](https://www.datacamp.com/certificate/SQA0019722049554)


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

## 📁 Project Structure

```
Sales Analytics and Insights Data-Driven Strategies for Business Growth/
├── sales_data.csv                    # Sales dataset
├── final_test.py                     # Streamlit dashboard application
├── sales_analytics.ipynb             # Jupyter Notebook 
├── requirements.txt                  # Installation of Dependencies
├── README_Sales_Analytics.docx       # README in docx format
└── README.md                         # Project documentation
```

---

## 🚀 Features

### 🎯 Key Functionalities

- **Sidebar Filtering**:
  - Filter sales data by **date range**, **category**, **product**, and **region**.

- **KPI Metrics**:
  - Total Sales
  - Total Quantity Sold
  - Unique Products Sold

- **Visual Analysis**:
  - Correlation Heatmap
  - Monthly Sales Trend
  - Sales Over Time
  - Top Selling Products
  - Sales Distribution by Region
  - Category-wise Sales Contribution
  - Quantity Sold per Category
  - Price Distribution Histogram
  - Region-wise Sales Heatmap
  - Word Cloud of Products Sold
  - Sales vs Profit Correlation

- **Predictive Modeling**:
  - Predict future sales using Linear Regression
  - Adjustable prediction window (7 to 60 days)

- **Report Download**:
  - Users can download an automated Word report of the analysis

---

## 🧠 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Data Manipulation**: `pandas`, `numpy`
- **Visualization**: `matplotlib`, `seaborn`, `wordcloud`
- **Machine Learning**: `scikit-learn` (Linear Regression)
- **Report Generation**: `python-docx`

---

## 📊 Sample KPIs (based on filters)

- **Total Sales**: Computed using `filtered_df['Total_Sales'].sum()`
- **Quantity Sold**: `filtered_df['Quantity'].sum()`
- **Unique Products**: `filtered_df['Product'].nunique()`

---

## 🔍 Insights Extracted

- **Time Trends**: Users can see monthly trends and forecast future sales.
- **Sales Distribution**: Heatmaps and boxplots highlight regional and customer behaviors.
- **Top Performers**: Identify top-selling products and high-performing categories.
- **Pricing Behavior**: Histogram shows unit price spread.
- **Customer Frequency**: Heatmap shows which customers buy more frequently.

---

## 🧪 How to Run

1. Clone this repo:
    ```bash
    https://github.com/prodigy234/Sales-Analytics-and-Insights-Data-Driven-Strategies-for-Business-Growth.git
    cd Sales Analytics and Insights Data-Driven Strategies for Business Growth
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Launch the Streamlit app:
    ```bash
    streamlit run final_test.py
    ```

---

## ⚙️ Requirements

Install these packages using `pip install -r requirements.txt`:

```txt
streamlit
pandas
matplotlib
seaborn
numpy
scikit-learn
wordcloud
python-docx
```

---

## 📄 Report Output

At the bottom of the dashboard, a Word document can be downloaded containing summaries of the insights.

---

## 👨‍💻 Author

**Kajola Gbenga**  
Data Analyst | AI Developer | Streamlit Expert

---

## 📬 Contact

- Email: kajolagbenga@example.com  
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/your-profile)  

---

## 📌 License

This project is licensed under the MIT License.
