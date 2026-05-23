def calculate_kpis(df):

    # SINGLE ROW CASE
    if len(df) < 2:

        revenue_growth = 0

        profit_margin = (
            df.iloc[0]['Net_Profit']
            /
            df.iloc[0]['Revenue']
        ) * 100

        current_ratio = (
            df.iloc[0]['Assets']
            /
            df.iloc[0]['Liabilities']
        )

    # MULTI-ROW CASE
    else:

        revenue_growth = (
            (
                df.iloc[-1]['Revenue']
                -
                df.iloc[-2]['Revenue']
            )
            /
            df.iloc[-2]['Revenue']
        ) * 100

        profit_margin = (
            df.iloc[-1]['Net_Profit']
            /
            df.iloc[-1]['Revenue']
        ) * 100

        current_ratio = (
            df.iloc[-1]['Assets']
            /
            df.iloc[-1]['Liabilities']
        )

    return {

        "Revenue Growth %":
        round(revenue_growth, 2),

        "Profit Margin %":
        round(profit_margin, 2),

        "Current Ratio":
        round(current_ratio, 2)
    }