#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns
import pandas as pd
import numpy as np
import random


# In[6]:


dataset = sns.load_dataset("titanic")


# In[7]:


dataset.shape


# In[8]:


dataset


# In[15]:


sns.set()
sns.scatterplot(x= 'age', y='fare', data=dataset, hue='sex')
plt.show()


# In[16]:


sns.set()
sns.scatterplot(x= 'age', y='fare', data=dataset, hue='sex', style='who')
plt.show()


# In[17]:


sns.set()
sns.scatterplot(x= 'age', y='fare', data=dataset, hue='sex', style='who', size='who')
plt.show()


# In[19]:


sns.set()
sns.scatterplot(x= 'age', y='fare', data=dataset, hue='sex', style='who', size='who',
               sizes=(100,400))
plt.show()


# In[20]:


plt.figure(figsize=(16,9))
sns.set()
sns.scatterplot(x= 'age', y='fare', data=dataset, hue='sex', style='who', size='who',
               sizes=(100,400))
plt.show()


# In[21]:


plt.figure(figsize=(16,9))
sns.set()
sns.scatterplot(x= 'who', y='fare', data=dataset, hue='alive', style='alive', size='who',
               sizes=(100,400))
plt.show()


# In[ ]:




