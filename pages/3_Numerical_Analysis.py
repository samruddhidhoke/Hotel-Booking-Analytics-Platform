import streamlit as st
import pandas as pd
import plotly.express as px

from utils.database import get_engine

from modules.data_preprocessing import (
    fix_data_types
)

from modules.numerical_analysis import (
    numerical_summary
)

st.set_page_config(
    page_title="Numerical Analysis",
    page_icon="🔢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title(
    "🔢 Numerical Features Analysis"
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

numerical_df = (
    numerical_summary(df)
)

st.dataframe(
    numerical_df,
    width="stretch"
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
    width="stretch"
)