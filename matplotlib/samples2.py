# ---------------------------------
# Scatter Plots with Matplotlib
# ---------------------------------
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y, label='skitscat', color='k', s=25, marker='o')#http://matplotlib.org/api/markers_api.html

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter plot')

plt.legend()
plt.show()

# ---------------------------------
# Stack Plots with Matplotlib
# ---------------------------------
import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating =   [2,3,4,3,2]
working =  [7,8,7,2,2]
playing =  [8,5,7,8,13]

plt.stackplot(days, sleeping, eating, working, playing, colors=['m','c','r','b'], labels=['sleeping','eating','working','playing'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Stack Plots')
plt.legend()
plt.show()

# ---------------------------
# Pie Charts with Matplotlib
# ---------------------------
import matplotlib.pyplot as plt

slices = [7,2,2,13]

activites = ['sleeping', 'eating', 'working', 'playing']
colors = ['m','c','r','b']

plt.pie(slices,
    labels=activites,
    colors=colors,
    startangle=90,
    shadow=True,
    explode=(0, 0.1, 0, 0),
    autopct='%1.1f%%')

plt.title('Pie Charts')
plt.show()