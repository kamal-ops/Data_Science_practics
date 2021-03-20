#!/usr/bin/env python
# coding: utf-8

# # Data cleaning (Missing Value Imputation)

# ## mean mode and median

# In[1]:


# Import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Load dataset
df1 = pd.read_csv(r"H:\data_science\datasets\house-prices-advanced-regression-techniques (1)\train.csv")
pd.set_option('display.max_columns', None) # load all columns of dataset
pd.set_option('display.max_rows', None) #load all rows of dataset


# In[3]:


df1.head(5) # first 5 records of dataset


# In[4]:


df1.tail(6) # last 6 records of dataset


# In[5]:


df1.info() #information of dataset


# In[6]:


df1.isnull().sum() #getting sum of null values present in column


# In[7]:


df1.isnull().sum().sum() # total NaN values present in dataset


# In[8]:


# getting percentage of null values present in every column.
missing_value_per = df1.isnull().sum()/df1.shape[0] *100
missing_value_per


# In[9]:


# getting list of columns having more than 17% missing values
missing_20_per = missing_value_per[missing_value_per > 20].keys()
missing_20_per


# In[10]:


# droping the columns having more than 17% missing values
df2 = df1.drop(columns = missing_20_per)


# In[11]:


#geting list of numeric data type columns
df3_numeric = df2.select_dtypes(include = ['int64', 'float64'])
df3_numeric.head()


# In[12]:


df3_numeric.shape


# In[13]:


plt.figure(figsize=(25,25))
sns.heatmap(df3_numeric.isnull())
plt.show()


# In[14]:


#accessing varibale who have missing values

missing_num_var = [var for var in df3_numeric if df3_numeric[var].isnull().sum()]
missing_num_var


# In[15]:


# showing distplot for missing var
plt.figure(figsize=(10,10))
sns.set()
for i, var in enumerate(missing_num_var):
    plt.subplot(2,2,i+1)
    sns.distplot(df3_numeric[var], bins=20, kde_kws = {'linewidth':5, 'color':'#DC143C'})
    plt.show()


# In[16]:


#filling missing values with mean 

df4_numeric = df3_numeric.fillna(df3_numeric.mean())
df4_numeric.isnull().sum().sum()


# In[20]:


# distributation of original data and clean data
plt.figure(figsize=(16,9))
sns.set()
for i, var in enumerate(missing_num_var):
    plt.subplot(2,2,i+1)
    sns.distplot(df3_numeric[var], bins=20,
                kde_kws={'linewidth':8, 'color':'blue'}, label='origional')
    sns.distplot(df4_numeric[var], bins=20,
                kde_kws={'linewidth':5, 'color':'green'}, label='Mean')
    plt.legend()
    plt.show()


# In[23]:


#filling missing values with median value
df5_numeric = df3_numeric.fillna(df3_numeric.median())
df5_numeric.isnull().sum().sum()


# In[33]:


#distributation of origional dataand missing value filled with median value
plt.figure(figsize=(16,9))
sns.set()
for i, var in enumerate(missing_num_var):
#     plt.subplot(2,2,i+1)
    sns.distplot(df3_numeric[var], bins=20,hist=False,
                kde_kws={'linewidth':8, 'color':'blue'}, label='origional')
    sns.distplot(df4_numeric[var], bins=20,hist=False,
                kde_kws={'linewidth':5, 'color':'green'}, label='Mean')
    sns.distplot(df5_numeric[var], bins=20,hist=False,
                kde_kws={'linewidth':3, 'color':'k'}, label='Median')
    plt.legend()
    plt.show()


# In[37]:


#boxplot of origional dataand missing value filled with mean, median value
plt.figure(figsize=(16,9))
sns.set()
for i, var in enumerate(missing_num_var):
#     plt.subplot(2,2,i+1)
    sns.boxplot(df3_numeric[var])
    sns.boxplot(df4_numeric[var])
    sns.boxplot(df5_numeric[var])
#     plt.legend()
    plt.show()


# In[ ]:




