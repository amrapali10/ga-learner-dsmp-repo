# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Code starts here
data = pd.read_csv(path)
sns.distplot(data['Rating'].dropna())

data = data[data['Rating'] <= 5]
#print(data.head())
sns.distplot(data['Rating'])
plt.show()


#Code ends here


# --------------
# code starts here

total_null = data.isnull().sum()
percent_null = (total_null/data.isnull().count())
missing_data = pd.concat([total_null, percent_null], axis=1, keys=['Total','Percentage'])
print(missing_data)
data.dropna(inplace=True)
total_null_1 = data.isnull().sum()
percent_null_1 = (total_null_1/data.isnull().count())
missing_data_1 = pd.concat([total_null_1, percent_null_1], axis=1,keys=['Total','Percentage'] )
print(missing_data_1)
# code ends here


# --------------

#Code starts here
ax = sns.catplot(x='Category', y='Rating', data=data, kind='box', height = 10)
ax.set_xticklabels(rotation=90)
plt.title('Rating vs Category [BoxPlot]')
#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print(data['Installs'].value_counts())
data['Installs'] = data['Installs'].str.replace(',','')
data['Installs'] = data['Installs'].str.replace('+','')
print(data['Installs'].value_counts())
data['Installs'] = data['Installs'].astype(int)

le = LabelEncoder()
le.fit(data['Installs'])
data['Installs'] = le.transform(data['Installs'])
r = sns.regplot(x='Installs', y = 'Rating', data = data)
r.set_title('Rating vs Installs [RegPlot]')

#Code ends here



# --------------
#Code starts here
print(data['Price'].value_counts())
data['Price'] = data['Price'].str.replace('$','')
data['Price'] = data['Price'].astype(float)
r = sns.regplot(x='Price', y='Rating', data = data)
r.set_title('Rating vs Price [RegPlot]')

#Code ends here


# --------------

#Code starts here

se = pd.Series(data['Genres'], name = 'Genres')
print(se.unique())
data['Genres'] = data['Genres'].str.split(';', expand = True)
#print(data['Genres'])
gr_mean = data.groupby(['Genres'], as_index=False)['Rating'].mean()
print(gr_mean.describe())
gr_mean = gr_mean.sort_values('Rating',ascending=True)
#print(gr_mean)
print(gr_mean.loc[14], gr_mean.loc[18])

#Code ends here


# --------------

#Code starts here
#print(data['Last Updated'])
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
#print(data['Last Updated'])
max_date = data['Last Updated'].max()
print(max_date)
data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days
#print(data['Last Updated Days'].head())
sns.regplot(x = 'Last Updated Days', y='Rating', data=data)
plt.title('Rating vs Last Updated [RegPlot]')
plt.show()
#Code ends here


