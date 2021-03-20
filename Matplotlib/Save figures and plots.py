#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
from matplotlib import style


# In[2]:


plt.pie([40,30,20])
plt.savefig("piecharrt2", dpi=100, quality=100, facecolor="g")


# """Signature: plt.savefig(*args, **kwargs)
# Docstring:
# Save the current figure.
# 
# Call signature::
# 
#   savefig(fname, dpi=None, facecolor='w', edgecolor='w',
#           orientation='portrait', papertype=None, format=None,
#           transparent=False, bbox_inches=None, pad_inches=0.1,
#           frameon=None, metadata=None)
# 
# The available output formats depend on the backend being used.
# 
# Parameters
# ----------
# fname : str or path-like or file-like
#     A path, or a Python file-like object, or
#     possibly some backend-dependent object such as
#     `matplotlib.backends.backend_pdf.PdfPages`.
# 
#     If *format* is set, it determines the output format, and the file
#     is saved as *fname*.  Note that *fname* is used verbatim, and there
#     is no attempt to make the extension, if any, of *fname* match
#     *format*, and no extension is appended.
# 
#     If *format* is not set, then the format is inferred from the
#     extension of *fname*, if there is one.  If *format* is not
#     set and *fname* has no extension, then the file is saved with
#     :rc:`savefig.format` and the appropriate extension is appended to
#     *fname*.
# 
# Other Parameters
# ----------------
# dpi : float or 'figure', default: :rc:`savefig.dpi`
#     The resolution in dots per inch.  If 'figure', use the figure's
#     dpi value.
# 
# quality : int, default: :rc:`savefig.jpeg_quality`
#     Applicable only if *format* is 'jpg' or 'jpeg', ignored otherwise.
# 
#     The image quality, on a scale from 1 (worst) to 95 (best).
#     Values above 95 should be avoided; 100 disables portions of
#     the JPEG compression algorithm, and results in large files
#     with hardly any gain in image quality.
# 
#     This parameter is deprecated.
# 
# optimize : bool, default: False
#     Applicable only if *format* is 'jpg' or 'jpeg', ignored otherwise.
# 
#     Whether the encoder should make an extra pass over the image
#     in order to select optimal encoder settings.
# 
#     This parameter is deprecated.
# 
# progressive : bool, default: False
#     Applicable only if *format* is 'jpg' or 'jpeg', ignored otherwise.
# 
#     Whether the image should be stored as a progressive JPEG file.
# 
#     This parameter is deprecated.
# 
# facecolor : color or 'auto', default: :rc:`savefig.facecolor`
#     The facecolor of the figure.  If 'auto', use the current figure
#     facecolor.
# 
# edgecolor : color or 'auto', default: :rc:`savefig.edgecolor`
#     The edgecolor of the figure.  If 'auto', use the current figure
#     edgecolor.
# 
# orientation : {'landscape', 'portrait'}
#     Currently only supported by the postscript backend.
# 
# papertype : str
#     One of 'letter', 'legal', 'executive', 'ledger', 'a0' through
#     'a10', 'b0' through 'b10'. Only supported for postscript
#     output.
# 
# format : str
#     The file format, e.g. 'png', 'pdf', 'svg', ... The behavior when
#     this is unset is documented under *fname*.
# 
# transparent : bool
#     If *True*, the axes patches will all be transparent; the
#     figure patch will also be transparent unless facecolor
#     and/or edgecolor are specified via kwargs.
#     This is useful, for example, for displaying
#     a plot on top of a colored background on a web page.  The
#     transparency of these patches will be restored to their
#     original values upon exit of this function.
# 
# bbox_inches : str or `.Bbox`, default: :rc:`savefig.bbox`
#     Bounding box in inches: only the given portion of the figure is
#     saved.  If 'tight', try to figure out the tight bbox of the figure.
# 
# pad_inches : float, default: :rc:`savefig.pad_inches`
#     Amount of padding around the figure when bbox_inches is 'tight'.
# 
# bbox_extra_artists : list of `~matplotlib.artist.Artist`, optional
#     A list of extra artists that will be considered when the
#     tight bbox is calculated.
# 
# backend : str, optional
#     Use a non-default backend to render the file, e.g. to render a
#     png file with the "cairo" backend rather than the default "agg",
#     or a pdf file with the "pgf" backend rather than the default
#     "pdf".  Note that the default backend is normally sufficient.  See
#     :ref:`the-builtin-backends` for a list of valid backends for each
#     file format.  Custom backends can be referenced as "module://...".
# 
# metadata : dict, optional
#     Key/value pairs to store in the image metadata. The supported keys
#     and defaults depend on the image format and backend:
# 
#     - 'png' with Agg backend: See the parameter ``metadata`` of
#       `~.FigureCanvasAgg.print_png`.
#     - 'pdf' with pdf backend: See the parameter ``metadata`` of
#       `~.backend_pdf.PdfPages`.
#     - 'svg' with svg backend: See the parameter ``metadata`` of
#       `~.FigureCanvasSVG.print_svg`.
#     - 'eps' and 'ps' with PS backend: Only 'Creator' is supported.
# 
# pil_kwargs : dict, optional
#     Additional keyword arguments that are passed to
#     `PIL.Image.Image.save` when saving the figure.
# File:      c:\users\kamal\anaconda3\lib\site-packages\matplotlib\pyplot.py
# Type:      function"""

# In[5]:


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


plt.savefig("Subplot", )

plt.show()


# In[ ]:




