# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:04:28 2024

@author: Armanis
"""
#pip install wrds


import wrds
import pandas as pd
import matplotlib.pyplot as plt

#%%

db = wrds.Connection(wrds_username = "username", wrds_password = "password") #Your username and PW

#%% Query for monthly data from CRSP database
query = """
    SELECT permno, date, ret    
    FROM crsp.msf
    WHERE date >= '2010-01-01'
"""

monthly_data = db.raw_sql(query) #Permno = unique identifiers of tickers

#%% Query for ticker data
ticker_query = """
    SELECT permno, ticker, comnam   
    FROM crsp.stocknames
"""
ticker_data = db.raw_sql(ticker_query)

db.close()  # Close connection to DB

#%% Preprocessing of monthly data
monthly_data['date'] = pd.to_datetime(monthly_data['date'])  # Convert date column to datetime
monthly_data.dropna(subset=['ret'], inplace=True)  # Drop rows where 'ret' is NaN
monthly_data['compound_ret'] = 1 + monthly_data['ret']  # Calculate compounded return
monthly_data['year'] = monthly_data['date'].dt.year  # Extract year from date

#%% Calculate annual returns
annual_returns = monthly_data.groupby(['permno', 'year'])['compound_ret'].prod() - 1

# Rename the columns of annual_returns DataFrame
annual_returns = annual_returns.reset_index()  # Reset index to get 'permno' and 'year' as columns
annual_returns.columns = ['permno', 'year', 'annual_ret']  # Rename columns properly

#%% Merge the annual returns with the ticker data
annual_returns = annual_returns.merge(ticker_data, on='permno', how='left')

print(annual_returns)  # Print the merged dataset

#%% Calculate average annual returns
average_annual_returns = annual_returns.groupby('year')['annual_ret'].mean().reset_index()

#%% Plot the average annual returns
plt.figure(figsize=(10, 6))
plt.plot(average_annual_returns['year'], average_annual_returns['annual_ret'], marker='o', color='g')
plt.grid()
plt.title('Average Annual Returns')
plt.xlabel('Year')
plt.ylabel('Average Annual Return')
plt.show()

