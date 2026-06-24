import streamlit as st
import pandas as pd

from utils.database import get_engine

from modules.data_preprocessing import (
    fix_data_types
)

from modules.missing_analysis import (
    missing_value_analysis
)

from modules.numerical_analysis import (
    numerical_summary
)

from modules.outlier_analysis import (
    outlier_summary
)

st.set_page_config(
    page_title="Download Reports",
    page_icon="📥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title(
    "📥 Download Reports"
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

numerical_df = (
    numerical_summary(df)
)

outlier_df = (
    outlier_summary(df)
)

missing_csv = (
    missing_df
    .to_csv()
)

numerical_csv = (
    numerical_df
    .to_csv()
)

outlier_csv = (
    outlier_df
    .to_csv()
)

d1, d2, d3 = st.columns(3)

with d1:

    st.download_button(
        label="Download Missing Report",
        data=missing_csv,
        file_name="missing_report.csv",
        mime="text/csv"
    )

with d2:

    st.download_button(
        label="Download Numerical Report",
        data=numerical_csv,
        file_name="numerical_report.csv",
        mime="text/csv"
    )

with d3:

    st.download_button(
        label="Download Outlier Report",
        data=outlier_csv,
        file_name="outlier_report.csv",
        mime="text/csv"
    )