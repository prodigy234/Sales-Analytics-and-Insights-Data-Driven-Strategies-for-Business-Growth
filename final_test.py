import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Streamlit App Title
st.title("📊 Sales Data Analysis Dashboard")

# Automatically load dataset (no upload needed)
DATA_PATH = "sales_data.csv"
df = pd.read_csv(DATA_PATH)

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Date"] = df["Date"].dt.date
df.columns = df.columns.str.strip()

# -------------------------
# 🔥 Outstanding Features
# -------------------------

# Sidebar Filters
st.sidebar.header("📂 Filter Options")

# Date Range Filter
min_date = min(df["Date"])
max_date = max(df["Date"])
start_date, end_date = st.sidebar.date_input("Select Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)

# Category Filter
selected_category = st.sidebar.multiselect("Filter by Category", options=df["Category"].unique(), default=df["Category"].unique())

# Product Filter
selected_product = st.sidebar.multiselect("Filter by Product", options=df["Product"].unique(), default=df["Product"].unique())

# Region Filter
selected_region = st.sidebar.multiselect("Filter by Region", options=df["Region"].unique(), default=df["Region"].unique())

# Apply all filters
filtered_df = df[
    (df["Date"] >= start_date) & (df["Date"] <= end_date) &
    (df["Category"].isin(selected_category)) &
    (df["Product"].isin(selected_product)) &
    (df["Region"].isin(selected_region))
]

# KPI Metrics
st.subheader("📌 Key Performance Indicators")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Sales", f"${filtered_df['Total_Sales'].sum():,.2f}")
with col2:
    st.metric("Total Quantity Sold", int(filtered_df["Quantity"].sum()))
with col3:
    st.metric("Unique Products", filtered_df["Product"].nunique())

# Correlation Heatmap
st.sidebar.markdown("---")
if st.sidebar.checkbox("Show Correlation Heatmap", value=True):
    st.subheader("🧠 Correlation Heatmap")
    corr = filtered_df.select_dtypes(include=[np.number]).corr()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# Monthly Sales Trend
st.sidebar.markdown("---")
if st.sidebar.checkbox("Show Monthly Sales Trend", value=True):
    st.subheader("📅 Monthly Sales Trend")
    df_monthly = filtered_df.copy()
    df_monthly["Month"] = pd.to_datetime(df_monthly["Date"]).dt.to_period("M").dt.to_timestamp()
    monthly_sales = df_monthly.groupby("Month")["Total_Sales"].sum()
    fig, ax = plt.subplots(figsize=(10, 5))
    monthly_sales.plot(marker='o', ax=ax)
    ax.set_title("Monthly Sales Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Sales")
    st.pyplot(fig)

# -------------------------
# 📈 Sales Prediction Model
# -------------------------
st.sidebar.markdown("---")
if st.sidebar.checkbox("📡 Predict Future Sales", value=True):
    st.subheader("🔮 Future Sales Prediction")
    pred_df = filtered_df.copy()
    pred_df["Date_Ordinal"] = pd.to_datetime(pred_df["Date"]).map(pd.Timestamp.toordinal)
    X = pred_df[["Date_Ordinal"]]
    y = pred_df["Total_Sales"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Future dates
    future_days = st.slider("Select how many future days to predict", 7, 60, 30)
    last_date = pd.to_datetime(filtered_df["Date"]).max()
    future_dates = [last_date + pd.Timedelta(days=i) for i in range(1, future_days + 1)]
    future_ordinals = [d.toordinal() for d in future_dates]
    future_preds = model.predict(np.array(future_ordinals).reshape(-1, 1))
    
    pred_chart = pd.DataFrame({"Date": future_dates, "Predicted_Sales": future_preds})
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(pred_chart["Date"], pred_chart["Predicted_Sales"], label="Predicted Sales", color="green")
    ax.set_title("Future Sales Forecast")
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales")
    ax.legend()
    st.pyplot(fig)

# -------------------------
# ✅ Original Dashboard Code
# -------------------------

# (Your original full dashboard code continues unmodified below)
# ...
# Dataset Overview
st.subheader("📌 Dataset Overview")
st.dataframe(filtered_df.astype(str))
st.subheader("📊 Summary Statistics")
st.write(filtered_df.describe())

# Total Sales Over Time
st.subheader("📈 Total Sales Over Time")
daily_sales = filtered_df.groupby("Date")["Total_Sales"].sum()
fig, ax = plt.subplots(figsize=(12, 6))
daily_sales.plot(ax=ax)
ax.set_title("Total Sales Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Total Sales")
ax.grid()
st.pyplot(fig)

# Top Selling Products
st.subheader("🏆 Top Selling Products")
top_products = filtered_df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(10, 5))
top_products.plot(kind="bar", color="skyblue", ax=ax)
ax.set_title("Top Selling Products")
ax.set_xlabel("Product")
ax.set_ylabel("Total Sales")
plt.xticks(rotation=45)
st.pyplot(fig)

# Sales by Region
st.subheader("🌍 Sales Distribution by Region")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x="Region", y="Total_Sales", data=filtered_df, palette="Set2", hue="Region", legend=False, ax=ax)
ax.set_title("Sales Distribution by Region")
st.pyplot(fig)

