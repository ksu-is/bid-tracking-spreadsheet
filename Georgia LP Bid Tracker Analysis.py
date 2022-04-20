#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os


# In[2]:


fileName=r'Bid Tracking Spreadsheet'
filePath=r'C:\Users\bayle\Downloads\Bid Tracking Spreadsheet.xlsx'
file=os.path.join(filePath,fileName)
print(file)


# In[10]:


df=pd.read_excel(r'C:\Users\bayle\Downloads\Bid Tracking Spreadsheet.xlsx',sheet_name='February', skiprows=1)


# In[11]:


df.shape


# In[12]:


df=df.iloc[[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],]


# In[ ]:




