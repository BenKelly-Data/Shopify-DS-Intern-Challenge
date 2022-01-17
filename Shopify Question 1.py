#!/usr/bin/env python
# coding: utf-8

# In[100]:


#Retreiving Data
import pandas as pd

sheet_url = 'https://docs.google.com/spreadsheets/d/16i38oonuX1y1g7C_UAmiK9GkY7cS-64DfiDMNiR41LM/edit#gid=0'
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
shopDat = pd.read_csv(url_1)     


# In[101]:


# Quick Data Viewing with boxplot
import seaborn as sns
sns.boxplot(x=shopDat['order_amount'])


# In[102]:


#Another quick plot to further understand data
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(16,8))
ax.scatter(shopDat['order_amount'], shopDat['total_items'])
ax.set_xlabel('Order Amount')
ax.set_ylabel('Number of Items')
plt.show()


# In[103]:


#Find the z-scores (distance from mean) from the odd outliers
from scipy import stats
import numpy as np
z = np.abs(stats.zscore(shopDat['order_amount']))


# In[104]:


#Test different z-score thresholds to capture outliers best
outliers = np.where(z > 0.1)

#Select the outliers from the data
toRemove=shopDat.iloc[outliers]


# In[105]:


#Check which shop id's create the outliers
cleanDat=shopDat.drop(toRemove.index)

#cleanDat['shop_id'].unique()
toRemove['shop_id'].unique()


# In[106]:



#shopDat['order_amount'].median()
#cleanDat['order_amount'].median()

#shopDat['order_amount'].mean()
cleanDat['order_amount'].mean()

