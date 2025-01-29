# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:07:48 2024

@author: Armanis
"""

#pip install darts

import pandas_datareader as pdr
from darts import TimeSeries
from darts.models import ExponentialSmoothing, AutoARIMA, Prophet
import matplotlib.pyplot as plt

# Load and preprocess data for WTI Crude Oil Prices
df = pdr.DataReader('PCOPPUSDM', 'fred', start='2005-01-01').dropna()
df = df.resample('ME').last()  # Monthly frequency

# Convert to Darts TimeSeries
series = TimeSeries.from_dataframe(df, value_cols='PCOPPUSDM', freq='M')

# Train-test split
train, val = series.split_before(0.9)

# Initialize models
arima_model = AutoARIMA()  
ets_model = ExponentialSmoothing()  
prophet_model = Prophet()  

# Fit models
arima_model.fit(train)
ets_model.fit(train)
prophet_model.fit(train)

# Forecast horizon
forecast_horizon = len(val)

# Predict with each model
arima_forecast = arima_model.predict(forecast_horizon)
ets_forecast = ets_model.predict(forecast_horizon)
prophet_forecast = prophet_model.predict(forecast_horizon)

# Plot the results
plt.figure(figsize=(10, 6))
train.plot(label='Train')
val.plot(label='Actual (Validation)', lw=2)
arima_forecast.plot(label='ARIMA Forecast', lw=2)
ets_forecast.plot(label='ETS Forecast', lw=2)
prophet_forecast.plot(label='Prophet Forecast', lw=2)
plt.title('Model Comparison: ARIMA, ETS, Prophet for WTI Crude Oil Prices')
plt.legend()
plt.show()


#%%
# Calculate performance metrics
from darts.metrics import mae, rmse

print("MAE - ARIMA:", mae(val, arima_forecast))
print("MAE - ETS:", mae(val, ets_forecast))
print("MAE - Prophet:", mae(val, prophet_forecast))

print("RMSE - ARIMA:", rmse(val, arima_forecast))
print("RMSE - ETS:", rmse(val, ets_forecast))
print("RMSE - Prophet:", rmse(val, prophet_forecast))

#%%
# Refit models on full data and predict future values
arima_model.fit(series)
ets_model.fit(series)
prophet_model.fit(series)

forecast_horizon_future = 24  # 24 periods into the future

arima_future_forecast = arima_model.predict(forecast_horizon_future)
ets_future_forecast = ets_model.predict(forecast_horizon_future)
prophet_future_forecast = prophet_model.predict(forecast_horizon_future)



# Plot future forecasts
plt.figure(figsize=(10, 6))
series.plot(label='Full Sample')

arima_future_forecast.plot(label='ARIMA Future Forecast', lw=2)
ets_future_forecast.plot(label='ETS Future Forecast', lw=2)
prophet_future_forecast.plot(label='Prophet Future Forecast', lw=2)

plt.title('Future Forecast: ARIMA, ETS, Prophet (Next 24 Months)')
plt.legend()
plt.show()
