import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

from backtest import backtest
from algorithm import algorithm

#do python main.py <ticker> to run this!
tester = backtest()

if len(sys.argv) >= 2:
    ticker = sys.argv[1]
    algo = algorithm(ticker)
else:
    print("No stock ticker given, defaulting to AAPL")
    algo = algorithm("AAPL")
    ticker = "AAPL"

tester.run(algo)
plt.figure(figsize=(10, 6), num="RSI Algorithm for "+ticker)
tester.calculateVol(algo)
tester.graphReturns(algo)
tester.graphRSI(algo)
tester.calculate_tot_returns(algo)
tester.calculate_market_return(algo)
plt.tight_layout()
plt.show()