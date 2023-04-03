import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from datetime import datetime

sns.set()

births=pd.read_csv("births.csv")

births['decade'] = 10 * (births['year'] // 10)

birth_decade = births.pivot_table('births', index='decade', columns='gender', aggfunc='sum')
birth_decade.plot()
plt.ylabel("Total births per year")
#plt.show()

#remove missing values or mistyped data

quartiles = np.percentile(births['births'], [25, 50, 75])
mu= quartiles[1]
sig = 0.74 *(quartiles[2]-quartiles[0])

#filter out rows with births outside mean value

births =births.query('(births > @mu-5 * @sig) & (births < @mu + 5 * @sig)')

births['day']=births['day'].astype(int)

births.index = pd.to_datetime(10000*births.year+100*births.month+births.day, format ='%Y%m%d')

births['dayofweek']=births.index.dayofweek

# plot births by weekday

births.pivot_table('births',index='dayofweek',columns='decade',aggfunc='mean').plot()
plt.gca().set_xticklabels(['Mon','Tues','Wed','Thurs','Fri','Sat','Sun'])
plt.ylabel('mean births by day')

#create groups of the data by month and day

births_month =births.pivot_table('births',[births.index.month , births.index.day])
print(births_month.head())

births_month.index=[datetime(2012,month,day) for (month , day) in births_month.index ]

print(births_month.head())

#average number of births by date of the year

fig,ax = plt.subplots(figsize = (12, 4))
births_month.plot(ax=ax)

plt.show()