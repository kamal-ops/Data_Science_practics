#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import random
from scipy.stats import norm


# In[2]:


dataset = sns.load_dataset("tips")
dataset


# In[8]:


sns.barplot(x = dataset.day, y = dataset["total_bill"], hue = "sex",data = dataset, order = ['Sun', 'Sat','Fri', 'Thur'],
           hue_order=['Female', 'Male'])
plt.show()


# In[9]:


sns.barplot(x = dataset.day, y = dataset["total_bill"], hue = "sex",data = dataset, order = ['Sun', 'Sat','Fri', 'Thur'],
           hue_order=['Female', 'Male'], estimator=np.max)
plt.show()


# In[11]:


sns.barplot(x = dataset.day, y = dataset["total_bill"], hue = "sex",data = dataset, order = ['Sun', 'Sat','Fri', 'Thur'],
           hue_order=['Female', 'Male'], estimator=np.max, ci=20)
plt.show()


# In[13]:


sns.barplot(x = dataset.day, y = dataset["total_bill"], hue = "sex",data = dataset, order = ['Sun', 'Sat','Fri', 'Thur'],
           hue_order=['Female', 'Male'], estimator=np.max, orient='v')
plt.show()


# In[16]:


sns.barplot(x = dataset.day, y = dataset["total_bill"], hue = "sex",data = dataset, order = ['Sun', 'Sat','Fri', 'Thur'],
           hue_order=['Female', 'Male'], estimator=np.max, color='red', palette='magma')
plt.show()


# In[19]:


sns.barplot(x = dataset.day, y = dataset["total_bill"], hue = "sex",data = dataset, order = ['Sun', 'Sat','Fri', 'Thur'],
           hue_order=['Female', 'Male'], estimator=np.max, color='red', palette='magma', saturation=100)
plt.show()


# In[20]:


sns.barplot(x = dataset.day, y = dataset["total_bill"], hue = "sex",data = dataset, order = ['Sun', 'Sat','Fri', 'Thur'],
           hue_order=['Female', 'Male'], estimator=np.max, color='red', palette='magma', saturation=100, errcolor='Red')
plt.show()


# In[21]:


sns.barplot(x = dataset.day, y = dataset["total_bill"], hue = "sex",data = dataset, order = ['Sun', 'Sat','Fri', 'Thur'],
           hue_order=['Female', 'Male'], estimator=np.max, color='red', palette='magma', saturation=100, errcolor="green", errwidth=15)
plt.show()


# In[24]:


sns.barplot(x = dataset.day, y = dataset["total_bill"], hue = "sex",data = dataset, order = ['Sun', 'Sat','Fri', 'Thur'],
           hue_order=['Female', 'Male'], estimator=np.max, color='red', palette='magma', saturation=100, errcolor="green", 
            errwidth=15, capsize = 1)
plt.show()


# In[27]:


sns.set()
sns.barplot(x = dataset.day, y = dataset["total_bill"],alpha=0.9, linestyle="-.", linewidth=6, edgecolor="red")
plt.show()


# In[ ]:




