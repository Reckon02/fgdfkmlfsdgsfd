import yfinance as yf
import pandas as pd

days = "YTD"
interval = "1d"

# Get the stock data for Apple Inc. (AAPL)
stock = yf.Ticker("AAPL")
df_aapl = stock.history(period=days, interval=interval)

# Add a new column with the stock name
df_aapl["Stock"] = "AAPL"

# Add a new column with the date of the stock data
df_aapl["Date"] = df_aapl.index.date
# Convert the datetime values to be timezone unaware
#df_aapl.index = df_aapl.index.tz_localize(None)

# Get the stock data for Amazon (AMZN)
#stock = yf.Ticker("AMZN")
#df_amzn = stock.history(period=days, interval=interval)

# Add a new column with the stock name
#df_amzn["Stock"] = "AMZN"

# Add a new column with the date of the stock data
#df_amzn["Date"] = df_amzn.index.date

# Convert the datetime values to be timezone unaware
#df_amzn.index = df_amzn.index.tz_localize(None)

# Combine the data for both stocks
df = pd.concat([df_aapl,])

# Set the "Stock" column as the index
df.set_index("Stock", inplace=True)

# Save the data to an Excel file
df.to_excel("stock_prices1.xlsx")

# Save the data to a CSV file as well
df.to_csv("stock_prices.csv")