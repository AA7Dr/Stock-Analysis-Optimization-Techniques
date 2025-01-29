#%%
import requests
import pandas as pd
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from plotly.offline import plot

# Replace with your FMP API key
api_key = 'V6CD62kaSoXAN6Wbj96yqLWXIRqw3wjd'

ticker = 'AAPL'
url = f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?limit=10&apikey={api_key}"
response = requests.get(url)
cash_flows = response.json()
#%%
# Extract FCF for the last 5 years
fcf_data=[]
for entry in cash_flows [:5]:
    fcf_data.append({
        'date': entry['date'],
        'FCF': entry ['freeCashFlow']
        })

df_fcf =pd.DataFrame(fcf_data)

# Step 2: Estimate Growth Rate
# Calculate the historical growth rate of FCF
#%%

df_fcf = df_fcf.sort_values(by = 'date')
df_fcf['FCF Growth'] = df_fcf['FCF'].pct_change()

growth_rate = df_fcf['FCF Growth'].mean()
growth_rate
#%%

years=5

projected_fcf=[]

last_fcf = df_fcf.iloc[0]['FCF'] #iloc is for grabbing specific rows

for i in range(1,years+1):
    projected_fcf.append(last_fcf*(1+growth_rate)**i)
    
projected_fcf
    
#%%

terminal_growth_rate =.04
terminal_value = projected_fcf[-1]*(1+terminal_growth_rate) / (.08-terminal_growth_rate) #.08 = Cost of Capital       (r-g)

terminal_value

#%%

wacc =.08 # weighted average cost of capital(the amount of Debt / Equity a company has )
discounted_fcf=[cf/(1+wacc)**i for i, cf in enumerate(projected_fcf, start = 1)]
discounted_terminal_value = terminal_value / (1+wacc)**years

#%%
#Shows value of the entire company but doesnt deduct debt

enterprise_value = sum(discounted_fcf)+ discounted_terminal_value

enterprise_value 







#%%
# Step 7: Get Net Debt
# Fetch balance sheet data to get net debt
balance_sheet_url = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?limit=1&apikey={api_key}"
balance_sheet_response = requests.get(balance_sheet_url)
balance_sheet = balance_sheet_response.json()[0]

net_debt=balance_sheet['totalDebt'] - balance_sheet['cashAndCashEquivalents'] #Shows value of the entire company and does deduct debt
net_debt



#%%

equity_value = enterprise_value - net_debt

shares_outstanding = 15300000000  #shares outstanding is behind paywall 

price_per_share = equity_value / shares_outstanding

price_per_share
#%%
# Print the results
print(f"Projected FCFs: {projected_fcf}")
print(f"Discounted FCFs: {discounted_fcf}")
print(f"Terminal Value: {terminal_value}")
print(f"Discounted Terminal Value: {discounted_terminal_value}")
print(f"Enterprise Value: {enterprise_value}")
print(f"Price per share: {price_per_share}")