#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import random
import pandas as pd


# In[2]:


df_google_playstore = pd.read_csv("H:\\data_science\\datasets\\archive\\googleplaystore.csv")
df_google_playstore.shape


# In[3]:


df_google_playstore = pd.read_csv("H:\\data_science\\datasets\\archive\\googleplaystore.csv", nrows = 1000)
df_google_playstore.shape


# In[4]:


df_google_playstore


# In[7]:


x = df_google_playstore["Rating"]
y = df_google_playstore["Reviews"]


# In[23]:


plt.figure(figsize=(16,9))
plt.scatter(x, y, color = 'r', marker = "*",  s=100, alpha = 0.5, linewidth=5, edgecolor = 'blue')#verts="<"
plt.title("Google play store apps scatter plot", fontsize = 25)
plt.xlabel("Rating")
plt.ylabel("Reviews")
plt.show()


# In[31]:


plt.figure(figsize=(16,9))
plt.scatter(x, y, color = 'r', marker = "*")#verts="<"
plt.scatter(x,df_google_playstore["Installs"], color = 'b', marker = "o")#verts="<"
plt.title("Google play store apps scatter plot", fontsize = 25)
plt.xlabel("Rating")
plt.ylabel("Reviews and Install")
plt.show()


# In[ ]:




