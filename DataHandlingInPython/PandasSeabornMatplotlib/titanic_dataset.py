# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 16:13:15 2023

@author: andyc
"""

import numpy as np
import pandas as pd
import seaborn as sns

#Load dataset
titanic = sns.load_dataset('titanic')

#Drop unnecessary rows
titanic = titanic.drop(['embark_town','class','alone','alive','deck'],
                       axis = 1)

#Check for duplicate data:
titanic_dupe = titanic[titanic.duplicated(keep=False)]
#lots of duplicated data but probably due to number of passengers
#with the same details, not passengers entered twice

#Round age to an integer

titanic['age'] = round(titanic['age'])
'''
# Find avg age
avg_age = round(titanic['age'].mean())
# Replace nan in age with average age
titanic['age'] = titanic['age'].fillna(avg_age)
'''

#'''

# Make an array of rows that are index man, then fillna for those rows???

#Find average age for men, women and children to fill in where nan
men = titanic[titanic['who'] == 'man']
men_index = np.array(men.index)
avg_men_age = round(men['age'].mean())
titanic.loc[men_index,'age'] = titanic.loc[men_index,'age'].fillna(avg_men_age)

child = titanic[titanic['who'] == 'child']
avg_child_age = round(child['age'].mean())
child_index = np.array(child.index)
titanic.loc[child_index,'age'] = titanic.loc[child_index,'age'].fillna(avg_child_age)

women = titanic[titanic['who'] == 'woman']
avg_women_age = round(women['age'].mean())
women_index = np.array(women.index)
titanic.loc[women_index,'age'] = titanic.loc[women_index,'age'].fillna(avg_women_age)

#Need to work out how to replace men with nan as avg_men_age

#titanic.loc[:,['age','who']].fillna(avg_men_age)
#titanic = titanic[titanic['who'] == 'woman'].fillna(avg_women_age)
#titanic = titanic[titanic['who'] == 'child'].fillna(avg_child_age)
#'''

# Check for any further nans
nan_counts = titanic.isna().sum()
# 2 nans in embarked, use mode to fill those

mode_embark = titanic['embarked'].mode()
titanic['embarked'] = titanic['embarked'].fillna(mode_embark[0])

# Check for any further nans
nan_counts = titanic.isna().sum()

first_class = titanic[titanic['pclass'] == 1]
second_class = titanic[titanic['pclass'] == 2]
third_class = titanic[titanic['pclass'] == 3]





