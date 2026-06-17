import pandas as pd

from utils.database import get_engine
from modules.missing_analysis import (
    missing_value_analysis
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

missing_df = (
    missing_value_analysis(df)
)

print(missing_df)