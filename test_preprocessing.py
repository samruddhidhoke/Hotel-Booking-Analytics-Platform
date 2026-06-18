import pandas as pd

from utils.database import get_engine
from modules.data_preprocessing import (
    fix_data_types
)

# Create database connection
engine = get_engine()

# SQL query
query = """
SELECT *
FROM hotel_bookings
"""

# Load data
df = pd.read_sql(
    query,
    engine
)

# Fix datatypes
df = fix_data_types(df)

# Print datatypes
print(df.dtypes)