# Import Streamlit library
import streamlit as st

# Configure browser tab
st.set_page_config(
    page_title="Hotel Booking Analytics & Automated EDA Platform",
    page_icon="🏨",
    layout="wide"
)

# Main title
st.title("🏨 Hotel Booking Analytics & Automated EDA Platform")

# Subtitle
st.subheader(
    "Automated Data Profiling, Business Intelligence "
    "and AI-Generated Insights"
)

# Horizontal divider
st.divider()

# Welcome message
st.write(
    """
    Welcome to the Hotel Booking Analytics Platform.

    This application will help users:

    • Upload hotel booking datasets
    • Perform automated exploratory data analysis
    • Generate business insights
    • Assess data quality
    • Download PDF reports
    """
)