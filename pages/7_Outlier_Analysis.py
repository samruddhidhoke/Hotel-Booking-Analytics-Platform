import streamlit as st
import pandas as pd
import plotly.express as px

from modules.data_loader import (
    load_data
)

from modules.data_preprocessing import (
    fix_data_types
)

from modules.outlier_analysis import (
    outlier_summary
)

st.set_page_config(
    page_title="Outlier Analysis",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title(
    "📦 Outlier Analysis"
)

df = load_data()

df = fix_data_types(df)

outlier_df = (
    outlier_summary(df)
)

st.dataframe(
    outlier_df,
    width="stretch"
)

st.subheader(
    "Outlier Metrics"
)

o1, o2 = st.columns(2)

with o1:

    st.metric(
        "Columns With Outliers",
        int(
            (
                outlier_df[
                    "Outlier Count"
                ]
                > 0
            ).sum()
        )
    )

with o2:

    st.metric(
        "Total Outliers",
        int(
            outlier_df[
                "Outlier Count"
            ]
            .sum()
        )
    )

fig = px.bar(
    outlier_df,
    x="Column",
    y="Outlier Percentage",
    title="Outlier Percentage by Feature"
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
    • High outlier percentages require business investigation.

    • Not all outliers should be removed automatically.

    • Outliers may indicate rare but valid business scenarios.

    • Outlier treatment decisions should depend on domain knowledge.
    """
)