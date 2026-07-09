import streamlit as st
import pandas as pd
import plotly.express as px
from utils import apply_theme
from data_loader import load_data

data = load_data()

product_revenue = data['product_revenue']
product_sales = data['product_sales']
product_summary = data['product_summary']
st.title('Product performance')
unique_products = product_summary["Description"].nunique()
total_revenue = product_summary["Revenue"].sum()
total_quantity = product_summary["Quantity"].sum()
avg_revenue = product_summary["Revenue"].mean()

kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
kpi_col1.metric("Unique Products", f"{unique_products:,}")

kpi_col2.metric("Total Revenue", f"${total_revenue:,.2f}")
kpi_col3.metric("Total Quantity Sold", f"{total_quantity:,}")
kpi_col4.metric("Average Revenue per Product", f"${avg_revenue:,.2f}")

top_n = st.slider(
    'Top products',
    min_value=5,
    max_value=50,
    value=10
)

col1, col2 = st.columns(2)
with col1:
    fig = px.bar(
        product_revenue.nlargest(top_n, 'Revenue').sort_values('Revenue', ascending=True),
        x='Revenue',
        y='Description',
        orientation='h',
        title=f'Top {top_n} Products by Revenue',
        color='Revenue',
        color_continuous_scale=px.colors.sequential.Viridis
    )
    fig.update_layout(height=450)
    apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.bar(
        product_sales.nlargest(top_n, 'Quantity').sort_values('Quantity', ascending=True),
        x='Quantity',
        y='Description',
        orientation='h',
        title=f'Top {top_n} Products by Quantity Sold',
        color='Quantity',
        color_continuous_scale=px.colors.sequential.Viridis
    )
    fig.update_layout(height=450)
    apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)


col3, col4 = st.columns(2)
with col3:
    fig = px.scatter(
        product_summary.nlargest(top_n, 'Revenue'),
        x='Quantity',
        y='Revenue',
        size='Orders',
        color='Orders',
        hover_name='Description',
        title='Revenue vs Quantity',
        color_continuous_scale=px.colors.sequential.Viridis
    )
    fig.update_layout(height=350)
    apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

with col4:
    st.subheader('Product Summary')
    st.dataframe(
        product_summary.nlargest(top_n, 'Revenue').sort_values('Revenue', ascending=False).reset_index(drop=True),
        use_container_width=True
    )
