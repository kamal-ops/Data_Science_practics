#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


# In[2]:


#load datsets
train = pd.read_csv(r"H:\data_science\datasets\house-prices-advanced-regression-techniques (1)\train.csv")
test = pd.read_csv(r"H:\data_science\datasets\house-prices-advanced-regression-techniques (1)\test.csv")

print("Shape of train datset : ",train.shape)
print("Shape of test dataset : ",test.shape)


# In[3]:


X_train = train.drop(columns = "SalePrice", axis = 1)
y_train = train["SalePrice"]
X_test = test.copy()

print("Shape of X_train: ", X_train.shape)
print("Shape of y_train: ", y_train.shape)
print("Shape of X_test: ", X_test.shape)


# # Missing Value Imputation

# In[4]:


isnull_sum = X_train.isnull().sum()
isnull_sum


# In[5]:


#Find the numerical variables which have missing values
num_vars = X_train.select_dtypes(include=["int64", "float64"]).columns
num_vars_miss = [var for var in num_vars if isnull_sum[var] >0]
num_vars_miss


# In[6]:


#finding the categorical variables which have missing values
cat_vars = X_train.select_dtypes(include=["O"]).columns
cat_vars_miss = [var for var in cat_vars if isnull_sum[var] > 0]
cat_vars_miss


# In[7]:


num_var_mean = ["LotFrontage"] #fill missing value with mean value
num_var_median = ["MasVnrArea", "GarageYrBlt"]#fill missing value with median
cat_vars_mode = ['Alley',
 'MasVnrType',
 'BsmtQual',
 'BsmtCond',
 'BsmtExposure',
 'BsmtFinType1',
 'BsmtFinType2',
 'Electrical',
 'FireplaceQu',
 'GarageType'] # fill missing value with mode
cat_vars_missing = ['GarageFinish',
 'GarageQual',
 'GarageCond',
 'PoolQC',
 'Fence',
 'MiscFeature']#fill missing value with static value


# In[12]:


#creating pipeline to fill different missing value variables

num_var_mean_imputer = Pipeline(steps=[("imputer", SimpleImputer(strategy="mean"))])
num_var_median_imputer = Pipeline(steps=[("imputer", SimpleImputer(strategy="median"))])

cat_vars_mode_imputer = Pipeline(steps=[("imputer", SimpleImputer(strategy="most_frequent"))])
cat_vars_missing_imputer = Pipeline(steps=[("imputer", SimpleImputer(strategy = "constant", fill_value = "Missing"))])


# In[13]:


#applying different strategy on different variables

preprocessor = ColumnTransformer(transformers=[('mean_imputer', num_var_mean_imputer, num_var_mean),
                                             ('median_imputer', num_var_median_imputer, num_var_median),
                                             ('mode_imputer', cat_vars_mode_imputer, cat_vars_mode),
                                             ('missing_imputer', cat_vars_missing_imputer, cat_vars_missing)])


# In[14]:


#applying preprocessor on X_train dataset
preprocessor.fit(X_train)


# In[17]:


#chceck states
preprocessor.named_transformers_['mean_imputer'].named_steps['imputer'].statistics_


# In[19]:


preprocessor.named_transformers_['median_imputer'].named_steps['imputer'].statistics_


# In[20]:


preprocessor.named_transformers_['mode_imputer'].named_steps['imputer'].statistics_


# In[21]:


preprocessor.named_transformers_['missing_imputer'].named_steps['imputer'].statistics_


# In[22]:


X_train_clean = preprocessor.transform(X_train)
X_test_clean = preprocessor.transform(X_test)


# In[25]:


X_train_clean_miss_variables = pd.DataFrame(X_train_clean, columns = num_var_mean+num_var_median+cat_vars_mode+cat_vars_missing)
X_train_clean_miss_variables


# In[27]:


X_train_clean_miss_variables.isnull().sum().sum()


# In[ ]:




