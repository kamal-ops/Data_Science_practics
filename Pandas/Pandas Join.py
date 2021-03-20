#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df1 = pd.DataFrame({'A': [1,2,3,4],
                   'B': [10,20,30,40]})
df2 = pd.DataFrame({'C':[5,6,7,8],
                   'D': [50,60,70,80]})

display(df1, df2)


# In[5]:


df1.join(df2)


# In[6]:


df1.append(df2)


# In[8]:


df1 = pd.DataFrame({'A': [1,2,3,4],
                   'B': [10,20,30,40]})
df2 = pd.DataFrame({'A':[5,6,7,8],
                   'B': [50,60,70,80]})

display(df1, df2)


# In[12]:


df1.append(df2, ignore_index = True)


# In[13]:


df1.append(df2, sort = True)


# In[15]:


df2.append(df1, ignore_index = True, sort = True)


# In[ ]:




