#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


df = pd.read_csv("H:\data_science\datasets\gini.csv")
df


# In[7]:


df.interpolate()


# In[9]:


df.interpolate(method='linear')


# In[12]:


df.interpolate(method='index')


# In[18]:


df.dtypes


# In[ ]:





# In[ ]:




