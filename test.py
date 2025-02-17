#!/usr/bin/env python3
import yfinance as yf
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
print("Hello")


ticker_symbol = "AAPL"
ticker_symbol_2 = "NVDA"
start_date = "2020-01-01"
end_date = "2024-01-01"

ticker = yf.Ticker(ticker_symbol)
historical_data = ticker.history(start=start_date, end=end_date)

#print("Historical Prices for ", ticker_symbol)
#print(historical_data)
df = pd.DataFrame(historical_data)

end_date = datetime.now().strftime('%Y-%m-%d')
historical_data = ticker.history(start='2020-01-01',end=end_date)

 
df = pd.DataFrame(historical_data)

# Print the DataFrame
print("Historical Stock Price Data for", ticker_symbol)
print(df)

# Plotting the closing price
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Close'], label='Close Price', color='blue')
plt.title('Historical Stock Price Data for ' + ticker_symbol)
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()