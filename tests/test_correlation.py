import pandas as pd

from utils.database import get_engine

from modules.data_preprocessing import (
    fix_data_types
)

from modules.correlation_analysis import (
    correlation_matrix
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

corr = (
    correlation_matrix(df)
)

print(corr)
print(corr.shape)