import pandas as pd
import numpy as np
import os
from tabulate import tabulate
import matplotlib.pyplot as plt

PATH = exelDir = os.path.dirname(os.path.realpath(__file__))

df = pd.read_excel(PATH + "/sales-funnel.xlsx")
df.head()

df['Status'] = df['Status'].astype('category')
df["Status"].cat.set_categories(["won","pending","presented","declined"],inplace=True)

print(tabulate(df, headers='keys', tablefmt='psql'))

output = pd.pivot_table(df, index=["Name"])
print(output)
#.plot(kind='bar', stacked=True)
# plt.show()