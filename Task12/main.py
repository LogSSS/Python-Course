import numpy as np
import pandas as pd

# 1
data = pd.read_csv("lab4.csv", delimiter=',', index_col=0)

# 2
print("-" * 30)
print(f"(Rows, Columns) in data: {data.shape}")

# 3
print("-" * 30)
print(f"List of names of columns: {data.columns.tolist()}")

# 4
print("-" * 30)
print(f"List of types if columns:\n{data.dtypes}")

# 5
print("-" * 30)
print(f"Count of unique murder places: {data['AREA NAME'].nunique()}")
print(f"Count of unique murdered GENDERS: {data['Vict Sex'].nunique()}")

# 6
print("-" * 30)
print(f"Count of NAN in columns:\n{data.isna().sum()}")
data.isna().fillna(0)

# 7
print("-" * 30)
print(f"Statistic according to age:\n{data['Vict Age'].describe()}")

# 8
print("-" * 30)
data.drop(columns='Vict Descent', inplace=True)
print("Deleted 'Visct Descent' column")

# 9
print("-" * 30)
data['Vict Sex'] = data['Vict Sex'].replace('X', np.NaN)
print("Replace 'X' to 'NaN' in 'Vict Sex' column")

# 10
print("-" * 30)
data['Date Rptd'] = data['Date Rptd'].apply(pd.to_datetime)
print("For 'Date Rtpd' applied datetime")

# 11
print("-" * 30)
data['Year'] = data['Date Rptd'].dt.year
data['Month'] = data['Date Rptd'].dt.strftime('%m')
print("Created column 'Year' and 'Month' with data")

# 12
print("-" * 30)
data.drop(columns='Date Rptd', inplace=True)
print("Column 'Date Rptd' deleted")

# 13
print("-" * 30)
if len(data['Year'].unique()) == 1:
    data.drop(columns='Year', inplace=True)
    print("Column 'Year' DROPPED")
else:
    print("Detected unique data in 'Year'")

# 14
print("-" * 30)
data = data.loc[data['Crm Cd Desc'].notnull()]
print("Dropped rows where null in 'Crm Cd Desc'")
print(f"Is cells with null values: {data[data['Crm Cd Desc'].isnull()]}")

# 15
print("-" * 30)
victim = data[['Crm Cd Desc', 'Vict Age', 'Vict Sex']].copy()
print("Copied 'Crm Cd Desc', 'Vict Age', 'Vict Sex' to victim")

# 16
print("-" * 30)
print(f"Count of unique data in 'Crm Cd Desc': {victim['Crm Cd Desc'].nunique()}")

# 17
print("-" * 30)
print(f"Value counts of 'Crm Cd Desc': {victim['Crm Cd Desc'].value_counts()}")

# 18
print("-" * 30)
print(f"Most often crime: {victim['Crm Cd Desc'].value_counts().index[0]}")

# 19
print("-" * 30)
print(f"Most often victims age: {victim['Vict Age'].value_counts().index[1:5]}")

# 20
print("-" * 30)
print(f"Count of 'Robbery' crimes: {victim['Crm Cd Desc'].value_counts().get('ROBBERY', 0)}")

# 21
print("-" * 30)
print(
    f"Count of 'M' victims: {victim[victim['Crm Cd Desc'] == 'ROBBERY']['Vict Sex'].value_counts().get('M', 0)}")

# 22
print("-" * 30)
print(
    "Count of 'VEHICLE - ATTEMPT STOLEN' or 'VEHICLE - STOLEN': "
    f"{len(victim[victim['Crm Cd Desc']
           .isin(['VEHICLE - ATTEMPT STOLEN',
                  'VEHICLE - STOLEN'])])}")

# 23
print("-" * 30)
print(
    "Count of 'VEHICLE - ATTEMPT STOLEN' or 'VEHICLE - STOLEN' to count of rows in victim: "
    f"{(len(victim[victim['Crm Cd Desc']
            .isin(['VEHICLE - ATTEMPT STOLEN',
                   'VEHICLE - STOLEN'])]) / len(victim)) * 100} %")

# 24
print("-" * 30)
bob = len(victim[victim['Crm Cd Desc'].str.contains(r'\bWEAPON')])
print(f"Count crimes with WEAPON: {bob}\n"
      f"Count crimes with WEAPON to count of rows in victim: {(bob / len(victim)) * 100} %")
# 25
print("-" * 30)
print(f"Unique crimes with WEAPON: {victim[victim['Crm Cd Desc'].str.contains(r'\bWEAPON')]['Crm Cd Desc'].unique()}")

# 26
print("-" * 30)
print(
    f"Is WIMEN more often become victims than Mens: {victim['Vict Sex'].value_counts().get('M', 0)
                                                     < victim['Vict Sex'].value_counts().get('W', 0)}")

# 27
print("-" * 30)
print(
    "In which crime most often became WIMEN: "
    f"{victim[victim['Vict Sex'] == 'F']['Crm Cd Desc'].value_counts().idxmax()}")

# 28
print("-" * 30)
vict = data[['Crm Cd Desc', 'Vict Sex']].copy()
print("Copied 'Crm Cd Desc', 'Vict Sex' to vict")

# 29
print("-" * 30)
print(f"Victim count by gender:  {vict.groupby('Vict Sex')['Crm Cd Desc'].count()}")

# 30
print("-" * 30)
print("Female victims counts by crime type: "
      f"{vict[vict['Vict Sex'] == 'F'].groupby('Crm Cd Desc')['Vict Sex'].count()}")

# 31
print("-" * 30)
print(f"Maximum number of victims: {vict.groupby('Crm Cd Desc')['Vict Sex'].count().max()}")

# 32
print("-" * 30)
print("Crime type with the maximum number of victims in each group: "
      f"{vict.groupby('Crm Cd Desc')['Vict Sex'].count().idxmax()}")

# 33
print("-" * 30)
print("Maximum age of victims for each crime: "
      f"{victim.groupby('Crm Cd Desc')['Vict Age'].max()}")

# 34
print("-" * 30)
Zv = data.pivot_table(values='Vict Sex', index='Month', columns='Crm Cd Desc', aggfunc=np.count_nonzero)
print(f"Pivot table:\n{Zv}")

# 35
print("-" * 30)
print(f"Pivot table for the 'ROBBERY' crime:\n{Zv[['ROBBERY']]}")

# 36
print("-" * 30)
print(f"Maximum number of robberies in a month: {Zv['ROBBERY'].max()}")

# 37
print("-" * 30)
print("Filtered pivot table with rows where at least one crime was committed:\n"
      f"{Zv.dropna(axis=1)}")

# 38
print("-" * 30)
print("Crime names in the filtered pivot table:"
      f"{Zv.dropna(axis=1).columns.to_list()}")
