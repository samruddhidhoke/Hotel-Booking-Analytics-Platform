import pandas as pd

from utils.database import get_engine

from modules.data_preprocessing import (
    fix_data_types
)

from modules.numerical_analysis import (
    numerical_summary
)

# Create SQL Server connection
engine = get_engine()

# Query dataset
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

# Generate numerical summary
summary = numerical_summary(df)

# Print result
print(summary)

