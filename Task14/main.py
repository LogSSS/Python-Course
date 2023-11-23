import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1
x = np.linspace(-5, 5, 400)

y1 = (136 - 4.2 * x) / 10
y2 = (132 + 10.1 * x) / 13.8
y3 = (18.3 * x + 108) / 7.6

plt.figure(figsize=(7, 7))

plt.plot(x, y1, color='red', linestyle='dashdot', label='4.2x + 10y = 136')
plt.plot(x, y2, color='blue', linestyle='dotted', label='10.1x - 13.8y = -132')
plt.plot(x, y3, color='green', linestyle='dashed', label='18.3x - 7.6y = -108')

plt.grid(True, alpha=0.6)

plt.text(0.8, y1[0] - 3, '$4.2x + 10y = 136$', color='red', rotation=-13)
plt.text(-1, y2[0] + 2, '$4.2x_1 + 10x_2 = 136$', color='blue', rotation=18)
plt.text(-3, y3[0] + 6, '$18.3x - 7.6y = -108$', color='green', rotation=45)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Intersection of Lines')

plt.legend()

plt.fill_between(x, y2, np.minimum(y1, y3), where=(x < 3.4) & (x > -2.8), color='grey')

plt.show()

# 2
data = pd.read_csv("KN-4.csv", delimiter=';')

fig, ax = plt.subplots()
bars = ax.bar(data['Student'][data['KR1'].notna()], data['KR1'][data['KR1'].notna()], color='blue')

plt.xticks(rotation=45, ha='right')

plt.xlabel('Students')
plt.ylabel('KR Results')
plt.title('KR Results for Students')

for bar in bars:
    val = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, val, round(val, 2), ha='center', va='bottom')

plt.subplots_adjust(bottom=0.3)

plt.show()

# 3
vict = pd.read_csv("lab4.csv", delimiter=',')

labels = ['Female', 'Male']
sizes = [len(vict[vict['Vict Sex'] == 'F']), len(vict[vict['Vict Sex'] == 'M'])]
colors = ['lightcoral', 'lightskyblue']
explode = (0.1, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Victim Genders')
plt.show()
