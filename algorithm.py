import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta



class algorithm:
    portfolio = 0 #list of ticker, amt
    cash = 1000000
    start_date = "2021-12-13" #starts 14 trading days early to calculate the moving average ahead of time
    end_date = "2023-01-01"
    SPY = "SPY"
    market_ticker = yf.download(SPY, start_date, end_date, progress=False)
    fourteen_day_ma = []
    trades = []
    RSI_vals = []
    return_vals = []
    portfolio_vals = []
    RSI_day_count = 1
    prev_price = 0
    today_return = 0

    def __init__(self, tick):
        self.ticker_symbols = tick
        self.ticker = yf.download(self.ticker_symbols, self.start_date, self.end_date, progress=False)
        return

    def buy(self, tick, day):
        price_on_day = self.ticker.loc[day]["Close"]
        
        buy_amt = self.cash / price_on_day
        self.portfolio += buy_amt
        self.cash -= buy_amt * price_on_day
        data = {"AAPL", buy_amt, day}
        self.trades.append(data)

    def sell(self, tick, day): 
        price_on_day = self.ticker.loc[day]["Close"]

        sell_amt = self.portfolio
        self.portfolio -= sell_amt
        self.cash += sell_amt * price_on_day
        data = {"AAPL", -sell_amt, day}
        self.trades.append(data)

    def calculate_gain(self):
        total_gain = 0
        for i in self.fourteen_day_ma:
            if i > 0:
                total_gain += i
        if self.RSI_day_count > 14:
            self.RSI_day_count = 14

        return total_gain / self.RSI_day_count

    def calculate_loss(self):
        total_loss = 0
        for i in self.fourteen_day_ma:
            if i < 0:
                total_loss += i
        if self.RSI_day_count > 14:
            self.RSI_day_count = 14
        return -(total_loss / self.RSI_day_count)

    def RSI_val(self, day):
        self.fourteen_day_ma.append(self.today_return - 1) # -1 for changing to excess return
        if self.RSI_day_count >= 14:
            self.fourteen_day_ma.pop(0)
        avg_gain = self.calculate_gain()
        avg_loss = self.calculate_loss()
        return 100 - (100 / (1 + avg_gain/avg_loss)) #known divide by zero issue

    def getCurrVal(self, day):
        price_on_day = self.ticker.loc[day]["Close"]
        portfolio_val = price_on_day*self.portfolio + self.cash
        return portfolio_val

    def decide(self, tick, day):
        if self.RSI_day_count == 1:
            self.RSI_day_count += 1
            self.prev_price = self.ticker.loc[day]["Close"]
            return
        self.today_return = self.ticker.loc[day]["Close"] / self.prev_price
        self.return_vals.append(self.today_return)
        self.ticker_symbols = tick #currently a string, should be an array of strings eventually
        RSI = self.RSI_val(day)
        self.RSI_vals.append(RSI)
        if RSI >= 70:
            self.sell("AAPL", day)
        elif RSI <= 30:
            self.buy("AAPL", day)
        self.prev_price = self.ticker.loc[day]["Close"] 
        self.RSI_day_count += 1

        self.portfolio_vals.append(self.getCurrVal(day))