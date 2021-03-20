#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# In[2]:


array_2d = np.linspace(1,5,12).reshape(4,3)
array_2d


# In[3]:


sns.heatmap(array_2d)


# In[28]:


df = pd.read_csv("H:\data_science\datasets\seaborn-data-master\diamonds.csv", nrows=15)


# In[29]:


df1 = df.set_index("cut").drop(columns=['color', 'clarity'], axis=1)
df1


# In[30]:


plt.figure(figsize=(16,9))
sns.set()
sns.heatmap(df1, vmin=0, vmax=10, cmap="Accent")


# In[33]:


plt.figure(figsize=(16,9))
sns.set()
sns.heatmap(df1, vmin=0, vmax=100, cmap="Accent", annot =True)
plt.show()


# In[ ]:




