#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("H:\data_science\datasets\gini.csv")
df


# In[3]:


df = pd.read_csv("H:\data_science\datasets\gini.csv", keep_default_na = False)
df


# In[4]:


df = pd.read_csv("H:\data_science\datasets\gini.csv", keep_default_na = True)
df


# In[5]:


df = pd.read_csv("H:\data_science\datasets\gini.csv",na_filter = False)
df


# In[6]:


df = pd.read_csv("H:\data_science\datasets\gini.csv",na_filter = True)
df


# In[7]:


df.isnull()


# In[8]:


df.notnull()


# In[9]:


df.isnull().sum().sum()


# In[10]:


df.notnull().sum().sum()


# In[11]:


import numpy as np
ser = pd.Series([1,2,3,np.nan, 4,5,np.NaN])
ser


# In[12]:


ser.isnull()


# In[13]:


ser.isnull().sum()


# In[14]:


ser.notnull()


# In[15]:


ser.notnull().sum()


# # drop na

# In[16]:


df


# In[17]:


df.dropna()


# In[18]:


df.dropna(axis=1)


# In[19]:


df.dropna(axis = 1,how = 'any')


# In[20]:


df.dropna(how = 'all')


# In[21]:


df.dropna(thresh = 5)


# In[22]:


df.dropna(subset = ['GINI index', '1982'])


# In[23]:


df.dropna(inplace=True)


# In[24]:


df.dropna(inplace=False)


# # Pandas fillna method

# In[25]:


df = pd.read_csv("H:\data_science\datasets\gini.csv")
df


# In[26]:


df.fillna(0)


# In[27]:


df.fillna(2)


# In[28]:


df.fillna(method='ffill')


# In[29]:


df.fillna(method='pad')


# In[30]:


df.fillna(method='bfill')


# In[31]:


df.fillna(method='ffill', axis=1)


# In[32]:


df.fillna(method='ffill', limit=10)


# # Pandas Replace

# In[ ]:




