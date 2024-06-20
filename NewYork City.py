#!/usr/bin/env python
# coding: utf-8

# # Task 2:
# # Cleaning Data

# ###### 1)Data Integrity: Ensuring the accuracy, consistency, and reliability of data throughout the cleaning process.
# ###### 2)Missing Data Handling: Dealing with missing values by either imputing them or making informed decisions on how to handle gaps in the dataset.
# ###### 3)Duplicate Removal: Identifying and eliminating duplicate records to maintain data uniqueness.
# ###### 4)Standardization: Consistent formatting and units across the dataset for accurate analysis.
# ###### 5)Outlier Detection: Identifying and addressing outliers that may skew analysis or model performance.
# 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as ex
import seaborn as sns 
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df=pd.read_csv(r"C:\Users\tejas\OneDrive\Desktop\Machine Leaening\archive (19)\AB_NYC_2019.csv")


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


(df.isna().sum()/df.shape[0])*100


# ###### Four Columns Have a null vlaue Name,Host_Name, Last Reviews,reviews per month .
# 
# Columns last_reviews and reviews_per_month has a more null values

# In[7]:


df["name"].value_counts()


# In[ ]:





# # Data Cleaning 

# In[8]:


df["name"].isna().sum()


# ## Missing Data Handling

# In[9]:


mode_value1=df["name"].mode()[0]
mode_value2=df["host_name"].mode()[0]


# In[10]:


df["name"].fillna(mode_value1,inplace=True)
df["host_name"].fillna(mode_value2,inplace=True)


# ###### name and host_name have object type data. we fill the null value by using mode of that columns 

# In[11]:


print(df["name"].isna().sum())
print(df["host_name"].isna().sum())


# In[12]:


mode_value3=df["reviews_per_month"].mode()[0]


# ### Standardization

# In[13]:


df["last_review"]=df["last_review"].astype("datetime64")
df["last_review"].info()


# ###### last review column have object type of data but it is in a date time format so we convert it into datetime.

# In[14]:


mode_value4=df["last_review"].mean()


# In[15]:


df["reviews_per_month"].fillna(mode_value3,inplace=True)
df["last_review"].fillna(mode_value4,inplace=True)


# ### Duplicate Removal

# In[16]:


df.duplicated().sum()


# #####  Data set  Don't have duplicate values.

# In[17]:


df.info()


# In[18]:


df.columns


# ## Outlier Detection

# In[19]:


ax = df.boxplot(
        column=['latitude', 'longitude',
       'minimum_nights', 'number_of_reviews',
       'reviews_per_month', 'calculated_host_listings_count',
       'availability_365'], 
        #by='ISBOT',
        figsize=(12, 8),     
        grid=True 
       );

plt.title("Boxplot of Kaggle");
plt.show()


# In[20]:


#sns.boxplot(data=df, x="price", y=, hue=None, order=None, hue_order=None, orient=None, color=None)


# In[21]:


df["latitude"].describe()


# In[ ]:





# In[23]:


ex.box(df["price"])


# ###### price have maximum value 10k 
# 50% values have price 106.
# 
# 75% values have price 175

# In[24]:


(df["price"]>800).sum()


# ###### 

# In[25]:


df=df[df["price"]<800].reset_index(drop=True)
df.head(1)


# ##### we remove values which is more then 800 .

# In[26]:


ex.box(df["price"])


# In[27]:


ex.box(df["minimum_nights"])


# In[28]:


ex.box(df["minimum_nights"])


# In[29]:


(df["minimum_nights"]>30).sum()


# In[30]:


df=df[df["minimum_nights"]<30].reset_index(drop=True)


# In[31]:


ex.box(df["minimum_nights"])


# In[32]:


ex.box(df["number_of_reviews"])


#   ##### number of reviews have maximum value 629
#   ##### median value is 6 and 75 % data have 26

# In[33]:


(df["number_of_reviews"]>200).sum()


# In[34]:


df=df[df["number_of_reviews"]<=200].reset_index(drop=True)


# ###### we remove value which is more then 200

# In[35]:


ex.box(df["number_of_reviews"])


# In[36]:


ex.box(df["calculated_host_listings_count"])


# ######  calculated_host_listings_count have max value 327

# In[37]:


(df["calculated_host_listings_count"]>20).sum()


# In[38]:


df=df[df["calculated_host_listings_count"]<=20].reset_index(drop=True)


# ######  we remove value more then 20

# In[39]:


ex.box(df["calculated_host_listings_count"])


# In[ ]:





# In[ ]:





# In[ ]:




