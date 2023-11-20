import pandas as pd

# data
data = pd.read_csv('NationalNames.csv')

# 1
print('-' * 30)
print(data.head(8))

# 2
print('-' * 30)
print(data.tail(8))

# 3
print('-' * 30)
print(data.columns)

# 4
print('-' * 30)
print(data.describe())

# 5
print('-' * 30)
print(len(data['Name'].unique()))

# 6
print('-' * 30)
print(data[(data['Year'] == 2010) & (data['Gender'] == 'M')].groupby(['Id', 'Name', 'Year', 'Gender'])[
          'Count'].sum().sort_values(ascending=False).head(5))

# 7
print('-' * 30)
print(data['Year'].nunique())

# 8
print('-' * 30)
print(data[data['Count'] == data['Count'].min()].shape[0])

# 9
print('-' * 30)
print(data[(data['Name'] == 'Barbara') & (data['Gender'] == 'M')]['Count'].sum())

# 10
print('-' * 30)
print(len(set(data[data['Gender'] == 'F']['Name']).intersection(set(data[data['Gender'] == 'M']['Name']))))

# 11
print('-' * 30)
print(data.groupby('Year')['Name'].nunique())

# 12
print('-' * 30)
print(data.groupby('Year')['Name'].nunique().reset_index().sort_values(by='Name', ascending=False).head(1))

# 13
print('-' * 30)
print(data[data['Year'] == 2008].groupby('Name')['Count'].sum().idxmax())

# 14
print('-' * 30)
print(data.groupby('Year')['Count'].sum())

# 15
print('-' * 30)
print(data.groupby('Year')['Count'].sum().idxmax())

# 16
print('-' * 30)
print(data.groupby(['Year', 'Gender']).agg({'Count': 'sum'}).unstack('Gender', fill_value=0))

# 17
print('-' * 30)
print((data.groupby(['Year', 'Gender']).agg({'Count': 'sum'}).unstack('Gender', fill_value=0)['Count', 'F'] >
       data.groupby(['Year', 'Gender']).agg({'Count': 'sum'}).unstack('Gender', fill_value=0)['Count', 'M']).sum())
