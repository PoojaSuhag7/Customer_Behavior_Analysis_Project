#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd

df = pd.read_csv('customer_shopping_behavior.csv')


# In[42]:


df.head()


# In[44]:


df.info()


# In[46]:


df.describe(include="all")


# In[38]:


df.isnull().sum()


# In[48]:


df['Review Rating'].describe()


# In[50]:


df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))


# In[52]:


df.isnull().sum()


# In[54]:


df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})


# In[56]:


df.columns


# In[58]:


#Feature Enginnering
# Create a column age_group
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)


# In[60]:


df[['age', 'age_group']].head(10)


# In[62]:


# Create column purchase_frequency_days

frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annualy': 365,
    'Every 3 months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)


# In[64]:


df[['purchase_frequency_days','frequency_of_purchases']].head(10)


# In[66]:


df[['discount_applied','promo_code_used']].head(10)


# In[68]:


(df['discount_applied'] == df['promo_code_used']).all()


# In[70]:


df = df.drop('promo_code_used', axis=1)


# In[72]:


df.columns


# In[74]:


get_ipython().system('pip install mysql-connector-python sqlalchemy')


# In[84]:


from sqlalchemy import create_engine

# MySQL details
Username = "root"
Password = "@suhag123"
Database = "customer_behavior"
table_name = "customer_data"

# Create connection
engine = create_engine(
    "mysql+mysqlconnector://root:%40suhag123@localhost/customer_behavior"
)

# Load DataFrame into MySQL
df.to_sql(
    table_name,
    con=engine,
    if_exists="replace",
    index=False
)

print(f"Data successfully loaded into table '{table_name}' in database '{Database}'.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




