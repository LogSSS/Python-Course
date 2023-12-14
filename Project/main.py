import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import numpy as np

# data
data = pd.read_csv("vgsales.csv")

# 2
print("-" * 30)
print("Information about the data:")
print(f"Data types:\n{data.dtypes}")

print("-" * 30)
print(f"Head:\n{data.head()}")

print("-" * 30)
print(f"Columns:\n{data.columns}")

print("-" * 30)
print(f"Shape:\n{data.shape}")

print("-" * 30)
print(f"Empty cells:\n{data.isnull().sum()}")

print("-" * 30)
print(f"Unique values:\n{data.nunique()}")

print("-" * 30)
print(f"Describe:\n{data.describe()}")

print("-" * 30)
print(f"Missing ranks: {list(set(range(1, data['Rank'].max() + 1)) - set(data['Rank']))}")

# 3
print("-" * 30)
print("Delete rows with empty cells:")
data = data.dropna(subset=['Year'])

print("-" * 30)
print("Set 'Year' type to int:")
data['Year'] = data['Year'].astype(int)

print("-" * 30)
print("Replace empty cells with 'nil':")
data = data.fillna("nil")

frame1 = data[['Name', 'Platform', 'Year', 'Genre', 'Publisher']]
frame2 = data[['Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']]
frame3 = data.groupby('Publisher')['Global_Sales'].sum().reset_index()

# 4
print("-" * 30)
print(f"All platforms:\n{frame1['Platform'].unique()}")

print("-" * 30)
print(f"Platforms count:\n{len(frame1['Platform'].unique())}")

print("-" * 30)
print(f"Most popular platform:\n{frame1['Platform'].value_counts().idxmax()}")

print("-" * 30)
print(
    f"Count of games from Valve:\n{frame1[frame1['Publisher'] == 'Valve Software']['Name'].count() +
                                   frame1[frame1['Publisher'] == 'Valve']['Name'].count()}")

print("-" * 30)
print(f"Games from 2007 year:\n{frame1[frame1['Year'] == 2007]['Name']}")

print("-" * 30)
print(f"Games from 2003 to 2009 years:\n{frame1[(frame1['Year'] >= 2003) & (frame1['Year'] <= 2009)]['Name']}")

print("-" * 30)
print(f"Games in 2014 on PC:\n{frame1[(frame1['Year'] == 2014) & (frame1['Platform'] == 'PC')]['Name']}")

print("-" * 30)
print(f"5 most popular genres:\n{frame1['Genre'].value_counts().head()}")

print("-" * 30)
print(f"How many 'Action' games in dataset:\n{frame1[frame1['Genre'] == 'Action']['Name'].count()}")

print("-" * 30)
print(
    "How many 'Assassin's Creed' games in dataset:\n"
    f"{frame1[frame1['Name'].str.contains('Assassin\'s Creed')]['Name'].count()}")

print("-" * 30)
print(f"Total sales in NA:\n{frame2['NA_Sales'].sum()}")

print("-" * 30)
print(f"Total sales in EU on PC:\n{frame2[(frame2['Platform'] == 'PC')]['EU_Sales'].sum()}")

print("-" * 30)
print(f"Best sales region:\n{frame2[['NA_Sales', 'EU_Sales', 'JP_Sales']].sum().idxmax()}")

print("-" * 30)
print(f"Best sales region for 'Role-Playing' games:\n"
      f"{frame2[frame2['Genre'] == 'Role-Playing'][['NA_Sales', 'EU_Sales', 'JP_Sales']].sum().idxmax()}")

print("-" * 30)
print(f"Sum of sales for each genre:\n"
      f"{frame2.groupby("Genre").agg({
          'NA_Sales': 'sum',
          'EU_Sales': 'sum',
          'JP_Sales': 'sum',
          'Other_Sales': 'sum'
      }).reset_index()}")

print("-" * 30)
print(
    "Years with average sales more than 0.15 in EU:"
    f"{frame2.groupby("Year")['EU_Sales'].mean().index[frame2.groupby("Year")['EU_Sales'].mean() >
                                                       0.15].tolist()}")

print("-" * 30)
print(f"First 5 genres with the highest sales in NA:\n" f"{frame2.groupby("Genre")['NA_Sales'].sum().head()}")

print("-" * 30)
print(f"Which game is in 128 place all info:\n{frame2.iloc[127]}")

print("-" * 30)
print(f"How much does each Publisher earn in each region:\n{frame2.groupby("Publisher").agg(
    {'NA_Sales': 'sum', 'EU_Sales': 'sum', 'JP_Sales': 'sum', 'Other_Sales': 'sum'})}")

print("-" * 30)
print(f"Which year was the best for Nintendo in EU:\n"
      f"{frame2[frame2['Publisher'] == 'Nintendo'].groupby('Year')['EU_Sales'].sum().idxmax()}")

