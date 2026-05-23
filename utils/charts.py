import plotly.express as px

def revenue_chart(df):

    fig = px.line(
        df,
        x="Year",
        y="Revenue",
        title="Revenue Trend"
    )

    return fig


def profit_chart(df):

    fig = px.bar(
        df,
        x="Year",
        y="Net_Profit",
        title="Net Profit Trend"
    )

    return fig