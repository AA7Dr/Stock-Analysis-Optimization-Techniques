# Description
## In this repository I focus on stock based optimizations / analysis techniques . I have labeled each python file under every title with the phrase "Code Label" for easy navigation and reference.












## *Stock-Portfolio-Optimization-Analysis*

## Code Label = MonteCarelo Simulations, API Keys,Optimized Weights,etc

### This project  analyzes historical stock data to create an optimized investment portfolio. Using the Financial Modeling Prep API, I fetched historical price data for several companies and calculated daily returns. I performed a Monte Carlo simulation to generate 1,000 random portfolios with different asset allocations, then computed key portfolio metrics such as expected return, volatility, and Sharpe ratio. The goal was to find the portfolio with the highest Sharpe ratio, indicating the best risk-adjusted return. The results were visualized with a cumulative return plot to track portfolio performance over time. 

## Code Label = MonteCarelo Simulations, API Keys,Optimized Weights,etc


## *Stock Return Analysis Using WRDS Data*

## Code Label = APikeys,QueryingWithSQL,Crspr

### In this project we connected to the WRDS database and extracted monthly stock return data from the CRSP database for companies since 2010. Cleaned the data, calculated compounded returns, and aggregated monthly returns to compute annual returns by stock. Merged stock return data with company information (tickers and names) to enrich the dataset. Calculated the average annual return for each year and visualized the trends with a line graph. This processed involved SQL querying, data processing, and financial analysis with Python.


