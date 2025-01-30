#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:41:30 2024

@author: dawei
"""
# %%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Set API key and define the companies
api_key = 'xxx
companies = {
    'Starbuck': 'SBUX',
    'Procter&Gamble': 'PG',
    'JPMorrgan Chase': 'JPM',
    'Johnson&johnson': 'JNJ',
    'NVIDIA': 'NVDA',
'NextEra Energy': 'NEE',
    'Exxon': 'XOM',
    'Verizon': 'VZ'
}

# Function to fetch historical price data
def get_historical_data(symbol, api_key):
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?serietype=line&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if 'historical' in data:  #When you make a request to the API, it returns a JSON object (essentially a dictionary in Python). This object typically has various keys, one of which is 'historical'. This key contains all the historical price data you want.In this example, the key 'historical' holds a list of dictionaries, each representing a specific day's price data. 
        return pd.DataFrame(data['historical'])
    else:
        print(f"Error fetching data for {symbol}")
        return pd.DataFrame()

# Get historical data for all companies
price_data = {}
for company, ticker in companies.items():
    df = get_historical_data(ticker, api_key)
    if not df.empty:
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)
        price_data[company] = df['close']

# Create a DataFrame for the closing prices of all companies
prices_df = pd.DataFrame(price_data)

# Calculate daily returns
returns_df = prices_df.pct_change().dropna()

# Calculate mean returns and covariance matrix
mean_returns = returns_df.mean()
cov_matrix = returns_df.cov()
risk_free_rate = 0.02

# Set number of random portfolios to generate
num_portfolios = 1000

# Store portfolio metrics
results = np.zeros((num_portfolios, len(mean_returns) + 3))  # Columns: [Weights..., Return, Volatility, Sharpe Ratio]

# Generate random portfolios
for i in range(num_portfolios):
    # Generate random weights and normalize to sum to 1
    weights = np.random.random(len(mean_returns))
    weights /= np.sum(weights)

    # Calculate portfolio return and standard deviation
    portfolio_return = np.sum(mean_returns * weights) * 252
    portfolio_std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_std_dev

    # Store the results
    results[i, :len(mean_returns)] = weights
    results[i, -3] = portfolio_return
    results[i, -2] = portfolio_std_dev
    results[i, -1] = sharpe_ratio

# Find the portfolio with the maximum Sharpe ratio
max_sharpe_idx = np.argmax(results[:, -1])
optimal_weights = results[max_sharpe_idx, :len(mean_returns)]

# Calculate daily portfolio returns based on optimized weights
weighted_returns = returns_df.dot(optimal_weights)
cumulative_returns = (1 + weighted_returns).cumprod() - 1
initial_investment = 100000
portfolio_value = initial_investment * (1 + cumulative_returns)

# Print optimal weights and Sharpe ratio
print("Optimal Weights:", optimal_weights)
print("Expected Portfolio Return:", results[max_sharpe_idx, -3])
print("Expected Portfolio Volatility:", results[max_sharpe_idx, -2])
print("Max Sharpe Ratio:", results[max_sharpe_idx, -1])

# Plot cumulative portfolio performance (percentage returns)
plt.figure(figsize=(12, 8))
plt.plot(cumulative_returns, label='Portfolio Return (%)', color='blue')  
plt.title('Cumulative Portfolio Performance (Percentage Return)')
plt.xlabel('Date')
plt.ylabel('Portfolio Return (%)')
plt.legend()
plt.grid(True)
plt.show()
