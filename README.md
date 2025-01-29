# Description
## In this repository I focus on stock based optimizations / analysis techniques . I have labeled each python file under every title with the phrase "Code Label" for easy navigation and reference. For security reasons, I have removed my API key, username, and password from some of the files. Please ensure to replace them with your own credentials when running the code.






## *Stock-Portfolio-Optimization-Analysis*

## Code Label = MonteCarelo Simulations, API Keys,Optimized Weights,etc

### This project  analyzes historical stock data to create an optimized investment portfolio. Using the Financial Modeling Prep API, I fetched historical price data for several companies and calculated daily returns. I performed a Monte Carlo simulation to generate 1,000 random portfolios with different asset allocations, then computed key portfolio metrics such as expected return, volatility, and Sharpe ratio. The goal was to find the portfolio with the highest Sharpe ratio, indicating the best risk-adjusted return. The results were visualized with a cumulative return plot to track portfolio performance over time. 




## *Stock Return Analysis Using WRDS Data*

## Code Label = APikeys,QueryingWithSQL,Crspr

### In this project we connected to the WRDS database and extracted monthly stock return data from the CRSP database for companies since 2010. Cleaned the data, calculated compounded returns, and aggregated monthly returns to compute annual returns by stock. Merged stock return data with company information (tickers and names) to enrich the dataset. Calculated the average annual return for each year and visualized the trends with a line graph. This processed involved SQL querying, data processing, and financial analysis with Python.




## *Financial Ratios Analysis and Visualization*

## Code Label = APIRequest&DefiningFunctionsUsingFMPLibaryWithNoKey

### In this project, I use the Financial Modeling Prep (FMP) API to fetch key financial ratios (P/E ratio and D/E ratio) for various companies, including Apple (AAPL), Microsoft (MSFT), Google (GOOG), Amazon (AMZN), and NVIDIA (NVDA). The data is then processed into a pandas DataFrame where each entry includes the company name, the quarter, the P/E ratio, and the D/E ratio. I consolidate the financial data for all companies into a single DataFrame and convert the "Quarter" column to a pandas datetime format for proper time-series analysis. Using Plotly, I create a subplot with two charts: one for P/E ratios and the other for D/E ratios, plotted over time for each company. These plots allow for an insightful comparison of how each company’s P/E and D/E ratios evolve across different quarters. 




### WTI Crude Oil Price Forecasting with ARIMA, ETS, and Prophet Models

In this project, I analyze the historical WTI Crude Oil prices using time-series forecasting techniques. The data is retrieved from the Federal Reserve Economic Data (FRED) API using the `pandas_datareader` library, and then processed to a monthly frequency. The processed data is converted into a `TimeSeries` object using the Darts library to facilitate time-series modeling.

I apply three different forecasting models: ARIMA, Exponential Smoothing (ETS), and Prophet, to predict future values. After splitting the data into training and validation sets, I fit the models on the training data and generate forecasts. The model predictions are then compared visually with the actual validation data. Additionally, I calculate performance metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) to assess the accuracy of each model.

The final step involves refitting each model using the full dataset and forecasting the next 24 months of WTI Crude Oil prices. The future forecasts are visualized alongside the original time series for comparison. This project demonstrates proficiency in time-series forecasting, model evaluation, and forecasting future trends using multiple algorithms.






