import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta



class algorithm:
    portfolio = 0 #list of ticker, amt
    cash = 1000000
    start_date = "2021-12-13"
    end_date = "2023-01-01"
    SPY = "SPY"
    market_ticker = yf.download(SPY, start_date, end_date, progress=False)
    trades = []
    portfolio_vals = []
    # TODO put whatever else you would like in here!

    def __init__(self, tick):
        self.ticker_symbols = tick
        self.ticker = yf.download(self.ticker_symbols, self.start_date, self.end_date, progress=False)
        return

    # Buy the maximum amount of the stock possible
    def buy(self, tick, day):
        price_on_day = self.ticker.loc[day]["Close"]
        
        buy_amt = self.cash / price_on_day
        self.portfolio += buy_amt
        self.cash -= buy_amt * price_on_day
        data = {tick, buy_amt, day}
        self.trades.append(data)

    # Sell the maximum amount of the stock possible
    def sell(self, tick, day): 
        price_on_day = self.ticker.loc[day]["Close"]

        sell_amt = self.portfolio
        self.portfolio -= sell_amt
        self.cash += sell_amt * price_on_day
        data = {tick, -sell_amt, day}
        self.trades.append(data)

    def getCurrVal(self, day):
        price_on_day = self.ticker.loc[day]["Close"]
        portfolio_val = price_on_day*self.portfolio + self.cash
        return portfolio_val

    def decide(self, tick, day):
        # TODO decide when to buy and when to sell based on the stock



        self.portfolio_vals.append(self.getCurrVal(day))