import os
import matplotlib.pyplot as plt
from pandas import read_csv, DataFrame, Series

defaultDir = os.path.dirname(os.path.realpath(__file__))

data = read_csv(defaultDir + '/Data/train.csv')

# По статусам

pivot = data.pivot_table('PassengerId', 'Pclass', 'Survived', 'count')

pivot.plot(kind='bar', stacked=True)
 
plt.show()

# Кол-во родственников

fig, axes = plt.subplots(ncols=2)
data.pivot_table('PassengerId', ['SibSp'], 'Survived', 'count').plot(ax=axes[0], title='SibSp')
data.pivot_table('PassengerId', ['Parch'], 'Survived', 'count').plot(ax=axes[1], title='Parch')

plt.show()

# Номера кают
