#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.stats import norm


# In[2]:


tips_dataset = sns.load_dataset("tips")
tips_dataset


# In[3]:


sns.distplot(tips_dataset["size"])


# In[4]:


sns.distplot(tips_dataset["tip"])


# In[5]:


sns.distplot(tips_dataset["total_bill"])


# In[6]:


sns.distplot(tips_dataset["total_bill"], bins = 10)


# In[7]:


sns.distplot(tips_dataset["total_bill"], bins = 100)


# In[8]:


sns.distplot(tips_dataset["total_bill"], bins = 100, hist=False)


# In[9]:


sns.distplot(tips_dataset["total_bill"], bins = 100, kde =False)


# In[10]:


sns.distplot(tips_dataset["total_bill"], bins = 100, kde =False, rug =True)


# In[11]:


sns.distplot(tips_dataset["total_bill"], bins = 100, kde =True, fit = norm )


# In[13]:


sns.distplot(tips_dataset["total_bill"], bins = 10, kde =False, fit = norm )


# In[14]:


sns.distplot(tips_dataset["total_bill"], bins = 10, kde =False, fit = norm, color="red" )


# In[16]:


sns.distplot(tips_dataset["total_bill"], bins = 10, kde =False, fit = norm, color="red",
            vertical = True)


# In[17]:


sns.distplot(tips_dataset["total_bill"], bins = 10, kde =False, fit = norm, color="red" , norm_hist=True)


# In[23]:


sns.distplot(tips_dataset["total_bill"], bins = 10, kde =False, fit = norm, color="red" , norm_hist=True, 
             axlabel = "Total Bill", label = "Historagm total bill")
plt.title("Histogram of Total Bill")
plt.legend(loc = 1)
plt.show()


# In[25]:


plt.figure(figsize=(16,9))
sns.set()
sns.distplot(tips_dataset["total_bill"], bins = 10, kde =False, fit = norm, color="red" , norm_hist=True, 
             axlabel = "Total Bill", label = "Historagm total bill")
plt.title("Histogram of Total Bill")
plt.legend(loc = 1)
plt.show()


# In[27]:


tips_dataset.total_bill.sort_values()


# In[32]:


bin = list(np.arange(0,60, 5))
bin


# In[35]:


plt.figure(figsize=(16,9))
sns.set()
sns.distplot(tips_dataset["total_bill"], kde =False, fit = norm, color="red" , norm_hist=True, 
             axlabel = "Total Bill", label = "Historagm total bill")
plt.title("Histogram of Total Bill")
plt.xticks(bin)
plt.legend(loc = 1)
plt.show()


# In[38]:


plt.figure(figsize=(16,9))
sns.set()
sns.distplot(tips_dataset["total_bill"], bins= bin, kde =False, fit = norm, color="red" , norm_hist=True, 
              label = "Historagm total bill")
plt.title("Histogram of Total Bill")
plt.legend(loc = 1)
plt.show()


# In[43]:


sns.distplot(tips_dataset["total_bill"],hist_kws={"color":"#DC143C", "edgecolor":"#AA4545", "linewidth":2, "linestyle":"--","alpha":0.9},)
plt.title("Histogram of Total Bill")
plt.legend(loc = 1)
plt.show()


# In[50]:


plt.figure(figsize=(16,9))
sns.set()
sns.distplot(tips_dataset["total_bill"],hist_kws={"color":"#DC143C", "edgecolor":"#AA4545", "linewidth":2, "linestyle":"--",
                                                  "alpha":0.9},
            kde_kws={"color":"#AAA45C",  "linewidth":5, "linestyle":"--",
                                                  "alpha":0.9},rug = True,
            rug_kws={"color":"#BBB45C", "linewidth":2, "linestyle":"--",
                                                  "alpha":0.9})
plt.title("Histogram of Total Bill")
# plt.legend(loc = 1)
plt.show()


# In[ ]:




