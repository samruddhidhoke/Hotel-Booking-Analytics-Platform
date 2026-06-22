import pandas as pd


def outlier_summary(df):

    numerical_columns = (
        df.select_dtypes(
            include=[
                "int64",
                "float64"
            ]
        )
        .columns
    )

    summary_list = []

    for column in numerical_columns:

        Q1 = (
            df[column]
            .quantile(0.25)
        )

        Q3 = (
            df[column]
            .quantile(0.75)
        )

        IQR = (
            Q3 - Q1
        )

        lower_bound = (
            Q1
            - 1.5 * IQR
        )

        upper_bound = (
            Q3
            + 1.5 * IQR
        )

        outliers = (
            (
                df[column]
                < lower_bound
            )
            |
            (
                df[column]
                > upper_bound
            )
        )

        outlier_count = (
            outliers
            .sum()
        )

        summary_list.append(
            {
                "Column":
                    column,

                "Outlier Count":
                    int(
                        outlier_count
                    ),

                "Outlier Percentage":
                    round(
                        (
                            outlier_count
                            / len(df)
                        )
                        * 100,
                        2
                    )
            }
        )

    summary = pd.DataFrame(
        summary_list
    )

    return summary