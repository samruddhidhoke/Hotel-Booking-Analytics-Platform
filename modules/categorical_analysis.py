import pandas as pd


def categorical_summary(df):

    categorical_columns = (
        df.select_dtypes(
            include=["object"]
        )
        .columns
    )

    summary_list = []

    for column in categorical_columns:

        summary_list.append(
            {
                "Column":
                    column,

                "Unique Values":
                    df[column]
                    .nunique(),

                "Most Frequent":
                    df[column]
                    .mode()[0],

                "Frequency":
                    df[column]
                    .value_counts()
                    .iloc[0]
            }
        )

    summary = pd.DataFrame(
        summary_list
    )

    return summary