print("-" * 30)
print(f"Publisher with the highest sales:\n{frame3[frame3['Global_Sales'] == frame3['Global_Sales'].max()]}")

print("-" * 30)
print(f"Publisher with the lowest sales:\n{frame3[frame3['Global_Sales'] == frame3['Global_Sales'].min()]}")

print("-" * 30)
print(f"The Publishers with sales more than 10 million:\n"
      f"{frame3[frame3['Global_Sales'] > 10]}")

# 5
print("-" * 30)
genre_data = data.groupby('Genre').agg({'Global_Sales': 'sum', 'Genre': 'count'}).sort_values(by='Global_Sales',
                                                                                              ascending=False)
plt.figure(figsize=(12, 8))
bars = plt.bar(genre_data.index, genre_data['Global_Sales'], color='blue')
plt.xlabel('Genre')
plt.ylabel('Total Global Sales (in millions)')
plt.title('Total Global Sales by Genre')

for bar, count in zip(bars, genre_data['Genre']):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, f'{count}',
             ha='center', va='center', color='white', fontsize=10)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

##
platform_counts = data['Platform'].value_counts()

platform_percentages = platform_counts / platform_counts.sum() * 100

other_platforms = platform_percentages[platform_percentages < 2]
platform_counts['Other'] = platform_counts[other_platforms.index].sum()
platform_counts = platform_counts.drop(other_platforms.index)

plt.figure(figsize=(10, 10))
plt.pie(platform_counts, labels=platform_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20c.colors,
        wedgeprops=dict(width=0.4))

centre_circle = plt.Circle((0, 0), 0.6, color='white', linewidth=0.8)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Distribution of Games by Platform', fontsize=16)
plt.legend(platform_counts.index, loc='upper right', bbox_to_anchor=(1.14, 1))
plt.show()

##
top_platforms = data['Platform'].value_counts().head(10).index

top_data = data[data['Platform'].isin(top_platforms)]

plt.scatter(top_data['Year'], top_data['Platform'], marker='.', color='orange', alpha=0.7)

plt.yticks(top_platforms)

plt.xlabel('Year')
plt.ylabel('Platform')
plt.title('Top 10 Platforms - Dotted Plot of Year vs Platform')

plt.show()

##
unique_years = data['Year'].unique()

x = []
y = []
y2 = []

fig, ax = plt.subplots(figsize=(16, 12))

fig.text(0.5, 0.04, 'Year', ha='center', fontsize=14)
fig.text(0.04, 0.5, 'Total Games Released from TOP', va='center', rotation='vertical', fontsize=14)


def animate(i):
    year = unique_years[i]
    subset_data = data[data['Year'] == year]

    x.append(year)
    y.append(len(subset_data))

    avg = sum(y[1:]) / len(y[1:]) if len(y) > 1 else len(data[data['Year'] == unique_years[0]])

    y2.append(avg)

    ax.clear()
    bars = ax.bar(x, y, color='mediumorchid', align='edge')

    ax.plot(range(0, i + 2), [avg] * (i + 2), lw=3, color='black', zorder=2)

    ax.bar_label(bars)
    ax.tick_params(labelrotation=90)
    ax.set_xlim([min(unique_years), max(unique_years)])
    ax.set_ylim([0, max(y)])
    ax.spines['top'].set_color(None)
    ax.spines['right'].set_color(None)

    fig.suptitle('Mid: ' + str(round(avg, 2)), fontsize=16)
    fig.subplots_adjust(bottom=0.2)


ani = FuncAnimation(fig, animate, frames=len(unique_years), interval=400, repeat=False)
plt.show()

writer = animation.PillowWriter(fps=5, metadata=dict(artist="Nazar Shkvarok"), bitrate=1800)
ani.save('bob_1.gif', writer=writer)

##
genre_counts = data['Genre'].value_counts()

fig, ax = plt.subplots()

explode = [0.2] * len(genre_counts)
cmap = plt.get_cmap("tab20c")
num_colors = len(genre_counts.index)
colors = cmap(np.arange(num_colors) * 2)


def animate(i):
    ax.clear()

    counts = genre_counts.values
    labels = genre_counts.index

    explode[i % len(explode)] = 0
    colors[i % num_colors] = cmap(i % num_colors)

    ax.pie(counts, labels=labels, explode=explode, autopct='%1.1f%%',
           wedgeprops={"edgecolor": "k", 'linewidth': 1, 'linestyle': 'solid', 'antialiased': True},
           textprops={'fontsize': 14}, shadow=True, startangle=25, colors=colors)

    explode[i % len(explode)] = 0
    ax.legend(bbox_to_anchor=(1.4, 0.5), loc="center left")
    ax.set_title('Distribution of Video Game Genres')


plt.subplots_adjust(right=0.6, left=0.15, top=0.85, bottom=0.15)

ani = FuncAnimation(fig, animate, frames=len(explode), interval=560, repeat=False)
plt.show()

ani.save('bob_2.gif', writer=writer)
