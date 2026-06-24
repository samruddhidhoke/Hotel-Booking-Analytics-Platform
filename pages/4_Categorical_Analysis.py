import streamlit as st
import pandas as pd
import plotly.express as px

from utils.database import get_engine

from modules.data_preprocessing import (
    fix_data_types
)

from modules.categorical_analysis import (
    categorical_summary
)

st.set_page_config(
    page_title="Categorical Analysis",
    page_icon="🔤",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title(
    "🔤 Categorical Features Analysis"
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

categorical_df = (
    categorical_summary(df)
)

st.dataframe(
    categorical_df,
    width="stretch"
)

st.subheader(
    "Categorical Dataset Metrics"
)

c1, c2 = st.columns(2)

with c1:

    st.metric(
        "Categorical Features",
        len(categorical_df)
    )

with c2:

    st.metric(
        "Total Unique Categories",
        int(
            categorical_df[
                "Unique Values"
            ]
            .sum()
        )
    )

st.subheader(
    "Unique Values Across Features"
)

fig = px.bar(
    categorical_df,
    x="Column",
    y="Unique Values",
    title="Unique Categories Across Features"
)

st.plotly_chart(
    fig,
    width="stretch"
)