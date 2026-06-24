import streamlit as st
import pandas as pd
import plotly.express as px

from utils.database import get_engine

from modules.data_preprocessing import (
    fix_data_types
)

from modules.correlation_analysis import (
    correlation_matrix
)

st.set_page_config(
    page_title="Correlation Analysis",
    page_icon="📉",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title(
    "📉 Correlation Analysis"
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

corr_df = (
    correlation_matrix(df)
)

st.dataframe(
    corr_df,
    width="stretch"
)

fig = px.imshow(
    corr_df,
    text_auto=True,
    aspect="auto",
    title="Correlation Heatmap"
)

st.plotly_chart(
    fig,
    width="stretch"
)

st.subheader(
    "Strong Correlations"
)

corr_long = (
    corr_df
    .stack()
    .reset_index()
)

corr_long.columns = [
    "Feature 1",
    "Feature 2",
    "Correlation"
]

corr_long = (
    corr_long[
        corr_long[
            "Feature 1"
        ]
        !=
        corr_long[
            "Feature 2"
        ]
    ]
)

corr_long["Pair"] = (
    corr_long[
        ["Feature 1", "Feature 2"]
    ]
    .apply(
        lambda x:
        "_".join(
            sorted(x)
        ),
        axis=1
    )
)

corr_long = (
    corr_long
    .drop_duplicates(
        subset="Pair"
    )
)

top_corr = (
    corr_long
    .reindex(
        corr_long[
            "Correlation"
        ]
        .abs()
        .sort_values(
            ascending=False
        )
        .index
    )
    .head(10)
)

st.dataframe(
    top_corr[
        [
            "Feature 1",
            "Feature 2",
            "Correlation"
        ]
    ],
    width="stretch"
)

st.subheader(
    "Correlation Insights"
)

st.info(
    """
    • Positive correlations indicate variables moving together.

    • Negative correlations indicate inverse relationships.

    • Weak correlations suggest independent behaviour.

    • Correlation does not imply causation.
    """
)