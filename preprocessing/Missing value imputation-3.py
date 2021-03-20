#!/usr/bin/env python
# coding: utf-8

# # Measure of central tendancy for each class

# In[1]:


# import python libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv(r"H:\data_science\datasets\house-prices-advanced-regression-techniques (1)\train.csv")


# In[3]:


#to see maximum rows and columns
pd.set_option('display.max_columns', None)
pd.set_option('display.max.rows', None)


# In[4]:


#finding columns having more then 20% missing values
missing_value_var = df.isnull().sum() / df.shape[0] *100


# In[5]:


# getting colums name having 20% or more missing value
clm_missing_20 = missing_value_var[missing_value_var > 20]. keys()
#dropping columns drop columns having 20% or more missing values
df_drop_20 = df.drop(columns = clm_missing_20)


# In[6]:


#finding columns having missing values after droping columns
# df_drop_20.isnull().sum()


# In[7]:


# Create a new datset having only numeric values.
df_numeric = df_drop_20.select_dtypes(include=['int64', 'float64'])
df_numeric.shape


# In[8]:


#check the missing values in newly created numeric dataset
missing_value_var = [var for var in df_numeric if df_numeric[var].isnull().sum() > 0]
#check the rows having missing value
df_numeric[missing_value_var][df_numeric[missing_value_var].isnull().any(axis=1)]


# In[11]:


#check the unique values present in column/ variable
# for var in missing_value_var:
#     value = df_numeric[var].unique()
#     value

df['LotConfig'].unique()


# In[13]:


#getting rows having particular value of a variable
df[df.loc[:,'LotConfig'] == 'Inside'] # all rows having "Inside" in "LotConfig" column recived
df[df.loc[:,'LotConfig'] == 'Inside']['LotFrontage']#getting value of "LotFrontage" column where "LogConfig == Inside"


# In[15]:


# fillied the missing value with mean value of all availbe values in particular column
df[df.loc[:,'LotConfig']   == 'Inside']['LotFrontage'].replace(np.nan, df[df.loc[:,'LotConfig'] == 'Inside']['LotFrontage'].mean())


# In[21]:


#Fill missing value of LoatFrontage cloumn/ varibale
df_copy = df.copy()#create copy of main dataset
for var_class in df_copy['LotConfig'].unique():
    df_copy.update(df[df.loc[:,'LotConfig'] == var_class]['LotFrontage'].replace(np.nan, df[df.loc[:, 'LotConfig']==var_class]['LotFrontage'].mean()))


# In[22]:


df_copy.isnull().sum()


# In[25]:


plt.figure(figsize=(10,10))
sns.set()
for i, var in enumerate(missing_value_var):
    plt.subplot(2,2,i+1)
    sns.distplot(df_copy[var], bins=20, kde_kws = {'linewidth':5, 'color':'#DC143C'})
    sns.distplot(df[var], bins=20, kde_kws = {'linewidth':5, 'color':'#AAAAAA'})
    plt.show()


# In[ ]:




