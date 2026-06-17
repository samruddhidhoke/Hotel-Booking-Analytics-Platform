import streamlit as st
import pandas as pd

from utils.database import get_engine
from modules.summary import dataset_summary

st.set_page_config(
    page_title="Hotel Booking Analytics & Automated EDA Platform",
    page_icon="🏨",
    layout="wide"
)

st.title(
    "🏨 Hotel Booking Analytics & Automated EDA Platform"
)

st.subheader(
    "Automated Data Profiling, Business Intelligence "
    "and AI-Generated Insights"
)

st.divider()

st.markdown(
    """
    This dashboard performs automated exploratory data analysis
    on hotel booking data and provides business intelligence insights.
    """
)

# Create database connection
engine = get_engine()

# Load data from SQL Server
query = """
SELECT *
FROM hotel_bookings
"""

df = pd.read_sql(
    query,
    engine
)

# Generate dataset summary
summary = dataset_summary(df)