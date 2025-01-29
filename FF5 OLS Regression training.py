# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:25:04 2024

@author: Armanis
"""


import pandas as pd
import statsmodels.api as sm
import plotly.express as px
import yfinance as yf
from pandas_datareader import data as pdr

#%%
#Retreive FF5 Data
ff_data_5f = pdr.get_data_famafrench(
    'F-F_Research_Data_5_Factors_2x3',
    start = '2010',
    end = '2020')[0]

print(ff_data_5f.head())
#%%
#Retreive Momentum Factor Data
ff_data_mom = pdr.get_data_famafrench(
    'F-F_Momentum_Factor',
    start = '2010',
    end = '2020')[0]

#is used to remove any leading or trailing whitespace characters (such as spaces) from the column names of the ff_data_mom DataFrame.
ff_data_mom.columns = ff_data_mom.columns.str.strip()

print(ff_data_mom.head())
#%%
#Join Both together
ff_data_5f_mom = ff_data_5f.join(ff_data_mom,
                                 how = 'inner')
#Match DataFrame
ff_data_5f_mom.reset_index(inplace = True)
ff_data_5f_mom['Date'] = pd.to_datetime(ff_data_5f_mom['Date'].astype(str)+ '-01')
ff_data_5f_mom.set_index('Date', inplace = True)

print(ff_data_5f_mom.head())

#%%
#Transform Data for Plotting
ff_data_5f_mom_long = ff_data_5f_mom.reset_index().melt(
    id_vars = "Date",
    value_vars = ['Mkt-RF', 'SMB', 'HML', 'RMW', 'CMA', 'Mom'],
    var_name = "Factor",
    value_name = "Value"
    )
#Plot Over Time
fig_factors_over_time = px.line(
    ff_data_5f_mom_long,
    x = "Date",
    y = "Value",
    color = "Factor",
    template = "plotly_dark")
fig_factors_over_time.show(renderer = "browser")



# Mkt-RF: Market excess return (Market return - Risk-free rate)
# SMB: Return difference between small-cap and large-cap stocks
# HML: Return difference between value stocks and growth stocks
# RMW: Return difference between firms with high profitability and low profitability
# CMA: Return difference between firms with conservative and aggressive investments
# Mom: Return difference between past winners and past losers (momentum effect)
#%%
#Retreive Stock Data and Calculate Monthly Returns
stock_data = yf.download(
    'AAPL',
    start = '2010-01-01',
    end = '2020-01-01',
    interval = '1mo')['Adj Close']

stock_returns = stock_data.pct_change().dropna()*100
print(stock_returns.head())

#%%
#Align Fama-French and Stock Data (Matching Date indicies)
ff_data_5f_mom_aligned, stock_returns_aligned = ff_data_5f_mom.align(
    stock_returns,
    join = 'inner',
    axis = 0
    )

excess_returns = stock_returns_aligned - ff_data_5f_mom_aligned['RF']
print(excess_returns.head())
#%%


#This will be are intercept(constant) and the values inside are are independent Variables
X_5f_mom = sm.add_constant(
    ff_data_5f_mom_aligned[['Mkt-RF', 'SMB', 'HML', 'RMW', 'CMA', 'Mom']]
    )

# These are the independent variables in the regression model:
# Mkt-RF: Market excess return (market return minus risk-free rate)
# SMB: Size factor (small minus big)
# HML: Value factor (high minus low book-to-market ratio)
# RMW: Robust minus weak factor (measures profitability)
# CMA: Conservative minus aggressive factor (measures investment behavior)
# Mom: Momentum factor (based on stock price momentum)
# These are the 5 Fama-French factors (plus the Momentum factor, Mom), which are commonly used to explain stock returns.
# After adding the constant, this creates a matrix X_5f_mom, which will be used as the independent variables in the regression model.



#OLS Regression
model_5f_mom = sm.OLS(
    excess_returns,
    X_5f_mom).fit()

# Extract the alpha (constant term)
alpha = model_5f_mom.params['const']

# Print the regression summary
print(model_5f_mom.summary())


# sm.add_constant(): Adds a constant (intercept) to the independent variables (Fama-French factors).
# sm.OLS(): Sets up an Ordinary Least Squares (OLS) regression model with excess_returns as the dependent variable and the Fama-French factors as independent variables.
# model_5f_mom.fit(): Fits the model to the data.
# alpha: Retrieves the constant (intercept) from the model, representing the alpha (excess return) for the stock.
# model_5f_mom.summary(): Prints the summary of the OLS regression, including coefficients, p-values, R-squared, etc.




# By running this regression:

# You're attempting to explain the stock's excess returns based on the Fama-French 5-factor model (with the addition of the momentum factor).
# The alpha (α) term in this regression tells you how much of the stock's return is unexplained by these factors, which is often interpreted as a measure of "abnormal" returns. A positive alpha suggests that the stock performed better than predicted by the factors, while a negative alpha indicates underperformance.









