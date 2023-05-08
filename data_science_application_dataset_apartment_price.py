# -*- coding: utf-8 -*-
"""Data_Science_Application_Dataset_Apartment_Price.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Crxw90E7uiGjEFFhsF305gO86e1mGfBl

**import the libraries**
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""**Import the database**"""

df = pd.read_excel('https://github.com/MCAGoncalves/dataset/blob/main/Base_Apartment_Price.xlsx?raw=true')

"""**Database Informatione**"""

df.info()

df.head()

"""**Univariate Analysis**"""

#Generating the Histogram
df['Price'].hist()
plt.xlabel("Apartment Price")
plt.ylabel("Frequency")
plt.show()

#Generating the Box-plot
sns.boxplot(df['Price'])
plt.ylabel("Apartment Price")
plt.show()

#At least 25% of the sample has the price of the apartment up to 797 thousand;
#50% of the sample are priced between 797 and 981 thousand;
#at least 25% of the sample have prices above 981 thousand.
#Values above 3Q+1.5(Q3-Q1) or below 1Q-1.5(Q3-Q1) are seen as outliers.
df.describe()

"""**Multivariate Analysis**"""

#Generating the Scatter Chart
sns.scatterplot(x=df['Size (m2)'], y=df['Price'])

#Adding the regression line
sns.regplot(x=df['Size (m2)'], y=df['Price'])

#Plot combined between Scatter and Histogram
sns.jointplot(x=df['Size (m2)'], y=df['Price'])

#To generate the Pearson coefficient, we will need to import the Scipy.stats library
from scipy.stats import pearsonr

pearsonr(df['Neighborhood_C'], df['Price'])

#Calculating the correlation for all combinations
df.corr()

#Heatmap to analyze the correlation between variables
sns.heatmap(df.corr(), annot=True, fmt='.2f')

#Cross analysis of categorical data
ctab = pd.crosstab(df['Garage'], df['Rooms'])
ctab

sns.heatmap(ctab, annot=True)

#Line-normalized analysis. Of the apartments that have 1 parking space, 64% have 3 bedrooms, 28% 2 bedrooms and 7% 4 bedrooms.
ctab = pd.crosstab(df['Garage'], df['Rooms'], normalize='index')
ctab

#Is it possible to add this table in a heatmap
sns.heatmap(ctab, annot=True, fmt='.2f')

#Column normalized analysis. Of the apartments with 2 bedrooms, 66% have 2 parking spaces, 26% 1 parking space and 6% do not have spaces.
ctab = pd.crosstab(df['Garage'], df['Rooms'], normalize='columns')
ctab

#Is it possible to add this table in a heatmap
sns.heatmap(ctab, annot=True, fmt='.2f')