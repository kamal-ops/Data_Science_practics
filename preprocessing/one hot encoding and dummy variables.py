#!/usr/bin/env python
# coding: utf-8

# In[1]:


#python libraries
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


# In[2]:


# #import dataset ---> loading data online using seaborn.load_dataset function
# import seaborn as sns
# tips_data = sns.lead_dataset("tips")
# tips_data


# In[3]:


tips_data = pd.read_csv(r"H:\data_science\datasets\seaborn-data-master\tips.csv")
tips_data


# In[4]:


#create dummy variables
dummy_dataset = pd.get_dummies(tips_data)
dummy_dataset


# In[5]:


dummy_dataset = pd.get_dummies(tips_data, drop_first =True)
dummy_dataset


# # Scikit-learn One Hot Encoder

# In[6]:


from sklearn.preprocessing import OneHotEncoder


# In[30]:


#one hot encoding 
oh_enc = OneHotEncoder(sparse=False, drop="First")


# In[31]:


#get categorical variables list
cat_vars = tips_data.select_dtypes(include=['object']).columns
cat_vars


# In[26]:


oh_enc_array = oh_enc.fit_transform(tips_data[cat_vars])
oh_enc_array


# In[34]:


pd.get_dummies(tips_data, drop_first=True).keys()


# In[37]:


#change numpy arry into DataFrame
oh_enc_data = pd.DataFrame(oh_enc_array, columns=['sex_Male', 'smoker_Yes', 'day_Sat',
       'day_Sun', 'day_Thur', 'time_Lunch'])


# In[38]:


oh_enc_data


# In[ ]:




