import pandas as pd
import streamlit as st


# -----------------------------------
# SAFE NUMBER CONVERSION
# -----------------------------------

def safe_number(value):

    try:

        if pd.isna(value):

            return 0

        return float(value)

    except:

        return 0


# -----------------------------------
# REVENUE GROWTH %
# -----------------------------------

def calculate_revenue_growth(df):

    if df is None or df.empty:

        return 0

    if "Revenue" not in df.columns:

        return 0

    if "Year" not in df.columns:

        return 0

    # SORT YEAR
    df = df.sort_values("Year")

    # NEED 2 YEARS
    if len(df) < 2:

        return 0

    previous_revenue = safe_number(
        df.iloc[-2]["Revenue"]
    )

    current_revenue = safe_number(
        df.iloc[-1]["Revenue"]
    )

    if previous_revenue == 0:

        return 0

    growth = (
        (
            current_revenue
            - previous_revenue
        )
        / previous_revenue
    ) * 100

    return round(growth, 2)


# -----------------------------------
# PROFIT MARGIN %
# -----------------------------------

def calculate_profit_margin(df):

    if df is None or df.empty:

        return 0

    if "Revenue" not in df.columns:

        return 0

    if "Net_Profit" not in df.columns:

        return 0

    # SORT YEAR
    if "Year" in df.columns:

        df = df.sort_values("Year")

    latest_row = df.iloc[-1]

    revenue = safe_number(
        latest_row["Revenue"]
    )

    net_profit = safe_number(
        latest_row["Net_Profit"]
    )

    if revenue == 0:

        return 0

    margin = (
        net_profit / revenue
    ) * 100

    return round(margin, 2)


# -----------------------------------
# CURRENT RATIO
# -----------------------------------

def calculate_current_ratio(df):

    if df is None or df.empty:

        return 0

    if "Assets" not in df.columns:

        return 0

    if "Liabilities" not in df.columns:

        return 0

    # SORT YEAR
    if "Year" in df.columns:

        df = df.sort_values("Year")

    latest_row = df.iloc[-1]

    assets = safe_number(
        latest_row["Assets"]
    )

    liabilities = safe_number(
        latest_row["Liabilities"]
    )

    if liabilities == 0:

        return 0

    ratio = assets / liabilities

    return round(ratio, 2)


# -----------------------------------
# MASTER KPI FUNCTION
# -----------------------------------

def calculate_kpis(df):

    st.success("PDF processed successfully")

    revenue_growth = calculate_revenue_growth(df)

    profit_margin = calculate_profit_margin(df)

    current_ratio = calculate_current_ratio(df)

    kpis = {

        "Revenue Growth %": revenue_growth,

        "Profit Margin %": profit_margin,

        "Current Ratio": current_ratio
    }

    st.write("KPI OUTPUT")
    st.write(kpis)

    return kpis
