# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 13:30:00 2024

@author: Armanis
"""



#%% Step 1: Import Required Libraries
import pandas as pd
import statsmodels.api as sm
import plotly.express as px
import yfinance as yf
from pandas_datareader import data as pdr

#%% Step 2: Retrieve and Preprocess Fama-French Three-Factor Data
ff_data_3f = pdr.get_data_famafrench(
    'F-F_Research_Data_Factors',
    start='2010',
    end='2020'
)[0]

# Quick look at the first few rows of the data
print("Fama-French 3-Factor Data (First Few Rows):\n", ff_data_3f.head())

# Convert the date index for easier handling
ff_data_3f.reset_index(inplace=True)
ff_data_3f['Date'] = pd.to_datetime(ff_data_3f['Date'].astype(str) + '-01')
ff_data_3f.set_index('Date', inplace=True)

#%% Step 3: Inspect Factor Behavior Over Time
# Minimal line plot for each Fama-French factor
fig_factors_over_time = px.line(
    ff_data_3f,
    x=ff_data_3f.index,
    y=['Mkt-RF', 'SMB', 'HML'],
    template="plotly_dark"
)
fig_factors_over_time.show(renderer="browser")

#%% Step 4: Retrieve Stock Data and Calculate Monthly Returns
stock_data = yf.download(
    'AAPL',
    start='2010-01-01',
    end='2020-01-01',
    interval='1mo'
)['Adj Close']
print("Apple Stock Data (First Few Rows):\n", stock_data.head())

# Calculate monthly returns
stock_returns = stock_data.pct_change().dropna() * 100
print("Monthly Returns (First Few Rows):\n", stock_returns.head())

#%% Step 5: Align Fama-French Data with Stock Returns
ff_data_3f_aligned, stock_returns_aligned = ff_data_3f.align(
    stock_returns,
    join='inner',
    axis=0
)
excess_returns = stock_returns_aligned - ff_data_3f_aligned['RF']
print("Aligned Fama-French Data (First Few Rows):\n", ff_data_3f_aligned.head())
print("Aligned Stock Returns (First Few Rows):\n", stock_returns_aligned.head())
print("Excess Returns (First Few Rows):\n", excess_returns.head())

#%% Step 6: Set Up Regression Model Fits an Ordinary Least Squares (OLS) regression model to predict Apple’s excess returns using Mkt-RF, SMB, and HML as predictors.
X_3f = sm.add_constant(
    ff_data_3f_aligned[['Mkt-RF', 'SMB', 'HML']]
)
model_3f = sm.OLS(
    excess_returns,
    X_3f
).fit()
print(model_3f.summary())

#%% Step 7: Visualize Factor Contributions to Excess Returns
# Market-Risk Premium (Mkt-RF) vs. Excess Returns
fig_mkt = px.scatter(
    x=ff_data_3f_aligned['Mkt-RF'],
    y=excess_returns,
    trendline="ols",
    template="plotly_dark"
)
fig_mkt.show(renderer="browser")

# Size Premium (SMB) vs. Excess Returns
fig_smb = px.scatter(
    x=ff_data_3f_aligned['SMB'],
    y=excess_returns,
    trendline="ols",
    template="plotly_dark"
)
fig_smb.show(renderer="browser")

# Value Premium (HML) vs. Excess Returns
fig_hml = px.scatter(
    x=ff_data_3f_aligned['HML'],
    y=excess_returns,
    trendline="ols",
    template="plotly_dark"
)
fig_hml.show(renderer="browser")

#%% Step 8: Coefficients for Factor Contributions
summary_df = pd.DataFrame({
    "Coefficient": model_3f.params,
    "p-Value": model_3f.pvalues
})
fig_summary = px.bar(
    summary_df,
    x=summary_df.index,
    y="Coefficient",
    color="p-Value",
    color_continuous_scale="bluered"
    
    
)
fig_summary.show(renderer="browser")




