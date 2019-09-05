#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


debt_file = "household-debt-by-county.csv"
debt_df = pd.read_csv(debt_file)
debt_df.head()


# In[3]:


debt_cols = ["year", "qtr", "area_fips", "low", "high"]
debt_transformed = debt_df[debt_cols].copy()


# In[4]:


debt_transformed = debt_transformed.rename(columns={"low": "DtoI_low", "high": "DtoI_high"})
debt_transformed["area_fips"]=debt_transformed["area_fips"].astype(str)


# In[5]:


county_file = "area_titles.csv"
county_df = pd.read_csv(county_file)
county_df.head()


# In[6]:


county_cols = ["area_fips", "area_title"]
county_transformed = county_df[county_cols].copy()


# In[7]:


county_transformed = county_transformed.rename(columns={"area_title": "county_name"})


# In[8]:


merged_df = pd.merge(debt_transformed, county_transformed, on='area_fips', how='left')
merged_df.head(100)


# In[9]:


cropped_df = merged_df.loc[(merged_df["year"]>=2009)]
cropped_df.head(25)


# In[10]:


cleaned_df = cropped_df.dropna(how="any")
cleaned_df.head(25)


# In[11]:


split_df = cleaned_df["county_name"].str.split(pat=", ", n=1, expand=True)
split_df.head()


# In[12]:


cleaned_cols = ["year", "qtr", "area_fips", "DtoI_low", "DtoI_high"]
cleaned_transformed = cleaned_df[cleaned_cols].copy()

cleaned_merged = pd.merge(cleaned_transformed, split_df, left_index=True, right_index=True, how='left')
cleaned_merged.head()


# In[13]:


final_df = cleaned_merged.rename(columns={0: "county_name", 1: "state"})
final_df.head()


# In[18]:


firstqtr_df = final_df.loc[(final_df["qtr"]==1)]
firstqtr_df.head()


# In[19]:


newfinal_df = firstqtr_df.drop(columns=['qtr'])
newfinal_df.head()


# In[ ]:




