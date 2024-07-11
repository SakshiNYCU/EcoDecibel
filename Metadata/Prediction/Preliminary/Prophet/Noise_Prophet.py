#!/usr/bin/env python
# coding: utf-8

# # 1 Prophet

# # Dependencies

# In[1]:


import warnings; 
warnings.simplefilter('ignore')


# In[2]:


get_ipython().system('pip install pystan==2.19.1.1')


# In[3]:


get_ipython().system('pip install pandas fbprophet')


# In[4]:


import pandas as pd
from fbprophet import Prophet


# # Processing Dataset

# In[5]:


df = pd.read_csv('G:/My Drive/NYCU/Research/Noise_Forecasting/Prophet/Noise_DateStamp.csv')


# In[6]:


#df.head()
#df.describe()
#print (df['ID'].unique())
df.dtypes


# In[7]:


df['Year'] = df['DateStamp'].apply(lambda x: str(x)[-8:-6])
df['Month'] = df['DateStamp'].apply(lambda x: str(x)[-13:-11])
df['Day'] = df['DateStamp'].apply(lambda x: str(x)[-16:-14])
df['ds'] = pd.DatetimeIndex(df['Day']+'-'+df['Month']+'-'+df['Year'])

#df.dtypes
df.head()


# In[8]:


#df = df.loc[(df['ID']==A01)
df.drop(['ID', 'DateStamp', 'Year', 'Month', 'Day'], axis=1, inplace=True)
df.columns = ['y', 'ds']
df.head()


# # Model Training

# In[10]:


m = Prophet(interval_width=0.95)
model = m.fit(df)


# # Forecasting

# In[26]:


future = m.make_future_dataframe(periods=100,freq='M')
forecast = m.predict(future)
forecast.head()


# In[27]:


#forecast.tail()
forecast[['ds','yhat']]


# # Plot

# In[28]:


plot1 = m.plot(forecast)


# In[29]:


plt2 = m.plot_components(forecast)

