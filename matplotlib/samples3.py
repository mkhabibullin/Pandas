# ------------------------
# Loading Data from Files for Matplotlib
# ------------------------
import matplotlib.pyplot as plt
import numpy as np
import os

file_path = os.path.join(os.path.dirname(__file__), "example.txt");

x, y = np.loadtxt(file_path, delimiter=',', unpack=True)

plt.plot(x, y, label='Loaded from file!')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# ------------------------
# Data from the Internet for Matplotlib
# ------------------------
import matplotlib.pyplot as plt
import numpy as np
import urllib
import json

def get_data():
    url_str = 'http://data.gov.ru/opendata/7704221753-unfavorablemeteorologicalconditions/data-20170124T0100.json?encoding=CP1251'
    source_code = urllib.request.urlopen(url_str).read().decode('cp1251')

    source_data = json.loads(source_code)

    data = []

    for line in source_data:
        data.append(line['Year'])

    return data

y = get_data()
x = range(1, len(y) + 1)

plt.plot(x, y, label='Year')
plt.legend()
plt.xlabel('Order')
plt.ylabel('Years')
plt.show()
