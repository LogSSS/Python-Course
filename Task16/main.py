import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

# Task 1
x = np.linspace(2, 15, 400)

y1 = (136 - 4.2 * x) / 10
y2 = (132 + 10.1 * x) / 13.8
y3 = (18.3 * x - 108) / 7.6

fig, ax = plt.subplots()

line1, = ax.plot([], [], color='red', linestyle='dashdot', label='4.2x + 10y = 136')
line2, = ax.plot([], [], color='blue', linestyle='dotted', label='10.1x - 13.8y = -132')
line3, = ax.plot([], [], color='green', linestyle='dashed', label='18.3x - 7.6y = 108')

ax.set_xlim(2, 15)
ax.set_ylim(8, 25)


def animate(frame):
    line1.set_data(x[:frame], y1[:frame])
    line2.set_data(x[:frame], y2[:frame])
    line3.set_data(x[:frame], y3[:frame])


ani = FuncAnimation(fig, animate, frames=len(x), interval=30, repeat=False)  # Adjust interval

plt.text(5, 9, '$4.2x + 10y = 136$', color='red', rotation=-12)
plt.text(7, 15.5, '$4.2x_1 + 10x_2 = 136$', color='blue', rotation=21)
plt.text(11, 11, '$18.3x - 7.6y = 108$', color='green', rotation=55)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Intersection of Lines')

plt.legend()

plt.fill_between(x, y2, np.maximum(y1, y3), where=(x < 14.2) & (x > 3.5), color='grey')

writer = animation.PillowWriter(fps=30, metadata=dict(artist="Nazar Shkvarok"), bitrate=1800)
plt.show()
ani.save('task1.gif', writer=writer)

# Task 2
fig, ax = plt.subplots()
ex = [0.2] * 5

data = pd.read_csv('kn.csv', delimiter=';')

stud_test = data['Test1'].value_counts()

cmap = plt.get_cmap("tab20c")
color = cmap(np.arange(len(stud_test.index)) * 2)
colors = [color[-1]] * len(stud_test.index)


def animate(i):
    ax.clear()

    grades = stud_test.index
    counts = stud_test.values

    ex[i % len(ex)] = 0
    colors[i % len(colors)] = color[i % len(color)]

    ax.pie(counts, labels=grades, explode=ex, autopct='%1.1f%%',
           wedgeprops={"edgecolor": "k", 'linewidth': 1, 'linestyle': 'solid', 'antialiased': True},
           textprops={'fontsize': 14}, shadow=True, startangle=25, colors=colors)

    ex[i % len(ex)] = 0

    ax.legend(bbox_to_anchor=(0.85, 1.025), loc="upper left")

    ax.set_title('Distribution of Test1 Grades')


ani = FuncAnimation(fig, animate, frames=len(ex), interval=560, repeat=False)
writer = animation.PillowWriter(fps=5, metadata=dict(artist="Nazar Shkvarok"), bitrate=1800)

ani.save('task2.gif', writer=writer)
plt.show()

# Task 3
data = pd.read_csv('kn.csv', delimiter=';')

x = []
y = []
y2 = []

fig, ax = plt.subplots()


def animate(i):
    x.append(data.iloc[i]['Student'])
    y.append(data.iloc[i]['KR-6'])

    avg = sum(y[1:]) / len(y[1:]) if len(y) > 1 else data.iloc[0]['KR-6']

    y2.append(avg)

    ax.clear()
    bars = ax.bar(x, y, color='mediumorchid', align='edge')

    ax.plot(range(0, i + 2), [avg] * (i + 2), lw=3, color='black')

    ax.bar_label(bars)
    ax.tick_params(labelrotation=90)
    ax.set_xlim([0, len(data)])
    ax.set_ylim([0, max(data['KR-6'])])
    ax.spines['top'].set_color(None)
    ax.spines['right'].set_color(None)

    fig.suptitle('Mid: ' + str(round(avg, 2)), fontsize=16)
    fig.subplots_adjust(bottom=0.2)


ani = FuncAnimation(fig, animate, frames=len(data), interval=400, repeat=False)
plt.show()

writer = animation.PillowWriter(fps=5, metadata=dict(artist="Nazar Shkvarok"), bitrate=1800)
ani.save('task3.gif', writer=writer)
