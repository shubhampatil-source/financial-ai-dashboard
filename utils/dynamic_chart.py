import plotly.express as px

def dynamic_metric_chart(df, metric):

    fig = px.line(
        df,
        x="Year",
        y=metric,
        title=f"{metric} Trend"
    )

    return fig