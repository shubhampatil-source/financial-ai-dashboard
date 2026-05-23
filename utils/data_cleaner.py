import pandas as pd

def clean_financial_data(df):

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna(0)

    # Convert numeric columns
    numeric_cols = [
        "Revenue",
        "Expenses",
        "Net_Profit",
        "Assets",
        "Liabilities"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(
            df[col],
            errors='coerce'
        )

    return df