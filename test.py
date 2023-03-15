import inline as inline
import matplotlib
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing the sales data set
df=pd.read_csv("C:/Users/Danilson Zammit/Desktop/data/vgsales.csv")
df.head()

GameRange = pd.DataFrame(df.query('Year >= 2010 and Year <= 2016 and Publisher.isin(["Electronic Arts", "Activision", "Take-Two Interactive"])', inplace=False))
publisher_sales = GameRange.groupby(['Year', 'Publisher'])['Global_Sales'].sum().reset_index()
publisher_sales_pivot = publisher_sales.pivot_table(values='Global_Sales', index='Year', columns='Publisher')
publisher_game_sales = GameRange.groupby(['Publisher', 'Name'])['Global_Sales'].sum().reset_index()

def showGameSales():


    # Pivot the data to create a table with Years as rows and Publishers as columns


    # Plot a stacked bar graph with Publisher sales for each Year
    publisher_sales_pivot.plot(kind='bar', stacked=True)
    plt.title('Global Sales by Publisher (2010-2016)')
    plt.xlabel('Year')
    plt.ylabel('Global Sales ($ millions)')
    plt.show()


ticker1 = "EA"
ticker2 = "TTWO"
ticker3 = "ATVI"

# Loading EA's stock data into Python from Yahoo Finance
EA_df = yf.download(ticker1, start="2010-01-01", end="2016-12-31")
TTWO_df = yf.download(ticker2, start="2010-01-01", end="2016-12-31")
ATVI_df = yf.download(ticker3, start="2010-01-01", end="2021-12-31")


def showStocks():


    plt.plot(EA_df['Close'], label='EA', color='blue')
    plt.plot(TTWO_df['Close'], label='TTWO', color='orange')
    plt.plot(ATVI_df['Close'], label='ATVI', color='green')
    plt.title('Stock Prices of EA,TTWO and ATVI in USD')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()

def showBestSelling():
    top_5_ea_games = publisher_game_sales[publisher_game_sales['Publisher'] == 'Electronic Arts'].nlargest(5,
                                                                                                           'Global_Sales')
    top_5_atvi_games = publisher_game_sales[publisher_game_sales['Publisher'] == 'Activision'].nlargest(5,
                                                                                                        'Global_Sales')
    top_5_ttwo_games = publisher_game_sales[publisher_game_sales['Publisher'] == 'Take-Two Interactive'].nlargest(5,
                                                                                                                  'Global_Sales')

    # Combine the top 5 games for each Publisher into a single dataframe
    top_15_games = pd.concat([top_5_ea_games, top_5_atvi_games, top_5_ttwo_games], ignore_index=True)

    # Create a bar chart showing the Global Sales of the top 5 games for each Publisher
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(top_15_games['Name'], top_15_games['Global_Sales'])
    ax.set_title('Top 5 Best Selling Games of Electronic Arts, Activision and Take-Two Interactive (2010-2016)')
    ax.set_xlabel('Game Title')
    ax.set_ylabel('Global Sales ($ millions)')
    plt.xticks(rotation=90)
    plt.show()


showBestSelling();





