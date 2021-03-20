#!/usr/bin/env python
# coding: utf-8

# # How to create Pandas DataFrame

# In[1]:


import pandas as pd


# In[4]:


df = pd.DataFrame()
print(df)


# In[7]:


list = ['a', 'b', 'c']
print(list)


# In[9]:


df1 = pd.DataFrame(list)
print(df1)


# In[10]:


df1


# In[13]:


ls_of_ls = [[1,2,3],[2,3,4],[5,6,7]]
df2 = pd.DataFrame(ls_of_ls)


# In[14]:


df2


# In[ ]:




