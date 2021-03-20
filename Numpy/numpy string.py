#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


str1 = "kamal kishor swami"
str2 = "asiistant pipline developer"


# In[3]:


np.char.add(str1, str2)


# In[4]:


np.char.lower(str1)


# In[5]:


np.char.upper(str1)


# In[8]:


np.char.center(str1, 60)


# In[9]:


np.char.center(str1, 60, fillchar="*")


# In[11]:


np.char.replace(str1,"kamal kishor swami",  "Palak Swami")


# In[12]:


np.char.count(str1, "a")


# In[14]:


np.char.find(str1, "kamal")


# In[16]:


np.char.title(str1)


# In[ ]:




