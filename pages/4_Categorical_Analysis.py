import streamlit as st
import pandas as pd
import plotly.express as px

from modules.data_loader import (
    load_data
)

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

df = load_data()

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