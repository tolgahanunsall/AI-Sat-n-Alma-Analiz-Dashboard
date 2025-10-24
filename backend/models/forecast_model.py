from prophet import Prophet
import pandas as pd


def forecast_purchases(df: pd.DataFrame, months_ahead: int = 6):
    # Aggregate by year and month
    required = {'YIL', 'AY', 'Tutar'}
    if not required.issubset(set(df.columns)):
        raise ValueError("DataFrame must contain YIL, AY, Tutar columns")

    agg = df.groupby(['YIL', 'AY'])['Tutar'].sum().reset_index()
    agg['ds'] = pd.to_datetime(agg['YIL'].astype(str) + '-' + agg['AY'].astype(str) + '-01')
    agg = agg.rename(columns={'Tutar': 'y'})

    # Ensure sorted and no NA
    agg = agg[['ds', 'y']].dropna().sort_values('ds')

    model = Prophet()
    model.fit(agg)
    future = model.make_future_dataframe(periods=months_ahead, freq='M')
    forecast = model.predict(future)
    result = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(months_ahead)
    return result
