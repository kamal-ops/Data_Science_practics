#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df1 = pd.read_csv("H:\data_science\datasets\happiness.csv")
df1


# In[3]:


df1.pivot_table(index = 'Country')


# In[14]:


df2 = df1.fillna(method = 'ffill')


# In[16]:


df2.pivot_table(index = 'Gender', columns = 'Country')


# In[20]:


df2.pivot_table(index = 'Gender', columns = 'Country', aggfunc = 'max')


# In[23]:


df2.pivot_table(index = 'Country', aggfunc = 'sum')


# In[24]:


df2.pivot_table(index = 'Country', aggfunc = 'count')


# In[25]:


df2.pivot_table(index = 'Country', margins = True)


# In[26]:


df2.pivot_table(index = 'Country', margins = False)


# In[ ]:




