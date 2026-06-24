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
    page_title="Distribution Analysis",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title(
    "📈 Distribution Analysis"
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

selected_column = st.selectbox(
    "Select Numerical Feature",
    numerical_df.index
)

fig = px.histogram(
    df,
    x=selected_column,
    title=f"Distribution of {selected_column}",
    nbins=30
)

st.plotly_chart(
    fig,
    width="stretch"
)

st.subheader(
    "Selected Feature Statistics"
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Mean",
        round(
            df[selected_column].mean(),
            2
        )
    )

with c2:
    st.metric(
        "Median",
        round(
            df[selected_column].median(),
            2
        )
    )

with c3:
    st.metric(
        "Minimum",
        round(
            df[selected_column].min(),
            2
        )
    )

with c4:
    st.metric(
        "Maximum",
        round(
            df[selected_column].max(),
            2
        )
    )

st.subheader(
    "Distribution Insights"
)

mean_value = (
    df[selected_column]
    .mean()
)

median_value = (
    df[selected_column]
    .median()
)

if mean_value > median_value:

    st.info(
        "Distribution appears right-skewed."
    )

elif mean_value < median_value:

    st.info(
        "Distribution appears left-skewed."
    )

else:

    st.info(
        "Distribution appears approximately symmetric."
    )