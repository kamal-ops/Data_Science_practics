#!/usr/bin/env python
# coding: utf-8

# # Numerical missing value Imputaion By Class

# In[1]:


#python librariers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#load data set
df1 = pd.read_csv(r"H:\data_science\datasets\house-prices-advanced-regression-techniques (1)\train.csv")


# In[3]:


#showing all compumns and rows 
pd.set_option('display.max_columns', None) # shows all columns
pd.set_option('display.max_rows', None) # Display all rows
df1.head(4) # Display fisrt 4 rows


# In[4]:


# get shape of dataset
df1.shape


# In[5]:


#Get dataset information
df1.info()


# In[6]:


# get missing values informations
df1.isnull().sum() # count the total missing values present in a column


# In[7]:


# count total missing value presennt in datset
df1.isnull().sum().sum()


# In[8]:


# get the list of all clolumns having numeric value in datset
num_values_clms = df1.select_dtypes(include= ['int64', 'float64']).columns


# In[9]:


# getting list of all comluns have categorical values in dataset
cat_value_clms = df1.select_dtypes(include=['object']).columns
cat_value_clms


# In[10]:


# getting presentage of missing value present in dataset
missing_value_per = df1.isnull().sum() / df1.shape[0] * 100
missing_value_per


# In[11]:


# getting list of columns having more than 20% missing values
missing_20_per = missing_value_per[missing_value_per > 20].keys()
missing_20_per


# In[12]:


#droping columns having more than 20% missing values
df2 = df1.drop(columns=missing_20_per)
df2.shape# as we can check after dropping columns having more then 20% missing vlaue shape of origional dataset and current dataset is changed


# In[13]:


plt.figure(figsize=(16,9))
sns.heatmap(df2.isnull())
plt.show()


# In[14]:


#create a new dataset having only numeric value
df_numeric = df2.select_dtypes(include=['int64', 'float64'])
df_numeric.head()


# In[15]:


#plotting a heatmap of missing values presnet in dataset with only numeric values
plt.figure(figsize=(25,25))
sns.set()
sns.heatmap(df_numeric.isnull())
plt.show()


# In[16]:


#getting list of columns having missing values 
num_var_missing = [var for var in df_numeric if df_numeric[var].isnull().sum() > 0]
num_var_missing


# In[19]:


#check the categorical variable 
val_fr_heat = df_numeric[num_var_missing].isnull().any(axis=1)


# In[35]:


plt.figure(figsize=(16,9))
sns.set()
plt.pie(val_fr_heat)
# plt.title("Missing Value Imputation")
# plt.legend(loc = 2)
plt.savefig("RnD.png")
plt.show()


# In[ ]:




