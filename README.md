# Description
## In this repository I focus on some of the stock based optimizations / analysis techniques I have learned. I have labeled each python file under every title with the phrase "Code Label" for easy navigation and reference. For security reasons, I have removed my API key, username, and password from some of the files.Please ensure to replace them with your own credentials when running the code. Also remember to change file paths.  Special thanks to Scott Liang for the help and knowledge to run many of these codes. If you would like to reach him or me please contact  me at Armanis Constanzo on LinkedIn.






## *Stock-Portfolio-Optimization-Analysis*

## Code Label = MonteCarelo Simulations, API Keys,Optimized Weights,etcNoKey


### This project  analyzes historical stock data to create an optimized investment portfolio. Using the Financial Modeling Prep API, I fetched historical price data for several companies and calculated daily returns. I performed a Monte Carlo simulation to generate 1,000 random portfolios with different asset allocations, then computed key portfolio metrics such as expected return, volatility, and Sharpe ratio. The goal was to find the portfolio with the highest Sharpe ratio, indicating the best risk-adjusted return. The results were visualized with a cumulative return plot to track portfolio performance over time. 

![image](https://github.com/user-attachments/assets/7771ebae-a06a-48c4-983c-12e33695cc25)



## *Stock Return Analysis Using WRDS Data*

## Code Label = APikeys,QueryingWithSQL,Crspr

### In this project we connected to the WRDS database and extracted monthly stock return data from the CRSP database for companies since 2010. Cleaned the data, calculated compounded returns, and aggregated monthly returns to compute annual returns by stock. Merged stock return data with company information (tickers and names) to enrich the dataset. Calculated the average annual return for each year and visualized the trends with a line graph. This processed involved SQL querying, data processing, and financial analysis with Python.

![image](https://github.com/user-attachments/assets/19c31b05-a60b-48a0-af32-070e6c5c09fa)



## *Financial Ratios Analysis and Visualization*

## Code Label = APIRequest&DefiningFunctionsUsingFMPLibaryWithNoKey

### In this project, I use the Financial Modeling Prep (FMP) API to fetch key financial ratios (P/E ratio and D/E ratio) for various companies, including Apple (AAPL), Microsoft (MSFT), Google (GOOG), Amazon (AMZN), and NVIDIA (NVDA). The data is then processed into a pandas DataFrame where each entry includes the company name, the quarter, the P/E ratio, and the D/E ratio. I consolidate the financial data for all companies into a single DataFrame and convert the "Quarter" column to a pandas datetime format for proper time-series analysis. Using Plotly, I create a subplot with two charts: one for P/E ratios and the other for D/E ratios, plotted over time for each company. These plots allow for an insightful comparison of how each company’s P/E and D/E ratios evolve across different quarters. 

![image](https://github.com/user-attachments/assets/25b09cce-4a0c-4f71-b896-7b61dc65eb1e)



## *WTI Crude Oil Price Forecasting with ARIMA, ETS, and Prophet Models*

## Code Label = Arima,ETS, and Prophet Model TrainingUsingFred

### In this project, I analyze the historical WTI Crude Oil prices using time-series forecasting techniques. The data is retrieved from the Federal Reserve Economic Data (FRED) API using the pandas_datareader library, and then processed to a monthly frequency. The processed data is converted into a TimeSeries object using the Darts library to facilitate time-series modeling.I apply three different forecasting models: ARIMA, Exponential Smoothing (ETS), and Prophet, to predict future values. After splitting the data into training and validation sets, I fit the models on the training data and generate forecasts. The model predictions are then compared visually with the actual validation data. Additionally, I calculate performance metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) to assess the accuracy of each model. The final step involves refitting each model using the full dataset and forecasting the next 24 months of WTI Crude Oil prices. The future forecasts are visualized alongside the original time series for comparison. This project demonstrates proficiency in time-series forecasting, model evaluation, and forecasting future trends using multiple algorithms.

![image](https://github.com/user-attachments/assets/62abeccf-18ce-4a85-8885-7038123178d7)

![image](https://github.com/user-attachments/assets/24df8e41-e1d0-4844-9811-ee36b69602d4)



## *Discounted Cash Flow (DCF) Valuation of AAPL using Free Cash Flow (FCF) and WACC*

## Code Label = DCF's & ValuationWithnokey

### In this project, I perform a discounted cash flow (DCF) analysis to estimate the intrinsic value of Apple Inc. (AAPL) based on its free cash flows (FCF). Using the Financial Modeling Prep API, I retrieve the company’s cash flow statement and extract FCF data for the last 5 years. The historical growth rate of FCF is calculated, and based on this, I project the FCF for the next 5 years. A terminal value is also estimated using a terminal growth rate of 4%, and the free cash flows and terminal value are discounted to the present value using a weighted average cost of capital (WACC) of 8%. To account for the company’s net debt, I fetch the balance sheet data, calculate net debt, and subtract it from the enterprise value to determine the equity value. Finally, I estimate the price per share based on the number of shares outstanding. 


![image](https://github.com/user-attachments/assets/51f676cd-85ae-4a23-8880-fd4b8cb9c783)






## *Stock Technical Analysis with Multiple Indicators: SMAs, WMA, Bollinger Bands, MACD, and RSI*

## Code Label = Examples of taking portfolios and graphing Indicators and Bollinger Bands


### In this project, I perform technical analysis on a selection of stocks using various indicators such as Simple Moving Averages (SMA), Weighted Moving Average (WMA), Bollinger Bands, MACD, and Relative Strength Index (RSI). The data is retrieved using the `yfinance` library and is then processed for each ticker from January 2023 to January 2024. For each stock, I calculate SMAs for different time windows (90 and 70 periods), WMA, Bollinger Bands, MACD, and RSI using pandas_ta for technical indicators. The results are visualized using `mplfinance` for candlestick charting, with added trendlines, and `matplotlib` for MACD and RSI plots. The visualizations help track stock price movements and assess overbought or oversold conditions, providing insights for traders and analysts.


![image](https://github.com/user-attachments/assets/af88fd0a-680e-412f-b6c0-6be610df866e)
![image](https://github.com/user-attachments/assets/69f531cf-c753-456d-a7c9-4a165358d709)
![image](https://github.com/user-attachments/assets/2e9171c6-1e14-42f2-ba6e-313ee39b13fb)

### - Although more charts will be generated when the code is run, I’ve limited the output to show only one company for demonstration purposes.





## *Fama-French Three-Factor Model Analysis for Apple (AAPL) Stock*

## Code Label = Fama-French Three-Factor Data RegressionTraining

### In this project, I analyze the relationship between Apple Inc.'s (AAPL) stock returns and the Fama-French three-factor model, which includes the Market Risk Premium (Mkt-RF), the Size Premium (SMB), and the Value Premium (HML). The data for the Fama-French factors is retrieved from the pandas_datareader API, covering the period from 2010 to 2020, while the stock data for Apple is fetched from Yahoo Finance.The analysis begins with data preprocessing, including aligning the Fama-French factors with Apple's stock returns and calculating excess returns. I then fit an Ordinary Least Squares (OLS) regression model to predict Apple’s excess returns using the Fama-French factors as predictors. The model’s performance is evaluated, and visualizations are provided for each factor’s contribution to excess returns, along with a bar plot of the regression coefficients and p-values. The results offer insights into how market risk, size, and value factors influence Apple's stock performance during the analysis period.


![image](https://github.com/user-attachments/assets/a080388d-3356-4e7c-b90f-1097b2baf31e)

![image](https://github.com/user-attachments/assets/6b247818-4a3e-4488-a58d-af956ee3089e)

### - Although more charts will be generated when the code is run, I’ve limited the output to show only two charts for demonstration purposes.



## *Fama-French Five-Factor Model with Momentum for Apple (AAPL) Stock*

## Code Label = FF5 OLS Regression training

### This project analysis the Fama-French Five-Factor Model with an added Momentum factor to explain Apple Inc.'s (AAPL) stock returns from 2010 to 2020. The Fama-French Five-Factor Model includes five factors: Market Risk Premium (Mkt-RF), Size Premium (SMB), Value Premium (HML), Profitability (RMW), and Investment (CMA). Additionally, the Momentum (Mom) factor is incorporated to capture the impact of stock price momentum on AAPL's returns.The data for the Fama-French factors and the Momentum factor is retrieved from the pandas_datareader API, and stock data for Apple is fetched from Yahoo Finance. After aligning the factors with Apple's stock returns, I calculate the **excess returns** by subtracting the risk-free rate (RF) from the stock returns. I then fit an Ordinary Least Squares (OLS) regression model to estimate the relationship between Apple's excess returns and the Fama-French factors. The project visualizes the behavior of the Fama-French factors and the Momentum factor over time, and the regression results are analyzed to understand the significance and impact of each factor on Apple's stock performance. The regression model’s alpha (constant term) represents any unexplained portion of the returns, offering insights into whether Apple outperforms the market beyond the factors considered.



![image](https://github.com/user-attachments/assets/a6f3c1fa-adee-48b7-b76a-7afd4f5b6c97)





## *Housing Price Prediction and Bitcoin Price Forecasting*

## Code Label = FutureHousing_BitCoinForCastForMultipleRegressions

### This project provides a comprehensive approach to predicting housing and Bitcoin prices using both regression and time series forecasting models. By evaluating multiple models, we gain insights into which models perform best for different types of time series data. The visualizations and performance metrics allow for a clear comparison of model accuracy and help inform decision-making for forecasting future prices.



![image](https://github.com/user-attachments/assets/97a0dc44-7d3a-4bde-a2a2-d1452cf53166)
![image](https://github.com/user-attachments/assets/ca5334d4-52ee-4b14-a55c-363d1583aaa9)







