#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("H:\data_science\datasets\gini.csv")
df


# In[3]:


df.loc[0]


# In[5]:


df.loc[226]


# In[6]:


df.loc[[0, 226]]


# In[9]:


df.loc[0:5]


# In[ ]:




