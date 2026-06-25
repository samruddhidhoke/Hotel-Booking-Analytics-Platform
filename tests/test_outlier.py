import pandas as pd

from utils.database import get_engine

from modules.data_preprocessing import (
    fix_data_types
)

from modules.outlier_analysis import (
    outlier_summary
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

summary = (
    outlier_summary(df)
)

print(summary)