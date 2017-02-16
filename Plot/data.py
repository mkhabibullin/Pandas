import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_excel("D://python//Data.xlsx", "Лист1")
fig=plt.figure() #Plots in matplotlib reside within a figure object, use plt.figure to create new figure
#Create one or more subplots using add_subplot, because you can't create blank figure

ax = fig.add_subplot(1,1,1)
#Variable

ax.hist(df['Age'],bins = 7) # Here you can play with number of bins
plt.title('Age distribution')
plt.xlabel('Age')
plt.ylabel('#Employee')
plt.show()