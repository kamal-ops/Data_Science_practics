#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib import style


# In[2]:


classes = ["Python", "R", "ML", "AI", "DS"]
class1_students = [30,10,20,25,10]
class2_students = [45,5,20,20,10]
class3_students = [35,5,30,15,15]
#class4_students = []
#class5_students = []


# In[3]:


plt.bar(classes, class1_students)
plt.show()


# In[4]:


plt.barh(classes, class1_students)
plt.show()


# In[5]:


plt.bar(classes, class1_students, width = 0.2, align= 'edge', color = 'y', edgecolor = 'm',
       linewidth = 1, alpha = 0.9, linestyle = '--', label = "Class 1 Students", visible = False)
plt.legend()
plt.show()


# In[6]:


style.use("ggplot")
plt.figure(figsize=(16,9))
plt.bar(classes, class1_students, width = 0.6, align= 'edge', color = 'k', edgecolor = 'm',
       linewidth = 1, alpha = 0.9, linestyle = '--', label = "Class 1 Students", visible = True)
plt.title("Class 1 Students", fontsize = 25)
plt.xlabel("Class Name")
plt.ylabel("No. of Students")
plt.legend()
plt.show()


# In[7]:


plt.figure(figsize=(16,9))
plt.bar(classes, class1_students, width = 0.6, align= 'center', color = 'k', edgecolor = 'm',
       linewidth = 1, alpha = 0.9, linestyle = '--', label = "Class 1 Students", visible = True)
plt.title("Class 1 Students", fontsize = 25)
plt.xlabel("Class Name")
plt.ylabel("No. of Students")
plt.legend()
plt.show()


# In[8]:


plt.figure(figsize=(16,9))
plt.bar(classes, class1_students, width = 0.3, align= 'center', color = 'r', edgecolor = 'm',
       linewidth = 1, alpha = 0.9, linestyle = '--', label = "Class 1 Students", visible = True)
plt.bar(classes, class2_students, width = 0.3, align= 'center', color = 'g', edgecolor = 'm',
       linewidth = 1, alpha = 0.9, linestyle = '--', label = "Class 2 Students", visible = True)
plt.bar(classes, class3_students, width = 0.3, align= 'center', color = 'b', edgecolor = 'm',
       linewidth = 1, alpha = 0.9, linestyle = '--', label = "Class 3 Students", visible = True)
plt.title("Class 1 Students", fontsize = 25)
plt.xlabel("Class Name")
plt.ylabel("No. of Students")
plt.legend()
plt.show()


# In[9]:


plt.figure(figsize=(16,9))
class_index = np.arange(len(classes))
width = 0.2
plt.bar(class_index, class1_students, width, color = 'r', label = "Class 1 Students")

plt.bar(class_index + width, class2_students, width , color = 'g', label = "Class 2 Students")

plt.bar(class_index+width+width, class3_students,width, color = 'b', label = "Class 3 Students")

plt.xticks(class_index+width, classes, rotation = 90)
plt.title("Class 1 Students", fontsize = 25)
plt.xlabel("Class Name")
plt.ylabel("No. of Students")
plt.legend()
plt.show()


# In[10]:


plt.figure(figsize=(16,9))
class_index = np.arange(len(classes))
width = 0.2
plt.barh(class_index, class1_students, width, color = 'r', label = "Class 1 Students")

plt.barh(class_index + width, class2_students, width , color = 'g', label = "Class 2 Students")

plt.barh(class_index+width+width, class3_students,width, color = 'b', label = "Class 3 Students")

plt.yticks(class_index+width, classes, rotation = 90)
plt.title("Class 1 Students", fontsize = 25)
plt.ylabel("Class Name")
plt.xlabel("No. of Students")
plt.legend()
plt.show()


# In[ ]:




