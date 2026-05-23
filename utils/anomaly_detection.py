import numpy as np

def detect_anomalies(df):

    revenue_mean = df["Revenue"].mean()

    revenue_std = df["Revenue"].std()

    anomalies = df[
        abs(df["Revenue"] - revenue_mean)
        > 2 * revenue_std
    ]

    return anomalies