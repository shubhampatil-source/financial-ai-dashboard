def compare_companies(df1, df2):

    comparison = {
        "Revenue Difference":
        df1["Revenue"].sum() - df2["Revenue"].sum(),

        "Profit Difference":
        df1["Net_Profit"].sum() - df2["Net_Profit"].sum()
    }

    return comparison

