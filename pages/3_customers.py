import streamlit as st
import pandas as pd
import plotly.express as px
from utils import apply_theme
from data_loader import load_data

data = load_data()

segments = data['segments']
rfm = data['rfm']
customer_summary = data['customer_summary']
st.title('Customer Analysis')
total_customers = customer_summary['CustomerID'].nunique()
avg_revenue_per_customer = customer_summary['Revenue'].mean()
avg_orders = customer_summary['Orders'].mean()
avg_quantity_per_customer = customer_summary['Quantity'].mean()

kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
kpi_col1.metric('Total Customers', f'{total_customers:,}')
kpi_col2.metric('Average Revenue per Customer', f'${avg_revenue_per_customer:,.2f}')
kpi_col3.metric('Average Orders per Customer', f'{avg_orders:,.2f}')
kpi_col4.metric('Average Quantity per Customer', f'{avg_quantity_per_customer:,.2f}')


customer_revenue = (
    customer_summary.nlargest(10, 'Revenue')
    .sort_values('Revenue', ascending=True)
    .reset_index(drop=True)
)

customer_revenue['CustomerID'] = customer_revenue['CustomerID'].astype(str)

col1, col2 = st.columns(2)
with col1:
    fig = px.bar(
        customer_revenue,
        x='Revenue',
        y='CustomerID',
        orientation='h',
        title='Top 10 Customers by Revenue',
        color='Revenue',
        color_continuous_scale=px.colors.sequential.Viridis
    )
    fig.update_layout(height=350)
    apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.bar(
        segments,
        x='Segment',
        y='Count',
        title='Customer Segments',
        color='Count',
        color_continuous_scale=px.colors.sequential.Viridis
    )
    fig.update_layout(height=350)
    apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)




segment_summary = (
    rfm.groupby('Segment')
    .agg(
        Customers=('Segment', 'size'),
        Avg_Monetary=('monetary', 'mean'),
        Avg_Frequency=('frequency', 'mean'),
        Avg_Recency=('recency', 'mean')
    )
    .reset_index()
)

st.dataframe(segment_summary, use_container_width=True)
