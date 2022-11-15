#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import plotly as plot
import plotly.express as px
import plotly.graph_objs as go
import cufflinks as cf
import matplotlib.pyplot as plt
import seaborn as sns


# In[19]:


df=pd.read_csv("Heart_Disease_Prediction.csv")
df.head()


# In[20]:


info = ["age","1: male, 0: female","chest pain type, 1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic","resting blood pressure"," serum cholestoral in mg/dl","fasting blood sugar > 120 mg/dl","resting electrocardiographic results (values 0,1,2)"," maximum heart rate achieved","exercise induced angina","oldpeak = ST depression induced by exercise relative to rest","the slope of the peak exercise ST segment","number of major vessels (0-3) colored by flourosopy","thal: 3 = normal; 6 = fixed defect; 7 = reversable defect"]



for i in range(len(info)):
    print(df.columns[i]+":\t\t\t"+info[i])


# In[21]:


df.groupby('Heart Disease').size()


# In[22]:


df.groupby('Heart Disease').sum()


# In[25]:


df.shape


# In[26]:


df.describe()


# In[27]:


df.info()


# In[28]:


df['Heart Disease'].unique()


# In[29]:


df.hist(figsize=(14,14))
plt.show()


# In[30]:


df['Heart Disease'].value_counts()


# In[31]:


df['Heart Disease'].isnull()


# In[32]:


df['Heart Disease'].sum()


# In[33]:


df['Heart Disease'].unique()


# In[34]:


df.isnull().sum()


# In[ ]:




