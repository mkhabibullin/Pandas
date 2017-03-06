import pandas as pd
import numpy as np
import os
#from tabulate import tabulate
import matplotlib.pyplot as plt

PATH = exelDir = os.path.dirname(os.path.realpath(__file__))

mainDataFile = PATH + "/sales-funnel.xlsx"

# -----------------------------------------------------------
df = pd.read_excel(mainDataFile, "Sheet2")
df.head()

df.plot(kind='bar', x='Index', y='Price')
plt.show()

# -----------------------------------------------------------
# Численность населения(городское\сельское)
# -----------------------------------------------------------

df = pd.read_excel(mainDataFile, "Stat1")

df.plot(x='Year', y=['Count', 'City', 'Other'])
plt.show()

# -----------------------------------------------------------
# Браки\разводы
# -----------------------------------------------------------

df = pd.read_excel(mainDataFile, "Brak")

df.plot(x="Year", y=["Brak", "Razvod"])
plt.grid(True)
plt.show()
