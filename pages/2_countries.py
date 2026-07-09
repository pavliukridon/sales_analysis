import streamlit as st
import pandas as pd
import plotly.express as px
from utils import apply_theme
from data_loader import load_data

data = load_data()

country_summary = data['country_summary']


st.title('Country performance')


kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
country_count = country_summary['Country'].nunique()
top_country = country_summary.iloc[0]['Country']
revenue_of_top_country = country_summary.iloc[0]['Revenue']
avg_revenue_per_country = country_summary['Revenue'].mean()

kpi_col1.metric('Unique Countries', f'{country_count:,}')
kpi_col2.metric('Top Country by Revenue', f'{top_country}')
kpi_col3.metric('Revenue of Top Country', f'${revenue_of_top_country:,.2f}')
kpi_col4.metric('Average Revenue per Country', f'${avg_revenue_per_country:,.2f}')

top_n = st.slider(
    'Top countries',
    min_value=5,
    max_value=50,
    value=10
)

col1, col2 = st.columns(2)
with col1:
    fig = px.bar(
        country_summary
        .nlargest(top_n, 'Revenue')
        .sort_values('Revenue', ascending=True),
        x='Revenue',
        y='Country',
        orientation='h',
        title=f'Top {top_n} Countries by Revenue',
        color='Revenue',
        color_continuous_scale=px.colors.sequential.Viridis
    )
    fig.update_layout(height=450)
    apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.bar(
        country_summary.nlargest(top_n, 'Orders').sort_values('Orders', ascending=True),
        x='Orders',
        y='Country',
        orientation='h',
        title=f'Top {top_n} Countries by Orders',
        color='Orders',
        color_continuous_scale=px.colors.sequential.Viridis
    )
    fig.update_layout(height=450)
    apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)
st.subheader('Country summary')

st.dataframe(country_summary, use_container_width=True)