# Total Sales by Region
st.subheader("📍 Total Sales by Region")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x="Region", y="Total_Sales", hue="Region", data=filtered_df, palette="Set2", ax=ax)
ax.set_title("Total Sales by Region")
ax.set_xlabel("Region")
ax.set_ylabel("Total Sales")
st.pyplot(fig)

# Customer Purchase Frequency Heatmap
st.subheader("📊 Customer Purchase Frequency Heatmap")
customer_frequency = filtered_df.pivot_table(index="Customer_ID", values="Total_Sales", aggfunc="count")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(customer_frequency, cmap="Blues", annot=False, ax=ax)
ax.set_title("Customer Purchase Frequency Heatmap")
st.pyplot(fig)

# Sales Contribution by Category (Pie Chart)
st.subheader("🎂 Sales Contribution by Category")
category_sales = filtered_df.groupby("Category")["Total_Sales"].sum()
fig, ax = plt.subplots(figsize=(8, 8))
category_sales.plot(kind="pie", autopct="%1.1f%%", colors=sns.color_palette("pastel"), ax=ax)
ax.set_title("Sales Contribution by Category")
ax.set_ylabel("")
st.pyplot(fig)

# Quantity Sold per Category
st.subheader("📦 Quantity Sold per Category")
category_quantity = filtered_df.groupby("Category")["Quantity"].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=category_quantity.index, y=category_quantity.values, hue=category_quantity.index, palette="coolwarm", ax=ax)
ax.set_title("Quantity Sold per Category")
ax.set_xlabel("Category")
ax.set_ylabel("Total Quantity Sold")
plt.xticks(rotation=45)
st.pyplot(fig)

# Price Distribution
st.subheader("💰 Price Distribution")
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(filtered_df["Unit_Price"], bins=30, kde=True, color="red", ax=ax)
ax.set_title("Price Distribution of Products")
ax.set_xlabel("Unit Price")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Region-wise Sales Heatmap
st.subheader("🗺️ Region-wise Sales Heatmap")
region_sales_matrix = filtered_df.pivot_table(index="Region", values="Total_Sales", aggfunc="sum")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(region_sales_matrix, cmap="coolwarm", annot=True, fmt=".0f", linewidths=0.5, ax=ax)
ax.set_title("Region-wise Sales Heatmap")
st.pyplot(fig)

# Sales vs. Profit Scatter Plot 
filtered_df["Profit"] = filtered_df["Total_Sales"] * 0.2
if "Profit" in filtered_df.columns and not filtered_df["Profit"].isnull().all():
    st.subheader("📉 Sales vs. Profit Correlation")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=filtered_df, x="Total_Sales", y="Profit", alpha=0.6, ax=ax)
    ax.set_title("Sales vs. Profit Correlation")
    ax.set_xlabel("Total Sales")
    ax.set_ylabel("Profit")
    ax.grid()
    st.pyplot(fig)
else:
    st.warning("⚠️ 'Profit' column is missing or contains only null values. Scatter plot not displayed.")

# Word Cloud for Most Sold Products
st.subheader("☁️ Most Sold Products Word Cloud")
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(filtered_df["Product"].astype(str)))
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
ax.set_title("Most Sold Products Word Cloud")
st.pyplot(fig)

st.success("✅ Analysis Completed!")

# -------------------------
# 📥 Downloadable Report
# -------------------------
st.subheader("📄 Download Sales Report")

# Add Download Button for Word Report
try:
    with open("sales_analytics_report.docx", "rb") as file:
        st.download_button(
            label="📥 Click to Download Sales Analysis Report (Word)",
            data=file,
            file_name="Sales_Analysis_Report.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
except FileNotFoundError:
    st.error("❌ Word report file not found. Please ensure 'Sales_Analysis_Report.docx' is in the same directory as this script.")
