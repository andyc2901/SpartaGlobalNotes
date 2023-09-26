# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 10:21:27 2023

@author: andyc
"""

import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')

#sns.jointplot(data = iris, x = 'sepal_width', y = 'sepal_length')

#sns.pairplot(data = iris, hue='species')

flights = sns.load_dataset('flights')

plt.figure()

f_piv = flights.pivot(index='year', columns='month', values='passengers')

sns.heatmap(f_piv)

# plt.pie
# plt.show

# doughnut charts

plt.figure()

data = [15,10,3,30,12]
plt.pie(data)
circle = plt.Circle((0,0), 0.7, color='white')
plt.plot(circle)