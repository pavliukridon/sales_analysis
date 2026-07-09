import streamlit as st
import pandas as pd
import plotly.express as px
from utils import apply_theme
st.set_page_config(page_title="Sales Dashboard", layout="wide")
from data_loader import load_data
data = load_data()

monthly_sales = data['monthly_sales']
weekly_sales = data['weekly_sales']
kpi = data['kpi']





st.title("Sales Dashboard")
st.write("Data source: [Kaggle](https://www.kaggle.com/datasets/carrie1/ecommerce-data)")
st.subheader("Key Performance Indicators (KPIs)")

revenue = kpi.loc[kpi["Metric"] == "Revenue", "Value"].values[0]
orders = kpi.loc[kpi["Metric"] == "Orders", "Value"].values[0]
customers = kpi.loc[kpi["Metric"] == "Customers", "Value"].values[0]
avg_check = kpi.loc[kpi["Metric"] == "Average Check", "Value"].values[0]



col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"${revenue:,.2f}")
col2.metric("Total Orders", f"{orders:,.0f}")
col3.metric("Total Customers", f"{customers:,.0f}")
col4.metric("Average Order Value", f"${avg_check:,.2f}")


chart1, chart2 = st.columns(2)
with chart1:
    fig = px.line(
        monthly_sales,
        x='Month',
        y='Revenue',
        title='Monthly Revenue Trend',
        markers=True
    )
    fig.update_layout(height=450)
    apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

with chart2:
    bar = px.bar(
        weekly_sales,
        x='Weekday',
        y='Revenue',
        title='Sales by Weekday',
        color='Revenue',
        color_continuous_scale=px.colors.sequential.Viridis
    ) 
    bar.update_layout(height=450)
    apply_theme(bar)
    st.plotly_chart(bar, use_container_width=True)





