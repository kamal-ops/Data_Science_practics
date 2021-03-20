#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[8]:


df = pd.read_csv('H:\\data_science\\datasets\\cars.csv')
df


# In[6]:


type(df)


# In[7]:


df.columns


# In[10]:


df = pd.read_csv('H:\\data_science\\datasets\\cars.csv', nrows = 2)
df


# In[ ]:




