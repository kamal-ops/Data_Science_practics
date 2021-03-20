#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df1 = pd.read_csv("H:\data_science\datasets\happiness.csv")
df1


# In[6]:


df2 = df1.fillna(method = 'ffill')
pd.melt(df2)


# In[8]:


pd.melt(df2, id_vars = ['Country', 'Gender'])


# In[10]:


pd.melt(df2, id_vars = ['Country'], value_vars = ['Gender'])


# In[ ]:




