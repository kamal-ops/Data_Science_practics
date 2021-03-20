#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


sr1 = pd.Series([0,1,2])
sr1


# In[7]:


sr2 = pd.Series([3,4,5,6,7])
sr2


# In[8]:


pd.concat([sr1, sr2])


# In[10]:


df1 = pd.DataFrame({'ID': [1,2,3,4],
                   'Name':['A', 'B', 'C', 'D'],
                   'Class':[5,6,7,8]})

df1


# In[11]:


df2 = pd.DataFrame({'ID': [5,6,7,8],
                   'Name':['E', 'F', 'G', 'H'],
                   'Class':[9,10,11,12]})
df2


# In[13]:


pd.concat([df2, df1])


# In[14]:


pd.concat([df1, df2], axis=1)


# In[16]:


pd.concat([df1, df2], axis=0, ignore_index = True)


# In[19]:


pd.concat([df1, df2], axis = 1, join= 'inner')


# In[20]:


pd.concat([df1, df2], keys=['first DF', 'Secoend DF'])


# In[21]:


pd.concat([df1, df2],axis = 1, keys=['first DF', 'Secoend DF'])


# In[ ]:




