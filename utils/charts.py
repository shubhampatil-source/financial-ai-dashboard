import plotly.express as px


def revenue_chart(df):

    # ---------------------------
    # CLEAN YEAR
    # ---------------------------

    df = df.copy()

    df["Year"] = (
        df["Year"]
        .astype(int)
    )

    # ---------------------------
    # CHART
    # ---------------------------

    fig = px.line(
        df,
        x="Year",
        y="Revenue",
        markers=True
    )

    # ---------------------------
    # FIX AXIS TICKS
    # ---------------------------

    fig.update_xaxes(

        tickmode="array",

        tickvals=df["Year"],

        ticktext=df["Year"].astype(str)
    )

    return fig


import plotly.express as px


def profit_chart(df):

    df = df.copy()

    df["Year"] = (
        df["Year"]
        .astype(int)
    )

    fig = px.line(
        df,
        x="Year",
        y="Net_Profit",
        markers=True
    )

    fig.update_xaxes(

        tickmode="array",

        tickvals=df["Year"],

        ticktext=df["Year"].astype(str)
    )

    return fig