import streamlit as st
import pandas as pd

from utils.database import get_engine

from modules.summary import (
    dataset_summary
)

from modules.data_preprocessing import (
    fix_data_types
)

st.set_page_config(
    page_title="Dataset Overview",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title(
    "📊 Dataset Overview"
)

# Database Connection
engine = get_engine()

query = """
SELECT *
FROM hotel_bookings
"""

df = pd.read_sql(
    query,
    engine
)

df = fix_data_types(df)

summary = dataset_summary(df)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Rows",
        summary["rows"]
    )

with col2:
    st.metric(
        "Columns",
        summary["columns"]
    )

with col3:
    st.metric(
        "Missing Values",
        summary["missing_values"]
    )

with col4:
    st.metric(
        "Duplicates",
        summary["duplicates"]
    )

with col5:
    st.metric(
        "Memory (MB)",
        summary["memory_usage_mb"]
    )

st.divider()

st.subheader(
    "Column Information"
)

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
    width="stretch"
)