# --------------------------------------
# Subplots
# --------------------------------------
import matplotlib.pyplot as plt
from matplotlib import style
import random

#vstyle.use('fivethirtyeight')

fig = plt.figure()

def get_data():
    xs = []
    ys = []

    for i in range(10):
        xs.append(i)
        ys.append(random.randrange(10))

    return xs, ys

ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(212)

x,y = get_data()

ax1.plot(x, y)

x,y = get_data()
ax2.plot(x, y)

x,y = get_data()
ax3.bar(x, y)

plt.legend()
plt.show()