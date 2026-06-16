"""
summary.py

Purpose:
Generate dataset overview.
"""


def dataset_summary(df):
    """
    Returns dataset summary.
    """

    summary = {
        "rows":
            int(df.shape[0]),

        "columns":
            int(df.shape[1]),

        "missing_values":
            int(
                df.isnull()
                  .sum()
                  .sum()
            ),

        "duplicates":
            int(
                df.duplicated()
                  .sum()
            ),

        "memory_usage_mb":
            float(
                round(
                    df.memory_usage(
                        deep=True
                    ).sum()
                    / 1024**2,
                    2
                )
            )
    }

    return summary