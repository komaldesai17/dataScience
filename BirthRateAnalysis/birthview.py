import pandas as pd

births=pd.read_csv("births.csv")
#print top records
print(births.head()) 
#remove NA i.e missing data and replace with 0
births['day'].fillna(0, inplace=True) 

births['day'] = births['day'].astype(int)
#create a new column name decade 
births['decade'] = 10 * (births['year'] // 10)
#create a table and group by gender and decade
print(births.pivot_table('births', index='decade', columns='gender', aggfunc='sum'))
print(births.head())

