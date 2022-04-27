#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import os


# In[3]:


fileName=r'Bid Tracking Spreadsheet'
filePath=r'C:\Users\bayle\Downloads\Bid Tracking Spreadsheet.xlsx'
file=os.path.join(filePath,fileName)


# In[5]:


df=pd.read_excel(r'C:\Users\bayle\Downloads\Bid Tracking Spreadsheet.xlsx',sheet_name='February', skiprows=1)


# In[6]:


df


# In[7]:


df=df[~pd.isnull(df['Date'])]


# In[8]:


df


# In[10]:


estimators=df['Estimator'].values.tolist()


# In[11]:


estimators=list(set(estimators))


# In[12]:


df['Price'].max()


# In[13]:


#{'Highest Bid' : x, 'Most Bids' : y, 'Highest Win Percentage' : z} 


# In[14]:


bidding_dict={} #create the dictionary


# In[15]:


maxBidder=df[df['Price']==df['Price'].max()]['Estimator'].values[0] #get the max bidder


# In[16]:


bidding_dict['Highest Bid']=maxBidder #assign the max bidder to the dictionary


# In[17]:


bidding_dict


# In[18]:


df1=pd.DataFrame(df.groupby(['Estimator'])['Project Name'].count())


# In[19]:


df1


# In[20]:


df1.reset_index(inplace=True)


# In[21]:


df1


# In[22]:


max_bids=df1['Project Name'].max()
max_bids


# In[23]:


mostBidder=df1[df1['Project Name']==max_bids]['Estimator'].values[0]


# In[24]:


mostBidder


# In[25]:


bidding_dict['Most Bids']=mostBidder


# In[26]:


bidding_dict


# In[28]:


bid_list=[]
for e in estimators:
    #print(e)
    y_bids=df[(df['Estimator']==e) & (df['Won?']=='Y')].shape[0]
    n_bids=df[(df['Estimator']==e) & (df['Won?']=='N')].shape[0]
    bid_percentage=y_bids/(y_bids+n_bids)
    bid_list.append(bid_percentage)
#zipped_list=list(zip(estimators,bid_list))
index_of_winner=bid_list.index(max(bid_list))
bidding_dict['Highest Winning Percentage']=estimators[index_of_winner]


# In[29]:


bid_list


# In[30]:


#max(bid_list)


# In[34]:


estimators


# In[36]:


estimators[0]


# In[37]:


bidding_dict


# In[38]:


df=pd.DataFrame()


# In[39]:


cols=list(bidding_dict.keys())


# In[40]:


cols


# In[41]:


data=list(bidding_dict.values())


# In[42]:


data


# In[43]:


df1=pd.DataFrame(data=[data],columns=cols)


# In[44]:


df1


# In[46]:


xlr=pd.ExcelWriter(file)
df1.to_excel(xlr,'Winners')
xlr.save()
