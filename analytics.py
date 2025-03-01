import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import numpy as np

# Streamlit App Title
st.title("📊 Sales Data Analysis Dashboard")

# Upload Dataset
uploaded_file = st.file_uploader("Upload your sales dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    # Load the dataset
    df = pd.read_csv(uploaded_file)

    # Convert Date column to datetime format
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Date"] = df["Date"].dt.date  # Convert to date-only for Streamlit compatibility

    # Ensure column names are correct
    df.columns = df.columns.str.strip()

    # Dataset Overview
    st.subheader("📌 Dataset Overview")
    st.dataframe(df.astype(str))
    st.subheader("📊 Summary Statistics")
    st.write(df.describe())

    # Total Sales Over Time
    st.subheader("📈 Total Sales Over Time")
    daily_sales = df.groupby("Date")["Total_Sales"].sum()
    fig, ax = plt.subplots(figsize=(12, 6))
    daily_sales.plot(ax=ax)
    ax.set_title("Total Sales Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Sales")
    ax.grid()
    st.pyplot(fig)

    # Top Selling Products
    st.subheader("🏆 Top Selling Products")
    top_products = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
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
    sns.boxplot(x="Region", y="Total_Sales", data=df, palette="Set2", hue="Region", legend=False, ax=ax)
    ax.set_title("Sales Distribution by Region")
    st.pyplot(fig)

    # Total Sales by Region
    st.subheader("📍 Total Sales by Region")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x="Region", y="Total_Sales", hue="Region", data=df, palette="Set2", ax=ax)
    ax.set_title("Total Sales by Region")
    ax.set_xlabel("Region")
    ax.set_ylabel("Total Sales")
    st.pyplot(fig)

    # Customer Purchase Frequency Heatmap
    st.subheader("📊 Customer Purchase Frequency Heatmap")
    customer_frequency = df.pivot_table(index="Customer_ID", values="Total_Sales", aggfunc="count")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(customer_frequency, cmap="Blues", annot=False, ax=ax)
    ax.set_title("Customer Purchase Frequency Heatmap")
    st.pyplot(fig)

    # Sales Contribution by Category (Pie Chart)
    st.subheader("🎂 Sales Contribution by Category")
    category_sales = df.groupby("Category")["Total_Sales"].sum()
    fig, ax = plt.subplots(figsize=(8, 8))
    category_sales.plot(kind="pie", autopct="%1.1f%%", colors=sns.color_palette("pastel"), ax=ax)
    ax.set_title("Sales Contribution by Category")
    ax.set_ylabel("")
    st.pyplot(fig)

    # Quantity Sold per Category
    st.subheader("📦 Quantity Sold per Category")
    category_quantity = df.groupby("Category")["Quantity"].sum().sort_values(ascending=False)
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
    sns.histplot(df["Unit_Price"], bins=30, kde=True, color="red", ax=ax)
    ax.set_title("Price Distribution of Products")
    ax.set_xlabel("Unit Price")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

    # Region-wise Sales Heatmap
    st.subheader("🗺️ Region-wise Sales Heatmap")
    region_sales_matrix = df.pivot_table(index="Region", values="Total_Sales", aggfunc="sum")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(region_sales_matrix, cmap="coolwarm", annot=True, fmt=".0f", linewidths=0.5, ax=ax)
    ax.set_title("Region-wise Sales Heatmap")
    st.pyplot(fig)

    # Sales vs. Profit Scatter Plot 
    df["Profit"] = df["Total_Sales"] * 0.2
    if "Profit" in df.columns and not df["Profit"].isnull().all():
        st.subheader("📉 Sales vs. Profit Correlation")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=df, x="Total_Sales", y="Profit", alpha=0.6, ax=ax)
        ax.set_title("Sales vs. Profit Correlation")
        ax.set_xlabel("Total Sales")
        ax.set_ylabel("Profit")
        ax.grid()
        st.pyplot(fig)
    else:
        st.warning("⚠️ 'Profit' column is missing or contains only null values. Scatter plot not displayed.")

    # Word Cloud for Most Sold Products
    st.subheader("☁️ Most Sold Products Word Cloud")
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(df["Product"].astype(str)))
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    ax.set_title("Most Sold Products Word Cloud")
    st.pyplot(fig)

    st.success("✅ Analysis Completed!")