import pandas as pd


def numerical_summary(df):

    numerical_columns = (
        df.select_dtypes(
            include=[
                "int64",
                "float64"
            ]
        )
    )

    summary = (
        numerical_columns
        .describe()
        .T
        .round(2)
    )

    return summary