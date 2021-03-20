#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import random
import numpy as np


# In[2]:


ml_student_age = np.random.randint(18,45,(100))
py_student_age = np.random.randint(15,40,(100))


# In[3]:


print(ml_student_age)
print(py_student_age)


# In[4]:


plt.hist(ml_student_age, label = "student age")
plt.title("Machine Learning Student Age Histogram", fontsize = 30)
plt.xlabel("Student age category")
plt.ylabel("No. Student Age")
plt.legend(loc = 1)
plt.show()


# In[5]:


bins = [15,20,25,30,35,40,45,50]
plt.hist(ml_student_age, bins, rwidth = 0.8, label = "student age")
plt.title("Machine Learning Student Age Histogram", fontsize = 30)
plt.xlabel("Student age category")
plt.ylabel("No. Student Age")
plt.legend(loc = 1)
plt.show()


# In[6]:


bins = [15,20,25,30,35,40,45,50]
plt.hist(ml_student_age, bins, rwidth = 0.8, histtype = 'barstacked',align = 'mid',orientation = 'horizontal', color = 'm',  label = "student age")
plt.title("Machine Learning Student Age Histogram", fontsize = 30)
plt.xlabel("Student age category")
plt.ylabel("No. Student Age")
plt.legend(loc = 1)
plt.show()


# In[7]:


bins = [15,20,25,30,35,40,45,50]
plt.hist(ml_student_age, bins, rwidth = 0.8, histtype = 'barstacked',align = 'mid',orientation = 'vertical', color = 'm',  label = "ML student age")
plt.hist(py_student_age, bins, rwidth = 0.8, histtype = 'barstacked',align = 'mid',orientation = 'vertical', color = 'y',  label = "PY student age")
plt.title("Machine Learning Student Age Histogram", fontsize = 30)
plt.xlabel("Student age category")
plt.ylabel("No. Student Age")
plt.legend(loc = 1)
plt.show()


# In[8]:


bins = [15,20,25,30,35,40,45,50]
plt.figure(figsize=(16,9))
plt.hist([ml_student_age,py_student_age], bins, rwidth = 0.8, histtype = 'bar',
         orientation = 'vertical', color = ["m","y"],  label = ["ML student age", "PY Student Age"])
#plt.hist(py_student_age, bins, rwidth = 0.8, histtype = 'barstacked',align = 'mid',orientation = 'vertical', color = 'y',  label = "PY student age")
plt.title("Machine Learning Student Age Histogram", fontsize = 30)
plt.xlabel("Student age category")
plt.ylabel("No. Student Age")
plt.legend(loc = 1)
plt.show()


# In[9]:


from matplotlib import style
bins = [15,20,25,30,35,40,45,50]
style.use("ggplot")
plt.figure(figsize=(16,9))
plt.hist([ml_student_age,py_student_age], bins, rwidth = 0.8, histtype = 'bar',
         orientation = 'vertical', color = ["m","y"],  label = ["ML student age", "PY Student Age"])
#plt.hist(py_student_age, bins, rwidth = 0.8, histtype = 'barstacked',align = 'mid',orientation = 'vertical', color = 'y',  label = "PY student age")
plt.title("Machine Learning Student Age Histogram", fontsize = 30)
plt.xlabel("Student age category")
plt.ylabel("No. Student Age")
plt.grid(color = 'b', linewidth = 2)
plt.legend(loc = 1)
plt.show()


# In[ ]:




