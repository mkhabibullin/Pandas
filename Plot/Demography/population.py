import matplotlib.pyplot as plt
import pandas as pd
import os

exelDir = os.path.dirname(os.path.realpath(__file__))

df=pd.read_excel(exelDir + "//Data.xls", "Лист3")
fig=plt.figure() #Plots in matplotlib reside within a figure object, use plt.figure to create new figure
#Create one or more subplots using add_subplot, because you can't create blank figure

ax = fig.add_subplot(1,1,1)
#Variable

ax.hist(df['x3'],bins = 16) # Here you can play with number of bins
plt.title('Age distribution')
plt.xlabel('Года')
plt.ylabel('Кол-во')
plt.show()