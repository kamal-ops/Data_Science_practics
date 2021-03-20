#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import python libs
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer


# In[2]:


train = pd.read_csv(r"H:\data_science\datasets\house-prices-advanced-regression-techniques (1)\train.csv")
test = pd.read_csv(r"H:\data_science\datasets\house-prices-advanced-regression-techniques (1)\test.csv")

print("Shape of Train Dataset:" ,train.shape)
print("Shape of Test Dataset:", test.shape)


# In[3]:


X_train = train.drop(columns = ['SalePrice'])
y_train = train['SalePrice']


# # Numerical Missing Value Imputation

# In[4]:


#getting numerical variables/ columns having numeric value in X_train
X_train_num =  X_train.select_dtypes(include=['int64', 'float64']).columns
X_train_num                                     


# In[5]:


#getting missing values in numerical varables
X_train_num.isnull().sum()


# In[ ]:




