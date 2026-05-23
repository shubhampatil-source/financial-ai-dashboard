from prophet import Prophet
import pandas as pd

def revenue_forecast(df):
    forecast_df = df[['Year', 'Revenue']]
    forecast_df.columns = ['ds', 'y']
    forecast_df['ds'] = pd.to_datetime(forecast_df['ds'],format='%Y')

    model = Prophet()
    model.fit(forecast_df)

    future = model.make_future_dataframe(periods=2,freq='Y')

    forecast = model.predict(future)
    return forecast