# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:01:49 2024

@author: Armanis
"""

import requests
import pandas as pd
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from plotly.offline import plot 

# replace with your FMP API key 

api_key = 'V6CD62kaSoXAN6Wbj96yqLWXIRqw3wjd'


def fetch_financial_ratios(ticker):
    url = f'https://financialmodelingprep.com/api/v3/ratios/{ticker}?limit=4&apikey={api_key}'
    response =requests.get(url)
    ratios = response.json()
    
  #If ratios is found and in a list format and if their is a value proceed and make a dataframe consisting of whats below
    if isinstance (ratios,list) and len(ratios) > 0:
        return pd.DataFrame([{
            'Company':ticker, # Creates column company with value set to ticker
            'Quarter':entry['date'],
            'P/E Ratio':entry.get('priceEarningsRatio', None), #is used to retrieve the value associated with the key 'priceEarningsRatio'. If the key doesn't exist, it returns None instead of raising an error.
            'D/E Ratio': entry.get('debtEquityRatio',None),
            } for entry in ratios]) #For each item in the ratios list, a dictionary is created with the fields "Company", "Quarter", "P/E Ratio", and "D/E Ratio". These dictionaries are used to build the rows in the pandas DataFrame.
    else:
        return pd.DataFrame()
    
    
    #%%
    # retriving tickers & ma dataframes
df_appl = fetch_financial_ratios('AAPL')
df_msft = fetch_financial_ratios('MSFT')
df_goog = fetch_financial_ratios('GOOG')
df_amzn = fetch_financial_ratios('AMZN')
df_Nvda = fetch_financial_ratios('NVDA')
    
    
    #%%
    # retriving tickers& combines multiple  dataframes into one
df_ratios = pd.concat([df_amzn,df_appl,df_goog,df_msft],
                          ignore_index = True)
df_ratios
    
    #%%
 # Convert Quarter column to a pandas datetime format
df_ratios['Quarter'] = pd.to_datetime(df_ratios['Quarter'])
    
 # Create subplots for P/E and D/E Ratios
fig = sp.make_subplots(rows = 2, cols = 1, shared_xaxes = True,
                           subplot_titles= ('P/E Ratio Over Quarters',
                                            'D/E Ratio Over Quarters'))
    
    #%%
  # Add P/E Ratio traces
for company in df_ratios['Company'].unique():
    company_data = df_ratios[df_ratios['Company'] == company ]
    fig.add_trace(go.Scatter(x = company_data['Quarter'],
                             y = company_data['P/E Ratio'],
                             name = f'{company} P/E Ratio',),row = 1, col =1 )
        
        
        #%%
       # Add D/E Ratio traces
for company in df_ratios['Company'].unique():
    company_data = df_ratios[df_ratios['Company'] == company]
    fig.add_trace(go.Scatter(x = company_data['Quarter'],
                             y = company_data['D/E Ratio'],
                             name = f'{company} D/E Ratio',),row = 2, col =1 )  
# Update layout
fig.update_layout(height = 800,title_text = 'P/E and D/E Ratios Over Quarters',showlegend = True)
fig.update_xaxes(title_text ='Quarter')
fig.update_yaxes(title_text ='P/E Ratio', row =1, col =1)
fig.update_yaxes(title_text ='D/E Ratio', row =2, col =1)
plot(fig)
