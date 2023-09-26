# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:07:23 2023

@author: andyc
"""

import numpy as np
import pandas as pd
import seaborn as sns


iris = sns.load_dataset('iris')
iris_details = iris.describe()

spec = iris.groupby('species')
spec_headers = spec.head()
species_details = spec.describe()

sepal_info = pd.DataFrame({'sepal_length':iris['sepal_length'],'sepal_width':iris['sepal_width'],'species':iris['species']})
petal_info = pd.DataFrame({'petal_length':iris['petal_length'],'petal_width':iris['petal_width'],'species':iris['species']})

pd.merge(sepal_info, petal_info, how='inner', right_index=True, left_index=True)

vers = iris[iris['species'] == 'versicolor']
setosa = iris[iris['species'] == 'setosa']
virg = iris[iris['species'] == 'virginica']

vers_and_setosa = pd.concat([vers,setosa], axis=0)



flights = sns.load_dataset('flights')

f_piv = flights.pivot(index='year', columns='month', values='passengers')

f_stack = f_piv.stack()
# Returns a multi-index series from the pivoted table

# To get back to original dataframe use unstack (not pivot)