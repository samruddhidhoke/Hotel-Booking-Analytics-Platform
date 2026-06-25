import streamlit as st
import pandas as pd

from modules.data_loader import (
    load_data
)

from modules.summary import (
    dataset_summary
)

from modules.data_preprocessing import (
    fix_data_types
)

from modules.missing_analysis import (
    missing_value_analysis
)

from modules.outlier_analysis import (
    outlier_summary
)

from modules.insight_engine import (
    generate_insights
)

st.set_page_config(
    page_title="Business Insights",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title(
    "🧠 Automated Business Insights"
)

df = load_data()

df = fix_data_types(df)

summary = dataset_summary(df)

missing_df = (
    missing_value_analysis(df)
)

outlier_df = (
    outlier_summary(df)
)

total_missing = (
    missing_df["Missing Count"]
    .sum()
)

total_cells = (
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

duplicate_rate = (
    summary["duplicates"]
    / summary["rows"]
) * 100

quality_score = (
    completeness
    +
    (
        100
        - duplicate_rate
    )
) / 2

insights = (
    generate_insights(
        summary,
        missing_df,
        outlier_df,
        quality_score
    )
)

for item in insights:
    st.success(item)