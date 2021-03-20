#!/usr/bin/env python
# coding: utf-8

# # Matplotlib Line Plot
# 

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


data1 = pd.read_csv("H:\data_science\datasets\happiness.csv")
data1


# In[3]:


data2 = data1.fillna(method = 'ffill')
data2


# In[4]:


df1 = [1,2,3,4,5,6,7,8,9,10]
def2 = [33,45,56,67,89,78,56,45,54,43]
plt.plot(df1, def2)
plt.title("Daily Temperature")
plt.xlabel("days")
plt.ylabel("Temperature")
plt.show()


# In[5]:


df1 = [1,2,3,4,5,6,7,8,9,10]
def2 = [33,45,56,67,89,78,56,45,54,43]
plt.plot(df1, def2)
plt.axis(xmin = 0, xmax = 15, ymin = 0, ymax = 100)
plt.title("Daily Temperature")
plt.xlabel("days")
plt.ylabel("Temperature")
plt.show()


# In[16]:


df1 = [1,2,3,4,5,6,7,8,9,10]
def2 = [33,45,56,67,89,78,56,45,54,43]
plt.plot(df1, def2, color = 'r', marker = 'o', linestyle = ":", linewidth = 2, markersize = 10)
plt.axis(xmin = 0, xmax = 15, ymin = 0, ymax = 100)
plt.title("Daily Temperature")
plt.xlabel("days")
plt.ylabel("Temperature")
plt.show()


# In[34]:


from matplotlib import style
df1 = [1,2,3,4,5,6,7,8,9,10]
def2 = [33,45,56,67,89,78,56,45,54,43]
df3 = [10,20,30,40,50,40,30,20,10,5]
plt.plot(df1, def2, "mo--", linewidth = 2, markersize = 10, label = "First")
plt.plot(df1, df3, "yo--", linewidth = 2, markersize = 10, label = "Second")
style.use("ggplot")
plt.axis(xmin = 0, xmax = 15, ymin = 0, ymax = 100)
plt.title("Daily Temperature", fontsize=30)
plt.xlabel("days", fontsize = 25)
plt.ylabel("Temperature", fontsize = 25)
plt.legend(loc = 4)
plt.grid(color='b', linestyle = '-', linewidth = 1)
plt.show()


# In[ ]:




