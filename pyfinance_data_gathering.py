import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web 

style.use('ggplot')

# start = dt.datetime(2000, 1, 1)
# end = dt.datetime(2016, 12, 31)

# dataframe
# df = web.DataReader('TSLA', 'yahoo', start, end)

# print first 10 rows
# print(df.head(10))

# print last 10 rows
# print('\n', df.tail(10))

# # convert dataframe to 
# df.to_csv('tesla.csv')


# read dataframe from csv
# df = pd.read_csv('tesla.csv', parse_dates=True, index_col=0)

# head from csv
# print(df.head())

# plot datframe to graph & show
# df.plot()
# plt.show()
  

# ma = moviing average, ma uses last 100 data points to create moving average
# min_periods =. minimum periods to calc 
# df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
#dropna = remove any NaN vars
# df.dropna(inplace=True)
# head wont have the 100 datapoints to create moving average, tail does
# print(df.head())
# print(df.tail())

# graphing datafranme with just matplotlib
# ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
# ax2 = plt.subplot2grid((6,1), (5,0), rowspan=5, colspan=1, sharex=ax1)

# plot line df.index is the date ref through df.index
# ax1.plot(df.index, df['Adj Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Volume'])

# plt.show()


# dataframe
df = pd.read_csv('tesla.csv', parse_dates=True, index_col=0)

# resample the dataframe to 10 days, ohlc = open, high, low, close
df_ohlc = df['Adj Close'].resample('10D').ohlc()
# resample volume of staiock, use sum vs mean to get true volume 
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

# print(df_ohlc.head())

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=5, colspan=1, sharex=ax1)

ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g', colordown='r')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
plt.show()