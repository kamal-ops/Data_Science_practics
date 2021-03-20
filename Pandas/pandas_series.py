#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.__version__


# In[3]:


list1= [1,2,3,4,-2.2,2.02,'kamal', 'swami', 10]


# In[5]:


series1=pd.Series(list1)
print(series1)


# In[6]:


type(series1)


# In[11]:


list2 = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'], dtype=float, name= 'values')
print(list2)


# In[12]:


list2[1]


# ## 

# In[13]:


list2[0:3]


# In[14]:


list2[>3]


# In[ ]:




