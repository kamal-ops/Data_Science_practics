#!/usr/bin/env python
# coding: utf-8

# # Method: Delete row and columns

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Load Dataset

dataset = pd.read_csv("H:\\data_science\datasets\\house-prices-advanced-regression-techniques (1)\\train.csv")


# In[3]:


dataset.shape


# In[4]:


dataset.head(5)


# In[5]:


# to display all columns we use pd.set_option
pd.set_option('display.max_columns', None) # Display all columns
pd.set_option('display.max_rows', None) # Dsiplay all rows
dataset.head(5) # display first 5 rows


# In[6]:


dataset.info() # all columns information


# In[7]:


dataset.isnull().sum() # get information of null value present in particular columns


# In[8]:


plt.figure(figsize=(16,9))
sns.heatmap(dataset.isnull())
plt.show()


# In[34]:


# getting per% missing value
null_var = dataset.isnull().sum()/dataset.shape[0] *100
null_var


# In[10]:


drop_clm = null_var[null_var > 17].keys()
drop_clm


# In[11]:


df2 = dataset.drop(columns = drop_clm)
df2


# In[12]:


plt.figure(figsize=(16,9))
sns.heatmap(df2.isnull())
plt.show()


# In[13]:


df3 = df2.dropna()
df3


# In[14]:


plt.figure(figsize=(16,9))
sns.heatmap(df3.isnull())
plt.show()


# In[15]:


df3.isnull().sum()


# In[19]:


df3.select_dtypes(include=['int64', 'float64']).columns


# In[23]:


plt.figure(figsize=(16,9))
sns.distplot(df3['SalePrice'])
plt.show()


# In[24]:


plt.figure(figsize=(16,9))
sns.distplot(df3['YrSold'])
plt.show()


# In[25]:


plt.figure(figsize=(16,9))
sns.distplot(df3['MSSubClass'])
plt.show()


# In[37]:


plt.figure(figsize=(16,9))
sns.distplot(dataset['MSSubClass'], kde=False)
plt.show()


# In[29]:


plt.figure(figsize=(16,9))
sns.distplot(dataset['MSSubClass'])
sns.distplot(df3['MSSubClass'])
plt.legend()
plt.show()


# In[36]:


variables = ['Id', 'MSSubClass', 'LotArea', 'OverallQual', 'OverallCond',
       'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2',
       'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF',
       'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
       'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces',
       'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF',
       'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal',
       'MoSold', 'YrSold', 'SalePrice']
plt.figure(figsize=(25,25))
for i, var in enumerate(variables):
    plt.subplot(9, 4, i+1)
    sns.distplot(dataset[var], bins = 20)
    sns.distplot(df3[var], bins=20)
    plt.show()
    
    


# In[38]:


# getting categorical 
df3.select_dtypes(include=['object']).columns


# In[ ]:




