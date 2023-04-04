import pandas as pd
import yfinance as yf
import datetime
from datetime import date,timedelta
import plotly.graph_objects as go
import plotly.express as px
today= date.today()

d1= today.strftime("%Y-%m-%d")
end_date =d1
d2 = date.today() - timedelta(days=720)
d2= d2.strftime("%Y-%m-%d")
start_date= d2

data = yf.download('AAPL',start=start_date,end=end_date,progress= False)
print(data.head())

figure= px.line(data, x = data.index, y="Close",title= "Time series Analysis")
figure.show()

figure = go.Figure(data= [go.Candlestick(x=data.index,open=data['Open'],high=data['High'],low=data['Low'],close=data['Close'])])
figure.update_layout(title="time sereis analysis (candlestick chart)", xaxis_rangeslider_visible= False)
figure.update_xaxes(rangeslider_visible=True,rangeselector =dict(buttons= list([dict(count = 1, label ='1m',step= 'month',stepmode ='backward'),
                                                                                dict(count = 6, label ='6m',step= 'month',stepmode ='backward'),
                                                                                dict(count = 1, label ='YTD',step= 'year',stepmode ='todate'),
                                                                                dict(count = 1, label ='1y',step= 'year',stepmode ='backward'),
                                                                                dict(step='all')
                                                                                
                                                                                ])))
figure.show()


figure = px.bar(data,x= data.index,y="Close",title="time series analysis (Bar plot)")

figure.show()

figure= px.line(data, x = data.index, y="Close",range_x =['2022-07-01','2022-12-31'],title= "Time series Analysis(custom range)")


figure.show()
