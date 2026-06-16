"""
test_connection.py

Purpose:
Test Python ↔ SQL Server connection.
"""

import pandas as pd
from utils.database import get_engine


# Create engine
engine = get_engine()

# SQL query
query = """
SELECT TOP 5 *
FROM hotel_bookings;
"""

# Execute query
df = pd.read_sql(
    query,
    engine
)

# Print results
print(df.head())