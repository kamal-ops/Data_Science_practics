#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libararies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#load dataset
df = pd.read_csv(r"H:\data_science\datasets\house-prices-advanced-regression-techniques (1)\train.csv")


# In[6]:


#get categorical variable from thedataset

cat_vars = df.select_dtypes(include=['object'])
cat_vars.head()


# In[7]:


#finding missing from categorical variable
miss_value_per = cat_vars.isnull().mean() *100
miss_value_per


# In[ ]:




