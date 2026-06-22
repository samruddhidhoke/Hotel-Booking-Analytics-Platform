def generate_insights(
    summary,
    missing_df,
    outlier_df,
    quality_score
):

    insights = []

    insights.append(
        f"Dataset contains "
        f"{summary['rows']:,} rows "
        f"and {summary['columns']} columns."
    )

    insights.append(
        f"Dataset contains "
        f"{summary['duplicates']:,} duplicate rows."
    )

    if not missing_df.empty:

        highest_missing = (
            missing_df[
                "Missing Percentage"
            ]
            .idxmax()
        )

        highest_percent = (
            missing_df.loc[
                highest_missing,
                "Missing Percentage"
            ]
        )

        insights.append(
            f"{highest_missing} has "
            f"{highest_percent}% missing values."
        )

    outlier_columns = int(
        (
            outlier_df[
                "Outlier Count"
            ]
            > 0
        ).sum()
    )

    insights.append(
        f"{outlier_columns} columns "
        f"contain outliers."
    )

    insights.append(
        f"Overall data quality score "
        f"is {round(quality_score, 2)}%."
    )

    return insights