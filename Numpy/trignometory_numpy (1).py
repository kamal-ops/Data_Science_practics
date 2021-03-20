#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[4]:


np.sin(180)


# In[6]:


np.sin(90)


# In[7]:


np.cos(180)


# In[8]:


np.tan(180)


# In[9]:


x_sin = np.arange(0, 3*np.pi, 0.1)
y_sin = np.sin(x_sin)


# In[10]:


plt.plot(x_sin, y_sin)
plt.show()


# In[11]:


y_cos = np.cos(x_sin)
plt.plot(x_sin, y_cos)
plt.show()


# In[12]:


y_tan = np.tan(x_sin)
plt.plot(x_sin, y_tan)
plt.show()


# In[ ]:




