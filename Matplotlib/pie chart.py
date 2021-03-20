#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np


# In[6]:


classes = ["Python", "R", "ML", "AI", "DS"]
class1_students = [30,10,20,25,10]
class2_students = [45,5,20,20,10]
class3_students = [35,5,30,15,15]

plt.pie(class1_students, labels=classes)
plt.show()


# In[57]:


classes = ["Python", "R", "ML", "AI", "DS"]
class1_students = [30,10,20,25,10]
class2_students = [45,5,20,20,10]
class3_students = [35,5,30,15,15]

explode = [0.03,0,0.2,0,0]
colors=['c','m','r','g','b']
plt.figure(figsize=(16,9))
textprops={"fontsize":15}
wedgeprops={"linewidth": 4, "width":1, "edgecolor":"k"}
plt.pie(class1_students, labels=classes, explode=explode, colors=colors, autopct="% .2f%%", shadow=True, radius=1.4, 
        startangle=270, textprops=textprops, rotatelabels=True, frame=True, center=(2,3), counterclock=True, labeldistance=1.2,
        pctdistance=0.6, wedgeprops=wedgeprops
       )

plt.legend()
plt.show()


# In[ ]:




