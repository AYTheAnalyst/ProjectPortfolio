#!/usr/bin/env python
# coding: utf-8

# In[22]:


import os, shutil


# In[23]:


path = r"/Users/abhishek/Downloads/"


# In[24]:


file_name = os.listdir(path)


# In[25]:


folder_names = ['csvfiles', 'pngfiles', 'excelfiles','jpgfiles', 'jpegfiles']

for loop in range(0,5):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs(path + folder_names[loop])
    


# In[28]:


for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csvfiles/" + file):
        shutil.move(path + file, path + "csvfiles/" + file)
    elif ".png" in file and not os.path.exists(path + "pngfiles/" + file):
        shutil.move(path + file, path + "pngfiles/" + file)
    elif ".xls" in file and not os.path.exists(path + "excelfiles/" + file):
        shutil.move(path + file, path + "excelfiles/" + file)
    elif ".jpg" in file and not os.path.exists(path + "jpgfiles/" + file):
        shutil.move(path + file, path + "jpgfiles/" + file)
    elif ".jpeg" in file and not os.path.exists(path + "jpegfiles/" + file):
        shutil.move(path + file, path + "jpegfiles/" + file)
        
        


# In[ ]:




