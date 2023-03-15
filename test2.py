import inline as inline
import matplotlib
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the sales data set
df = pd.read_csv("C:/Users/Danilson Zammit/Desktop/data/vgsales.csv")

GameRange = pd.DataFrame(df.query('Year >= 2010 and Year <= 2016 and Publisher.isin(["Electronic Arts", "Activision", "Take-Two Interactive"])', inplace=False))


def showGameSales(ax):
    publisher_sales = GameRange.groupby(['Year', 'Publisher'])['Global_Sales'].sum().reset_index()

    # Pivot the data to create a table with Years as rows and Publishers as columns
    publisher_sales_pivot = publisher_sales.pivot_table(values='Global_Sales', index='Year', columns='Publisher')

    # Plot a stacked bar graph with Publisher sales for each Year
    publisher_sales_pivot.plot(kind='bar', stacked=True, ax=ax)
    ax.set_title('Global Sales by Publisher (2010-2016)')
    ax.set_xlabel('Year')
    ax.set_ylabel('Global Sales ($ millions)')

    return ax


ticker1 = "EA"
ticker2 = "TTWO"
ticker3 = "ATVI"

# Loading EA's stock data into Python from Yahoo Finance
EA_df = yf.download(ticker1, start="2010-01-01", end="2016-12-31")
TTWO_df = yf.download(ticker2, start="2010-01-01", end="2016-12-31")
ATVI_df = yf.download(ticker3, start="2010-01-01", end="2016-12-31")


def showStocks(ax):
    ax.plot(EA_df['Close'], label='EA', color='blue')
    ax.plot(TTWO_df['Close'], label='TTWO', color='orange')
    ax.plot(ATVI_df['Close'], label='ATVI', color='green')
    ax.set_title('Stock Prices of EA, TTWO and ATVI in USD')
    ax.set_xlabel('Date')
    ax.set_ylabel('Stock Price')
    ax.legend()

    return ax


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Plot the game sales graph in the first subplot
ax1 = showGameSales(ax1)

# Plot the stock prices graph in the second subplot
ax2 = showStocks(ax2)

# Display the figure
plt.tight_layout()
plt.show()
