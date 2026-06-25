import pandas as pd

from utils.database import get_engine
from modules.summary import dataset_summary


# Create SQL Server connection
engine = get_engine()

# Query entire dataset
query = """
SELECT *
FROM hotel_bookings
"""

# Load SQL data into DataFrame
df = pd.read_sql(
    query,
    engine
)

# Generate summary
summary = dataset_summary(df)

# Print summary
print(summary)