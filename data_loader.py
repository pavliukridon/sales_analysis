import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    return {
        'monthly_sales': pd.read_csv('data/sales_by_month.csv'),
        'weekly_sales': pd.read_csv('data/sales_by_weekday.csv'),
        'product_revenue': pd.read_csv('data/products_by_revenue.csv'),
        'product_sales': pd.read_csv('data/products_by_sales.csv'),
        'segments': pd.read_csv('data/segment_size.csv'),
        'rfm': pd.read_csv('data/rfm.csv'),
        'kpi': pd.read_csv('data/kpi.csv'),
        'country_summary': pd.read_csv('data/country_summary.csv'),
        'customer_summary': pd.read_csv('data/customer_summary.csv'),
        'product_summary': pd.read_csv('data/product_summary.csv'),
    }
