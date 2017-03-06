import pandas as pd
import numpy as np
import os
#from tabulate import tabulate
import matplotlib.pyplot as plt

PATH = exelDir = os.path.dirname(os.path.realpath(__file__))

# -----------------------------------------------------------
df = pd.read_excel(PATH + "/sales-funnel.xlsx", "Sheet2")
df.head()

df.plot(kind='bar', x='Index', y='Price')
plt.show()

# -----------------------------------------------------------

df = pd.read_excel(PATH + "/sales-funnel.xlsx", "Stat1")
df.head()

df.plot(x='Year', y=['Count', 'City', 'Other'])
plt.show()