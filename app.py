import streamlit as st

dashboard = st.Page(
    "pages/stream.py",
    title="Overview",
    icon="📋"
)

products = st.Page(
    "pages/1_products.py",
    title="Products",
    icon="📦"
)

countries = st.Page(
    "pages/2_countries.py",
    title="Countries",
    icon="🌍"
)

customers = st.Page(
    "pages/3_customers.py",
    title="Customers",
    icon="👥"
)

pg = st.navigation([dashboard, products, countries, customers])

pg.run()
