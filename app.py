import streamlit as st
import pandas as pd
import plotly.express as px


from utils.database import get_engine
from modules.summary import dataset_summary

from modules.data_preprocessing import (
    fix_data_types
)

from modules.numerical_analysis import (
    numerical_summary
)

from modules.missing_analysis import (
    missing_value_analysis
)


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

df = fix_data_types(df)

# Generate dataset summary
summary = dataset_summary(df)

missing_df = (
    missing_value_analysis(df)
)

numerical_df = (
    numerical_summary(df)
)

# Display summary dictionary temporarily
#st.write(summary)

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

st.divider()

st.header("⚠️ Missing Value Analysis")

total_missing = (               # Create Missing Value Metrics
    missing_df[
        "Missing Count"
    ]
    .sum()
)

columns_with_missing = (
    len(missing_df)
)

m1, m2 = st.columns(2)          #Create Metric Cards

with m1:
    st.metric(
        "Total Missing Values",
        int(total_missing)
    )

with m2:
    st.metric(
        "Columns With Missing Values",
        columns_with_missing
    )
  
st.subheader(                       # Display Missing Value Table
    "Missing Value Summary"
)

st.dataframe(
    missing_df,
    use_container_width=True
)    

fig = px.bar(                   # Build Chart
    missing_df,
    x=missing_df.index,
    y="Missing Count",
    title="Missing Values by Column"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader(                   # Recommendations Section
    "Recommendations"
)

st.info(
    """
    • company has more than 90% missing values and may be removed.

    • agent contains moderate missing values and requires business investigation.

    • country has very few missing values and can be imputed.

    • children has negligible missing values.
    """
)

st.divider()

st.header("🛡️ Data Quality Score")

total_cells = (                 # Calculate Completeness
    df.shape[0]
    * df.shape[1]
)

completeness = (
    (
        total_cells
        - total_missing
    )
    / total_cells
) * 100

duplicate_rate = (                      # Duplicate Rate
    summary["duplicates"]
    / summary["rows"]
) * 100

quality_score = (                       # Overall Quality Score 
    completeness
    +
    (
        100
        - duplicate_rate
    )
) / 2

q1, q2, q3 = st.columns(3)              # Create Metric Cards

with q1:                                # Card 1
    st.metric(
        "Completeness %",
        round(
            completeness,
            2
        )
    )
    
with q2:                                   #  # Card 2
    st.metric(
        "Duplicate Rate %",
        round(
            duplicate_rate,
            2
        )
    )    
    
with q3:                                # Card 3
    st.metric(
        "Overall Quality Score",
        round(
            quality_score,
            2
        )
    )    
    
st.divider()

st.header(
    "🔢 Numerical Features Analysis"
)
  
st.dataframe(
    numerical_df,
    use_container_width=True
)    

st.subheader(
    "Numerical Dataset Metrics"
)

n1, n2 = st.columns(2)

with n1:
    st.metric(
        "Numerical Features",
        len(numerical_df)
    )

with n2:
    st.metric(
        "Total Numerical Cells",
        int(
            df[
                numerical_df.index
            ]
            .count()
            .sum()
        )
    )
    
st.subheader(
    "Average Values of Numerical Features"
)

fig = px.bar(
    numerical_df,
    x=numerical_df.index,
    y="mean",
    title="Mean of Numerical Features"
)

st.plotly_chart(
    fig,
    use_container_width=True
)    