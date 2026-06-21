def correlation_matrix(df):

    numerical_df = (
        df.select_dtypes(
            include=[
                "int64",
                "float64"
            ]
        )
    )

    correlation_df = (
        numerical_df
        .corr()
        .round(2)
    )

    return correlation_df