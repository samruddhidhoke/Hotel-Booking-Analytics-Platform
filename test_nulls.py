import pandas as pd

from utils.database import get_engine

engine = get_engine()

query = """
SELECT *
FROM hotel_bookings
"""

df = pd.read_sql(
    query,
    engine
)

# Print all column names
print(df.columns.tolist())

print("\nAGENT")
print(
    df["agent"]
    .value_counts(
        dropna=False
    )
    .head(10)
)

print("\nCOMPANY")
print(
    df["company"]
    .value_counts(
        dropna=False
    )
    .head(10)
)

print("\nCOUNTRY")
print(
    df["country"]
    .value_counts(
        dropna=False
    )
    .head(10)
)

print("\nCHILDREN")
print(
    df["children"]
    .value_counts(
        dropna=False
    )
    .head(10)
)