#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[6]:


import matplotlib.pyplot as plt
url = 'https://raw.githubusercontent.com/ameer-fice/ai-vodafone/main/datasets/Melbourne_housing_FULL.csv'
df = pd.read_csv(url)
print(df.head())


# In[13]:


df.shape


# In[15]:


df.info


# In[14]:


url = 'https://raw.githubusercontent.com/ameer-fice/ai-vodafone/main/datasets/Melbourne_housing_FULL.csv'
df = pd.read_csv(url)
print(df.columns)


# In[8]:


x = df.iloc[:,[0]].values
y = df.iloc[:,[1]].values
print(type(x))
print(type(y))


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
url = 'https://raw.githubusercontent.com/ameer-fice/ai-vodafone/main/datasets/Melbourne_housing_FULL.csv'
df = pd.read_csv(url)
# Plotting
plt.scatter(df['Suburb'], df['BuildingArea'])
plt.title('Suburb vs BuildingArea')
plt.xlabel('Suburb')
plt.ylabel('BuildingArea')
#plt.grid(True)
plt.show()


# In[16]:


num_col = df.dtypes[df.dtypes!='object'].index.values
cat_col = df.dtypes[df.dtypes=='object'].index.values
cat_col


# In[18]:


df[cat_col].nunique()
#checking number of unique values


# In[27]:


for col in cat_col:
    if df[col].nunique() >50:
        df = df.drop(col,axis=1)
#res['Price'] = df['Price']


# In[25]:


df.head()


# In[30]:


a = df[['Rooms','Bedroom2']].dropna()
(a['Rooms']==a['Bedroom2']).value_counts()


# In[31]:


948/25692*100


# In[34]:


df = df.drop(columns=['Bedroom2','Lattitude','Longtitude','Postcode'])
df.head()


# In[38]:


col = ['Distance','Bathroom','Car','PropertyCount']
df[col] = df[col].fillna(0)
df['Landsize'] = df['Landsize'].fillna(df['Landsize'].mean())
df['BuildingArea'] = df['BuildingAreaa'].fillna(df['BuildingArea'].mean())
df['YearBuilt'] = 2024-df['YearBuilt']
df = dfdrop.na()


# In[39]:


df2 = df.copy().select_dtypes(exclude = ['object'])
df2.head(2)


# In[37]:


for i in df2.columns:
    plt.scatter(df[i],df['Price'])
    plt.show()


# In[ ]:




