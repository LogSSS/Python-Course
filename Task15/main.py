import matplotlib.pyplot as plt
from matplotlib import gridspec
import pandas as pd
import numpy as np

# Task 1

univer = {'MedUn': 1770, 'PNU': 11175, 'KD': 1612, 'IFUNG': 4729}

keys = list(univer.keys())
values = list(univer.values())

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(9, 3), sharey=True)

fig.subplots_adjust(top=0.8)
fig.subplots_adjust(bottom=0.2)

axes[0].plot(keys, values, color='blue', marker='o')
axes[0].set_title('Графік')
axes[0].set_xlabel('Університети')
axes[0].set_ylabel('Кількість студентів')
axes[0].set_facecolor('pink')

axes[1].bar(keys, values, color='green')
axes[1].set_title('Стовпчаста діаграма')
axes[1].set_xlabel('Університети')
axes[1].set_facecolor('blue')

axes[2].scatter(keys, values, color='red', marker='x')
axes[2].set_title('Точковий графік')
axes[2].set_xlabel('Університети')
axes[2].set_facecolor('yellow')

plt.suptitle('Лабораторна робота №7')

plt.tight_layout()
plt.show()

# Task 2

fig = plt.figure()

ax_1 = fig.add_subplot(2, 2, 1)
ax_2 = fig.add_subplot(2, 2, 2)
ax_3 = fig.add_subplot(2, 2, 3)
ax_4 = fig.add_subplot(2, 2, 4)
ax_1.set(title='ax_1', xticks=[], yticks=[], facecolor='green')
ax_2.set(title='ax_2', xticks=[], yticks=[], facecolor='blue')
ax_3.set(title='ax_3', xticks=[], yticks=[], facecolor='gold')
ax_4.set(title='ax_4', xticks=[], yticks=[], facecolor='olive')

plt.show()

# Task 3

fig = plt.figure()

ax_1 = fig.add_subplot(2, 1, 1)
ax_3 = fig.add_subplot(2, 2, 3)
ax_4 = fig.add_subplot(2, 2, 4)
ax_1.set(title='ax_1', xticks=[], yticks=[], facecolor='green')
ax_3.set(title='ax_3', xticks=[], yticks=[], facecolor='gold')
ax_4.set(title='ax_4', xticks=[], yticks=[], facecolor='olive')

plt.show()

# Task 4

fig = plt.figure()

ax_1 = fig.add_subplot(1, 2, 1)
ax_2 = fig.add_subplot(2, 2, 2)
ax_4 = fig.add_subplot(2, 2, 4)
ax_1.set(title='ax_1', xticks=[], yticks=[], facecolor='green')
ax_2.set(title='ax_2', xticks=[], yticks=[], facecolor='blue')
ax_4.set(title='ax_4', xticks=[], yticks=[], facecolor='olive')

plt.show()

# Task 5

fig = plt.figure()
ax_1 = fig.add_subplot(3, 3, 1)
ax_2 = fig.add_subplot(3, 2, 3)
ax_3 = fig.add_subplot(3, 1, 3)

plt.show()

# Task 6

plt.figure(figsize=(6, 4))

G = gridspec.GridSpec(3, 3)

ax_1 = plt.subplot(G[:, 0])
ax_1.set(title='ax_1', xticks=[], yticks=[], facecolor='green')
ax_2 = plt.subplot(G[:-1, 1])
ax_2.set(title='ax_2', xticks=[], yticks=[], facecolor='blue')
ax_3 = plt.subplot(G[0, -1])
ax_3.set(title='ax_3', xticks=[], yticks=[], facecolor='gold')
ax_4 = plt.subplot(G[1, -1])
ax_4.set(title='ax_4', xticks=[], yticks=[], facecolor='olive')
ax_5 = plt.subplot(G[-1, -2:])
ax_5.set(title='ax_5', xticks=[], yticks=[], facecolor='pink')

plt.show()

# # Task 7

data = pd.read_csv('NationalNames.csv')

data1 = data[(data['Year'] >= 1980) & (data['Year'] <= 1989)].groupby('Year')['Count'].sum()
data2 = data[(data['Year'] >= 1990) & (data['Year'] <= 1999)].groupby('Year')['Count'].sum()

plt.style.use('ggplot')
fig = plt.figure()

ax_1 = fig.add_subplot(2, 2, 1)
ax_2 = fig.add_subplot(2, 2, 2)
ax_3 = fig.add_subplot(2, 1, 2)

rects = ax_1.bar(data1.index, data1, color='indigo')
for rect in rects:
    height = rect.get_height()
    ax_1.text(rect.get_x() + rect.get_width() / 2., 0.35 * height,
              '%d' % round(int(height), -4),
              ha='center', va='bottom', color='white', rotation=90)
ax_1.set_title('1980-1990')
ax_1.set_xticks(data1.index[::2])

rects = ax_2.bar(data2.index, data2.values, color='blue')
for rect in rects:
    height = rect.get_height()
    ax_2.text(rect.get_x() + rect.get_width() / 2., 0.35 * height,
              '%d' % round(int(height), -4),
              ha='center', va='bottom', color='white', rotation=90)
ax_2.set_title('1990-2000')
ax_2.set_xticks(data2.index[::2])

ax_3.bar(np.arange(len(data1)) - 0.2, data1, color='indigo', width=0.4, label='1980-1990')
ax_3.bar(np.arange(len(data2)) + 0.2, data2, color='red', width=0.4, label='1990-2000')
ax_3.locator_params(axis='x', nbins=20)
ax_3.set_ylim([0, 5500000])
ax_3.legend()
ax_3.legend(bbox_to_anchor=(0.4, 0.7))
ax_3.set_title('Comparison')

fig.text(0.04, 0.5, 'Count', va='center', rotation='vertical')

plt.subplots_adjust(wspace=0.2, hspace=0.5)

plt.suptitle('Лабораторна робота №7')

plt.show()

# EXTRA

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))

x = np.arange(-5, 5, 0.1)

ax_1 = fig.add_subplot(2, 2, 1)
ax_2 = fig.add_subplot(2, 2, 2)
ax_3 = fig.add_subplot(2, 2, 3)
ax_4 = fig.add_subplot(2, 2, 4)

ax_1.plot(x, np.sin(x))
ax_2.plot(x, np.cos(x))
ax_3.plot(x, np.sin(2 * x))
ax_4.plot(x, np.sin(x / 2))

for ax in fig.get_axes():
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.show()
