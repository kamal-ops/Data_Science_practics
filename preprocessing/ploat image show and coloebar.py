#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# In[3]:


img = mpimg.imread("C:\\Users\\Kamal\\Downloads\\images\\images (1).jfif")


# In[4]:


img


# In[5]:


type(img)


# In[6]:


img.shape


# In[7]:


img.ndim


# In[11]:


plt.figure(figsize=(16,9))
plt.axis("off")
plt.imshow(img)

plt.show()


# In[12]:


plt.figure(figsize=(16,9))
plt.axis("off")
plt.imshow(img)
plt.colorbar()
plt.show()


# In[16]:


plt.figure(figsize=(16,9))
plt.axis("off")
plt.imshow(img, cmap="Accent")
plt.colorbar()
plt.show()


# In[17]:


single_channel = img[:,:,1]
plt.figure(figsize=(16,9))
plt.axis("off")
plt.imshow(single_channel, cmap="Accent")
plt.colorbar()
plt.show()


# In[ ]:




