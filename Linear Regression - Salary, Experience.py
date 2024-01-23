#!/usr/bin/env python
# coding: utf-8

# # Linear Regression

# # Years of Experience and Salary

# In[53]:


import pandas as pd
import matplotlib.pyplot as plt


# In[54]:


import matplotlib.pyplot as plt
url = 'https://raw.githubusercontent.com/ameer-fice/ai-vodafone/main/datasets/Salary_Data.csv'
df = pd.read_csv(url)
print(df.head())


# In[55]:


url = 'https://raw.githubusercontent.com/ameer-fice/ai-vodafone/main/datasets/Salary_Data.csv'
df = pd.read_csv(url)
print(df.columns)


# In[56]:


url = 'https://raw.githubusercontent.com/ameer-fice/ai-vodafone/main/datasets/Salary_Data.csv'
df = pd.read_csv(url)
df.plot.scatter(x='YearsExperience', y='Salary')
plt.show()


# In[57]:


x = df.iloc[:,[0]]
y = df.iloc[:,[1]]


# In[58]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)
y_predict = model.predict(x)
y_predict


# In[59]:


y


# In[60]:


model.coef_


# In[61]:


model.intercept_


# In[62]:


#y = mx+c
y = (9499*15)+25792
print(y)


# In[63]:


import matplotlib.pyplot as plt
plt.scatter(df['YearsExperience'],df['Salary'])
plt.plot(x,y_predict,c='r')
for i in range(len(x)):
    plt.plot([x[i],x[i]],[y[i],y_predict[i]],c='k',linestyle='--')
plt.show


# In[65]:


print(type(y_predict))
print(type(y))
from sklearn.metrics import mean_squared_error, r2_score
print(mean_squared_error(y_predict,y,squared=False))
print(r2_score(y_predict,y))


# # 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




