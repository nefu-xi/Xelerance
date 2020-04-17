import pandas as pd
data = pd.read_csv('address.csv')
#data.head()
mask = data.loc[:,'Province'] == 'Ontario'
#1. with 'First name' and 'Last name' header
#residents_ON = data.loc[:,['First name','Last name']][mask]
#2. without 'First name' and 'Last name' header, only full name
#residents_ON = data.loc[:,'First name'][mask] + ' ' + data.loc[:,'Last name'][mask]
#3. with all information of ontario residents
residents_ON = data.loc[mask]
print(residents_ON)