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

db = wrds.Connection(wrds_username = "username", wrds_password = "PW") #Your username and PW

#%%
#permno = unique identifier 

query = """
    SELECT permno, date, ret    
    FROM crsp.msf
    WHERE date >= '2010-01-01'
"""
    

monthly_data =db.raw_sql(query)

#%%


ticker_query = """
    SELECT permno, ticker, comnam   
    FROM crsp.stocknames
"""
ticker_data =db.raw_sql(ticker_query)
    
db.close() #Closes connection to DB

#%%



monthly_data['date']= pd.to_datatime(monthly_data['date'])

monthly_data.dropna(subset = ['ret'],inplace = True ) #Inplace = replace #subset = what columns your looking for N/A's

monthly_data['compound_ret'] = 1+monthly_data['ret'] 

monthly_data['year'] = monthly_data['date'].dt.year #date.year


#%%


annual_returns = monthly_data.groupby(['permno','year'])['compound_ret'].prod()-1

annual_returns.column = ['permno', 'year', 'annual_ret']

#%%


annual_returns = annual_returns.merge(ticker_data, on = 'permno', how = 'left') #Merge datasets ticker_query and query to have super dataset

print(annual_returns)


#%%

average_annual_returns = annual_returns.groupby('year')['annual_ret'].mean().reset_index()

#%%

plt.figure(figsize =(10,6))
plt.plot(average_annual_returns['year'],
         average_annual_returns['annual_ret'],
         marker='o',
         color='g')

plt.grid()
plt.show()

