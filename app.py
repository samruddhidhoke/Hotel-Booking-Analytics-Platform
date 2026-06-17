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

# Display summary dictionary temporarily
st.write(summary)

st.divider()

st.header("📊 Dataset Overview")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        label="Rows",
        value=summary["rows"]
    )
    
with col2:
    st.metric(
        label="Columns",
        value=summary["columns"]
    )

with col3:
    st.metric(
        label="Missing Values",
        value=summary["missing_values"]
    )

with col4:
    st.metric(
        label="Duplicates",
        value=summary["duplicates"]
    )

with col5:
    st.metric(
        label="Memory (MB)",
        value=summary["memory_usage_mb"]
    )    
    
st.divider()

st.header("📋 Column Information")    
  
column_info = pd.DataFrame(
    {
        "Column Name":
            df.columns,

        "Data Type":
            df.dtypes.astype(str)
    }
)  

st.dataframe(
    column_info,
    use_container_width=True
)    