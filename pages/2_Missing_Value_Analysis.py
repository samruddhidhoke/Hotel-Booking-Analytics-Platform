import streamlit as st
import pandas as pd
import plotly.express as px

from utils.database import get_engine

from modules.data_preprocessing import (
    fix_data_types
)

from modules.missing_analysis import (
    missing_value_analysis
)

st.set_page_config(
    page_title="Missing Value Analysis",
    page_icon="⚠️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title(
    "⚠️ Missing Value Analysis"
)

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

missing_df = (
    missing_value_analysis(df)
)

total_missing = (
    missing_df[
        "Missing Count"
    ]
    .sum()
)

columns_with_missing = (
    len(missing_df)
)

m1, m2 = st.columns(2)

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

st.subheader(
    "Missing Value Summary"
)

st.dataframe(
    missing_df,
    width="stretch"
)

fig = px.bar(
    missing_df,
    x=missing_df.index,
    y="Missing Percentage",
    title="Missing Percentage by Column",
    text="Missing Percentage"
)

fig.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig,
    width="stretch"
)

st.subheader(
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