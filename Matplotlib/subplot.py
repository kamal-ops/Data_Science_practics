#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
from matplotlib import style


# In[2]:


plt.subplot(2,2,1)
plt.pie([1])

plt.subplot(2,2,2)
plt.pie([1, 2])

plt.subplot(2,2,3)
plt.pie([1,2,3])

plt.subplot(2,2,4)
plt.pie([1,2,3,4])

plt.show()


# In[17]:


plt.figure(figsize=(16,9))
plt.subplot(3,2,1)
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

plt.subplot(3,2,2)
ml_student_age = np.random.randint(18,45,(100))
py_student_age = np.random.randint(15,40,(100))

bins = [15,20,25,30,35,40,45,50]
plt.hist(ml_student_age, bins, rwidth = 0.8, label = "student age")
plt.title("Machine Learning Student Age Histogram", fontsize = 30)
plt.xlabel("Student age category")
plt.ylabel("No. Student Age")
plt.legend(loc = 1)

plt.subplot(3,2,3)
classes = ["Python", "R", "ML", "AI", "DS"]
class1_students = [30,10,20,25,10]
class2_students = [45,5,20,20,10]
class3_students = [35,5,30,15,15]
# plt.figure(figsize=(16,9))
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

plt.subplot(3,2,4)
df_google_playstore = pd.read_csv("H:\\data_science\\datasets\\archive\\googleplaystore.csv", nrows = 1000)
x = df_google_playstore["Rating"]
y = df_google_playstore["Reviews"]
# plt.figure(figsize=(16,9))
plt.scatter(x, y, color = 'r', marker = "*")#verts="<"
plt.scatter(x,df_google_playstore["Installs"], color = 'b', marker = "o")#verts="<"
plt.title("Google play store apps scatter plot", fontsize = 25)
plt.xlabel("Rating")
plt.ylabel("Reviews and Install")

plt.subplot(3,2,5)

classes = ["Python", "R", "ML", "AI", "DS"]
class1_students = [30,10,20,25,10]
class2_students = [45,5,20,20,10]
class3_students = [35,5,30,15,15]

explode = [0.03,0,0.2,0,0]
colors=['c','m','r','g','b']
# plt.figure(figsize=(16,9))
textprops={"fontsize":15}
wedgeprops={"linewidth": 4, "width":1, "edgecolor":"k"}
plt.pie(class1_students, labels=classes, explode=explode, colors=colors, autopct="%0.2f%%", shadow=True, radius=1, 
        startangle=270, textprops=textprops, rotatelabels=True, frame=True, counterclock=True, labeldistance=1.2,
        pctdistance=0.6, wedgeprops=wedgeprops
       )

plt.legend()


plt.subplot(3,2,6, projection="polar", facecolor="k", frameon=True)


plt.show()


# In[ ]:




