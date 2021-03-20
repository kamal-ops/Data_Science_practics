#!/usr/bin/env python
# coding: utf-8

# In[1]:


#python libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


# In[2]:


#load dataset
df = pd.read_csv(r"H:\data_science\datasets\house-prices-advanced-regression-techniques (1)\train.csv")
# df.keys().sort
pd.set_option("display.max_rows", None)


# In[3]:


#select columns on which we are applying label encoding
df2 = df[["KitchenQual","BldgType"]]
df2


# In[4]:


#apply lable encoding
label_encod = LabelEncoder()


# In[5]:


label_encod.fit_transform(df2["BldgType"])


# In[6]:


df2["BldgType_encod"] = label_encod.fit_transform(df2["BldgType"])
df2


# In[7]:


df['BldgType'].value_counts()


# In[8]:


df2['BldgType_encod'].value_counts()


# # Order Encoding

# In[9]:


df["KitchenQual"].value_counts()


# In[10]:


#Create order dictionary
order_label = {"EX":4, "Gd":3, "TA":2, "Fa":1}


# In[11]:


df2["KitchenQual_encod"] = df2["KitchenQual"].map(order_label)
df2


# In[ ]:




