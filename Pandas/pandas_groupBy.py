#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[9]:


df = pd.read_csv("H:\\data_science\\datasets\\BabyData\\Nursing_data_11_29_2012.csv", sep = "\t")
df


# In[3]:


gr1 = df.groupby(by = 'Side 2')
gr1


# In[4]:


gr1.groups


# In[5]:


df.groupby(['Side 1', 'Side 2']).groups


# In[6]:


for side_1, Side_2 in gr1:
    print(side_1)
    print(Side_2)


# In[7]:


list(gr1)


# In[8]:


dict(list(gr1))


# In[16]:


gr1.sum()


# In[17]:


gr1.mean()


# In[18]:


gr1.describe()


# In[ ]:




