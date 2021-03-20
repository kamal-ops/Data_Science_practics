#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("H:\data_science\datasets\gini.csv")
df


# In[3]:


type(df)


# In[4]:


df.columns


# In[5]:


df = pd.read_csv("H:\data_science\datasets\gini.csv", nrows = 1)
df


# In[6]:


df = pd.read_csv("H:\data_science\datasets\gini.csv", nrows = 5)
df


# In[7]:


df = pd.read_csv("H:\data_science\datasets\gini.csv", usecols = [0,1], nrows = 5)
df


# In[8]:


df = pd.read_csv("H:\data_science\datasets\gini.csv", usecols = [0,1], nrows = 5,index_col = 'GINI index')
df


# In[9]:


df = pd.read_csv("H:\data_science\datasets\cars.csv", header = None, prefix = 'columns')
df


# In[10]:


df = pd.read_csv("H:\data_science\datasets\cars.csv", sep = ';', skiprows = 2, header = None, prefix = 'Kamal')
df


# In[12]:


df = pd.read_csv("H:\data_science\datasets\cars.csv", sep = ';', skiprows = [1])
df


# In[13]:


df.head()


# In[14]:


df.tail()


# In[15]:


df.head(10)


# In[ ]:





# In[17]:


df.tail(10)


# In[25]:


df = pd.read_csv("H:\data_science\datasets\cars.csv", sep = ';', skiprows = [1], dtype = {'Model':'float64'})
df


# In[27]:


df = pd.read_csv("H:\data_science\datasets\cars.csv", sep = ';', skiprows = [1], true_values = ['US'], false_values = ['Europe'])
df


# In[ ]:





# In[ ]:




