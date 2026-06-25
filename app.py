import streamlit as st
import pandas as pd

from modules.data_loader import (
    load_data
)

from modules.summary import dataset_summary

from modules.outlier_analysis import (
    outlier_summary
)

from modules.data_preprocessing import (
    fix_data_types
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
    "🏨 Hotel Booking Analytics Platform"
)

st.caption(
    "Built with Python • SQL Server • Pandas • Streamlit • Plotly"
)

st.markdown(
    """
    ### Transforming Hotel Booking Data into Actionable Business Intelligence

    An enterprise-style analytics platform that combines
    SQL Server, Python, and Streamlit to automate data profiling,
    quality assessment, exploratory analysis, and business insight generation.

    Designed to help analysts identify data quality issues,
    uncover booking trends, detect anomalies, and generate
    data-driven recommendations through an interactive dashboard.
    """
)

df = load_data()

df = fix_data_types(df)

# Generate dataset summary
summary = dataset_summary(df)

missing_df = (
    missing_value_analysis(df)
)

total_missing = (
    missing_df[
        "Missing Count"
    ]
    .sum()
)

outlier_df = (
    outlier_summary(df)
)


# Display summary dictionary temporarily
#st.write(summary)



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
    "🚀 Platform Capabilities"
)

c1, c2 = st.columns(2)

with c1:

    st.success(
        """
        📊 Automated Data Profiling

        Dataset overview,
        schema inspection,
        and data quality assessment.
        """
    )

    st.success(
        """
        📈 Exploratory Data Analysis

        Numerical,
        categorical,
        and distribution analysis.
        """
    )

with c2:

    st.success(
        """
        📉 Correlation & Outlier Detection

        Identify hidden relationships
        and anomalous records.
        """
    )

    st.success(
        """
        🧠 Insight Generation & Reporting

        Automated business insights
        and downloadable reports.
        """
    )

st.divider()

st.header(
    "📊 Dataset Snapshot"
)    

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Bookings",
        f"{summary['rows']:,}"
    )

with k2:
    st.metric(
        "Features",
        summary["columns"]
    )

with k3:
    st.metric(
        "Duplicate Records",
        f"{summary['duplicates']:,}"
    )

with k4:
    st.metric(
        "Quality Score",
        round(
            quality_score,
            2
        )
    )
    
st.info(
    f"""
    The platform analyzes {summary['rows']:,} hotel booking records across
    {summary['columns']} business and operational attributes,
    providing automated profiling, quality assessment,
    exploratory analysis, and business intelligence reporting.
    """
)

st.divider()

st.header(
    "🧭 Analysis Modules"
)

m1, m2, m3 = st.columns(3)

with m1:

    st.info(
        """
        📊 Dataset Overview

        Dataset structure,
        schema and profiling.
        """
    )

    st.info(
        """
        🔢 Numerical Analysis

        Statistical analysis
        of numerical features.
        """
    )

    st.info(
        """
        📈 Distribution Analysis

        Histograms and
        distribution insights.
        """
    )

with m2:

    st.info(
        """
        ⚠️ Missing Value Analysis

        Missing data detection
        and recommendations.
        """
    )

    st.info(
        """
        🔤 Categorical Analysis

        Category distributions
        and frequency analysis.
        """
    )

    st.info(
        """
        📉 Correlation Analysis

        Feature relationships
        and heatmaps.
        """
    )

with m3:

    st.info(
        """
        📦 Outlier Analysis

        Outlier detection
        using IQR methodology.
        """
    )

    st.info(
        """
        🧠 Business Insights

        Automated insight
        generation engine.
        """
    )

    st.info(
        """
        📥 Download Reports

        Export analytical
        reports as CSV files.
        """
    )
    
    