"""
missing_analysis.py

Purpose:
Detect and summarize
missing values.
"""

import pandas as pd

def missing_value_analysis(df):
    """
    Returns missing value information.
    """
    df = df.replace(
    [
        '',
        'NULL',
        'NA',
        'null',
        'nan'
    ],
    pd.NA
    )
    
    missing_count = (       # Calculate Missing Values
    df.isnull()
      .sum()
    )
    missing_percent = (     #Missing Percentage
    missing_count
    / len(df)
    ) * 100
 
    missing_df = pd.DataFrame(           #Create Summary Table
    {
        "Missing Count":
            missing_count,

        "Missing Percentage":
            missing_percent.round(2)
    }
    )   
    
    missing_df = (                  #Remove Non-Missing Columns
    missing_df[
        missing_df[
            "Missing Count"
        ] > 0
    ]
    ) 
    
    missing_df = (                   # Sort Table
    missing_df
    .sort_values(
        by="Missing Count",
        ascending=False
    )
    )
    
    return missing_df