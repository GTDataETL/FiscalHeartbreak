#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Dependencies
import pandas as pd

def marriage_def():
    # In[5]:


    # Make a reference to the books.csv file path
    csv_path = "ACS_09_5YR_S1201_with_ann.csv"

    # Import the books.csv file as a DataFrame0
    #Marriage09_df = pd.read_csv(csv_path, encoding="utf-8")
    Marriage09_df = pd.read_csv(csv_path, encoding="ISO-8859-1",header=0)
    Marriage09_df = Marriage09_df[["GEO.display-label", 
                "HC01_EST_VC01", "HC02_EST_VC01", "HC03_EST_VC01", "HC04_EST_VC01", "HC05_EST_VC01", "HC06_EST_VC01",
                "HC01_MOE_VC01", "HC02_MOE_VC01", "HC03_MOE_VC01", "HC04_MOE_VC01", "HC05_MOE_VC01", "HC06_MOE_VC01"]]
                                
    M09_renamed_df = Marriage09_df.rename(columns={"GEO.display-label": "County and State",
                                            "HC01_EST_VC01": "Total Population",
                                            "HC02_EST_VC01": "Percent Married",
                                            "HC03_EST_VC01": "Percent Widowed",
                                            "HC04_EST_VC01": "Percent Divorced",
                                            "HC05_EST_VC01": "Percent Separated",
                                            "HC06_EST_VC01": "Never Married", 
                                            "HC01_MOE_VC01": "Total Population Error",
                                            "HC02_MOE_VC01": "Percent Married Error",
                                            "HC03_MOE_VC01": "Percent Widowed Error",
                                            "HC04_MOE_VC01": "Percent Divorced Error",
                                            "HC05_MOE_VC01": "Percent Separated Error",
                                            "HC06_MOE_VC01": "Never Married Error", })
    new = M09_renamed_df["County and State"].str.split(", ", n = 1, expand = True) 
    M09_renamed_df["County"]= new[0]
    M09_renamed_df["State"]= new[1]
    M09_renamed_df.drop(columns =["County and State"], inplace = True) 
    # we drop the extra header here
    M09_renamed_df.drop([0], inplace=True)
    M09_renamed_df['Year'] = 2009
    M09_renamed_df.head()



    # In[6]:


    # Make a reference to the books.csv file path
    csv_path = "ACS_10_5YR_S1201_with_ann.csv"

    # Import the books.csv file as a DataFrame0
    #Marriage09_df = pd.read_csv(csv_path, encoding="utf-8")
    Marriage10_df = pd.read_csv(csv_path, encoding="ISO-8859-1",header=0)
    Marriage10_df = Marriage10_df[["GEO.display-label", 
                "HC01_EST_VC01", "HC02_EST_VC01", "HC03_EST_VC01", "HC04_EST_VC01", "HC05_EST_VC01", "HC06_EST_VC01",
                "HC01_MOE_VC01", "HC02_MOE_VC01", "HC03_MOE_VC01", "HC04_MOE_VC01", "HC05_MOE_VC01", "HC06_MOE_VC01"]]
                                
    M10_renamed_df = Marriage10_df.rename(columns={"GEO.display-label": "County and State",
                                            "HC01_EST_VC01": "Total Population",
                                            "HC02_EST_VC01": "Percent Married",
                                            "HC03_EST_VC01": "Percent Widowed",
                                            "HC04_EST_VC01": "Percent Divorced",
                                            "HC05_EST_VC01": "Percent Separated",
                                            "HC06_EST_VC01": "Never Married", 
                                            "HC01_MOE_VC01": "Total Population Error",
                                            "HC02_MOE_VC01": "Percent Married Error",
                                            "HC03_MOE_VC01": "Percent Widowed Error",
                                            "HC04_MOE_VC01": "Percent Divorced Error",
                                            "HC05_MOE_VC01": "Percent Separated Error",
                                            "HC06_MOE_VC01": "Never Married Error", })

    new = M10_renamed_df["County and State"].str.split(", ", n = 1, expand = True) 
    M10_renamed_df["County"]= new[0]
    M10_renamed_df["State"]= new[1]
    M10_renamed_df.drop(columns =["County and State"], inplace = True) 
    # we drop the extra header here
    M10_renamed_df.drop([0], inplace=True)
    M10_renamed_df['Year'] = 2010
    M10_renamed_df.head()




    # In[7]:


    # Make a reference to the books.csv file path
    csv_path = "ACS_11_5YR_S1201_with_ann.csv"

    # Import the books.csv file as a DataFrame0
    #Marriage09_df = pd.read_csv(csv_path, encoding="utf-8")
    Marriage11_df = pd.read_csv(csv_path, encoding="ISO-8859-1",header=0)
    Marriage11_df = Marriage11_df[["GEO.display-label", 
                "HC01_EST_VC01", "HC02_EST_VC01", "HC03_EST_VC01", "HC04_EST_VC01", "HC05_EST_VC01", "HC06_EST_VC01",
                "HC01_MOE_VC01", "HC02_MOE_VC01", "HC03_MOE_VC01", "HC04_MOE_VC01", "HC05_MOE_VC01", "HC06_MOE_VC01"]]
                                
    M11_renamed_df = Marriage11_df.rename(columns={"GEO.display-label": "County and State",
                                            "HC01_EST_VC01": "Total Population",
                                            "HC02_EST_VC01": "Percent Married",
                                            "HC03_EST_VC01": "Percent Widowed",
                                            "HC04_EST_VC01": "Percent Divorced",
                                            "HC05_EST_VC01": "Percent Separated",
                                            "HC06_EST_VC01": "Never Married", 
                                            "HC01_MOE_VC01": "Total Population Error",
                                            "HC02_MOE_VC01": "Percent Married Error",
                                            "HC03_MOE_VC01": "Percent Widowed Error",
                                            "HC04_MOE_VC01": "Percent Divorced Error",
                                            "HC05_MOE_VC01": "Percent Separated Error",
                                            "HC06_MOE_VC01": "Never Married Error", })

    new = M11_renamed_df["County and State"].str.split(", ", n = 1, expand = True) 
    M11_renamed_df["County"]= new[0]
    M11_renamed_df["State"]= new[1]
    M11_renamed_df.drop(columns =["County and State"], inplace = True) 
    # we drop the extra header here
    M11_renamed_df.drop([0], inplace=True)
    M11_renamed_df['Year'] = 2011
    M11_renamed_df.head()



    # In[8]:


    # Make a reference to the books.csv file path
    csv_path = "ACS_12_5YR_S1201_with_ann.csv"

    # Import the books.csv file as a DataFrame0
    #Marriage09_df = pd.read_csv(csv_path, encoding="utf-8")
    Marriage12_df = pd.read_csv(csv_path, encoding="ISO-8859-1",header=0)
    Marriage12_df = Marriage12_df[["GEO.display-label", 
                "HC01_EST_VC01", "HC02_EST_VC01", "HC03_EST_VC01", "HC04_EST_VC01", "HC05_EST_VC01", "HC06_EST_VC01",
                "HC01_MOE_VC01", "HC02_MOE_VC01", "HC03_MOE_VC01", "HC04_MOE_VC01", "HC05_MOE_VC01", "HC06_MOE_VC01"]]
                                
    M12_renamed_df = Marriage12_df.rename(columns={"GEO.display-label": "County and State",
                                            "HC01_EST_VC01": "Total Population",
                                            "HC02_EST_VC01": "Percent Married",
                                            "HC03_EST_VC01": "Percent Widowed",
                                            "HC04_EST_VC01": "Percent Divorced",
                                            "HC05_EST_VC01": "Percent Separated",
                                            "HC06_EST_VC01": "Never Married", 
                                            "HC01_MOE_VC01": "Total Population Error",
                                            "HC02_MOE_VC01": "Percent Married Error",
                                            "HC03_MOE_VC01": "Percent Widowed Error",
                                            "HC04_MOE_VC01": "Percent Divorced Error",
                                            "HC05_MOE_VC01": "Percent Separated Error",
                                            "HC06_MOE_VC01": "Never Married Error", })

    new = M12_renamed_df["County and State"].str.split(", ", n = 1, expand = True) 
    M12_renamed_df["County"]= new[0]
    M12_renamed_df["State"]= new[1]
    M12_renamed_df.drop(columns =["County and State"], inplace = True) 
    # we drop the extra header here
    M12_renamed_df.drop([0], inplace=True)
    M12_renamed_df['Year'] = 2012
    M12_renamed_df.head()



    # In[9]:


    # Make a reference to the books.csv file path
    csv_path = "ACS_13_5YR_S1201_with_ann.csv"

    # Import the books.csv file as a DataFrame0
    #Marriage09_df = pd.read_csv(csv_path, encoding="utf-8")
    Marriage13_df = pd.read_csv(csv_path, encoding="ISO-8859-1",header=0)
    Marriage13_df = Marriage13_df[["GEO.display-label", 
                "HC01_EST_VC01", "HC02_EST_VC01", "HC03_EST_VC01", "HC04_EST_VC01", "HC05_EST_VC01", "HC06_EST_VC01",
                "HC01_MOE_VC01", "HC02_MOE_VC01", "HC03_MOE_VC01", "HC04_MOE_VC01", "HC05_MOE_VC01", "HC06_MOE_VC01"]]
                                
    M13_renamed_df = Marriage13_df.rename(columns={"GEO.display-label": "County and State",
                                            "HC01_EST_VC01": "Total Population",
                                            "HC02_EST_VC01": "Percent Married",
                                            "HC03_EST_VC01": "Percent Widowed",
                                            "HC04_EST_VC01": "Percent Divorced",
                                            "HC05_EST_VC01": "Percent Separated",
                                            "HC06_EST_VC01": "Never Married", 
                                            "HC01_MOE_VC01": "Total Population Error",
                                            "HC02_MOE_VC01": "Percent Married Error",
                                            "HC03_MOE_VC01": "Percent Widowed Error",
                                            "HC04_MOE_VC01": "Percent Divorced Error",
                                            "HC05_MOE_VC01": "Percent Separated Error",
                                            "HC06_MOE_VC01": "Never Married Error", })

    new = M13_renamed_df["County and State"].str.split(", ", n = 1, expand = True) 
    M13_renamed_df["County"]= new[0]
    M13_renamed_df["State"]= new[1]
    M13_renamed_df.drop(columns =["County and State"], inplace = True) 
    # we drop the extra header here
    M13_renamed_df.drop([0], inplace=True)
    M13_renamed_df['Year'] = 2013
    M13_renamed_df.head()



    # In[10]:


    # Make a reference to the books.csv file path
    csv_path = "ACS_14_5YR_S1201_with_ann.csv"

    # Import the books.csv file as a DataFrame0
    #Marriage09_df = pd.read_csv(csv_path, encoding="utf-8")
    Marriage14_df = pd.read_csv(csv_path, encoding="ISO-8859-1",header=0)
    Marriage14_df = Marriage14_df[["GEO.display-label", 
                "HC01_EST_VC01", "HC02_EST_VC01", "HC03_EST_VC01", "HC04_EST_VC01", "HC05_EST_VC01", "HC06_EST_VC01",
                "HC01_MOE_VC01", "HC02_MOE_VC01", "HC03_MOE_VC01", "HC04_MOE_VC01", "HC05_MOE_VC01", "HC06_MOE_VC01"]]
                                
    M14_renamed_df = Marriage14_df.rename(columns={"GEO.display-label": "County and State",
                                            "HC01_EST_VC01": "Total Population",
                                            "HC02_EST_VC01": "Percent Married",
                                            "HC03_EST_VC01": "Percent Widowed",
                                            "HC04_EST_VC01": "Percent Divorced",
                                            "HC05_EST_VC01": "Percent Separated",
                                            "HC06_EST_VC01": "Never Married", 
                                            "HC01_MOE_VC01": "Total Population Error",
                                            "HC02_MOE_VC01": "Percent Married Error",
                                            "HC03_MOE_VC01": "Percent Widowed Error",
                                            "HC04_MOE_VC01": "Percent Divorced Error",
                                            "HC05_MOE_VC01": "Percent Separated Error",
                                            "HC06_MOE_VC01": "Never Married Error", })

    new = M14_renamed_df["County and State"].str.split(", ", n = 1, expand = True) 
    M14_renamed_df["County"]= new[0]
    M14_renamed_df["State"]= new[1]
    M14_renamed_df.drop(columns =["County and State"], inplace = True) 
    # we drop the extra header here
    M14_renamed_df.drop([0], inplace=True)
    M14_renamed_df['Year'] = 2014
    M14_renamed_df.head()



    # In[11]:


    # Make a reference to the books.csv file path
    csv_path = "ACS_15_5YR_S1201_with_ann.csv"

    # Import the books.csv file as a DataFrame0
    #Marriage09_df = pd.read_csv(csv_path, encoding="utf-8")
    Marriage15_df = pd.read_csv(csv_path, encoding="ISO-8859-1",header=0)
    Marriage15_df = Marriage15_df[["GEO.display-label", 
                "HC01_EST_VC01", "HC02_EST_VC01", "HC03_EST_VC01", "HC04_EST_VC01", "HC05_EST_VC01", "HC06_EST_VC01",
                "HC01_MOE_VC01", "HC02_MOE_VC01", "HC03_MOE_VC01", "HC04_MOE_VC01", "HC05_MOE_VC01", "HC06_MOE_VC01"]]
                                
    M15_renamed_df = Marriage15_df.rename(columns={"GEO.display-label": "County and State",
                                            "HC01_EST_VC01": "Total Population",
                                            "HC02_EST_VC01": "Percent Married",
                                            "HC03_EST_VC01": "Percent Widowed",
                                            "HC04_EST_VC01": "Percent Divorced",
                                            "HC05_EST_VC01": "Percent Separated",
                                            "HC06_EST_VC01": "Never Married", 
                                            "HC01_MOE_VC01": "Total Population Error",
                                            "HC02_MOE_VC01": "Percent Married Error",
                                            "HC03_MOE_VC01": "Percent Widowed Error",
                                            "HC04_MOE_VC01": "Percent Divorced Error",
                                            "HC05_MOE_VC01": "Percent Separated Error",
                                            "HC06_MOE_VC01": "Never Married Error", })

    new = M15_renamed_df["County and State"].str.split(", ", n = 1, expand = True) 
    M15_renamed_df["County"]= new[0]
    M15_renamed_df["State"]= new[1]
    M15_renamed_df.drop(columns =["County and State"], inplace = True) 
    # we drop the extra header here
    M15_renamed_df.drop([0], inplace=True)
    M15_renamed_df['Year'] = 2015
    M15_renamed_df.head()



    # In[12]:


    # Make a reference to the books.csv file path
    csv_path = "ACS_16_5YR_S1201_with_ann.csv"

    # Import the books.csv file as a DataFrame0
    #Marriage09_df = pd.read_csv(csv_path, encoding="utf-8")
    Marriage16_df = pd.read_csv(csv_path, encoding="ISO-8859-1",header=0)
    Marriage16_df = Marriage16_df[["GEO.display-label", 
                "HC01_EST_VC01", "HC02_EST_VC01", "HC03_EST_VC01", "HC04_EST_VC01", "HC05_EST_VC01", "HC06_EST_VC01",
                "HC01_MOE_VC01", "HC02_MOE_VC01", "HC03_MOE_VC01", "HC04_MOE_VC01", "HC05_MOE_VC01", "HC06_MOE_VC01"]]
                                
    M16_renamed_df = Marriage16_df.rename(columns={"GEO.display-label": "County and State",
                                            "HC01_EST_VC01": "Total Population",
                                            "HC02_EST_VC01": "Percent Married",
                                            "HC03_EST_VC01": "Percent Widowed",
                                            "HC04_EST_VC01": "Percent Divorced",
                                            "HC05_EST_VC01": "Percent Separated",
                                            "HC06_EST_VC01": "Never Married", 
                                            "HC01_MOE_VC01": "Total Population Error",
                                            "HC02_MOE_VC01": "Percent Married Error",
                                            "HC03_MOE_VC01": "Percent Widowed Error",
                                            "HC04_MOE_VC01": "Percent Divorced Error",
                                            "HC05_MOE_VC01": "Percent Separated Error",
                                            "HC06_MOE_VC01": "Never Married Error", })

    new = M16_renamed_df["County and State"].str.split(", ", n = 1, expand = True) 
    M16_renamed_df["County"]= new[0]
    M16_renamed_df["State"]= new[1]
    M16_renamed_df.drop(columns =["County and State"], inplace = True) 
    # we drop the extra header here
    M16_renamed_df.drop([0], inplace=True)
    M16_renamed_df['Year'] = 2016
    M16_renamed_df.head()



    # In[13]:


    # Make a reference to the books.csv file path
    csv_path = "ACS_17_5YR_S1201_with_ann.csv"

    # Import the books.csv file as a DataFrame0
    #Marriage09_df = pd.read_csv(csv_path, encoding="utf-8")
    Marriage17_df = pd.read_csv(csv_path, encoding="ISO-8859-1",header=0)
    Marriage17_df = Marriage17_df[["GEO.display-label", 
                "HC01_EST_VC01", "HC02_EST_VC01", "HC03_EST_VC01", "HC04_EST_VC01", "HC05_EST_VC01", "HC06_EST_VC01",
                "HC01_MOE_VC01", "HC02_MOE_VC01", "HC03_MOE_VC01", "HC04_MOE_VC01", "HC05_MOE_VC01", "HC06_MOE_VC01"]]
                                
    M17_renamed_df = Marriage17_df.rename(columns={"GEO.display-label": "County and State",
                                            "HC01_EST_VC01": "Total Population",
                                            "HC02_EST_VC01": "Percent Married",
                                            "HC03_EST_VC01": "Percent Widowed",
                                            "HC04_EST_VC01": "Percent Divorced",
                                            "HC05_EST_VC01": "Percent Separated",
                                            "HC06_EST_VC01": "Never Married", 
                                            "HC01_MOE_VC01": "Total Population Error",
                                            "HC02_MOE_VC01": "Percent Married Error",
                                            "HC03_MOE_VC01": "Percent Widowed Error",
                                            "HC04_MOE_VC01": "Percent Divorced Error",
                                            "HC05_MOE_VC01": "Percent Separated Error",
                                            "HC06_MOE_VC01": "Never Married Error", })

    new = M17_renamed_df["County and State"].str.split(", ", n = 1, expand = True) 
    M17_renamed_df["County"]= new[0]
    M17_renamed_df["State"]= new[1]
    M17_renamed_df.drop(columns =["County and State"], inplace = True) 
    # we drop the extra header here
    M17_renamed_df.drop([0], inplace=True)
    M17_renamed_df['Year'] = 2017
    M17_renamed_df.head()



    # In[14]:


    M16_renamed_df.tail()


    # In[21]:


    Marriage_all_df = pd.concat([M09_renamed_df, M10_renamed_df,M11_renamed_df,M12_renamed_df,M13_renamed_df,M14_renamed_df,M15_renamed_df,M16_renamed_df, M17_renamed_df])
    Marriage_all_df


    # In[26]:


    Marriage_df = Marriage_all_df.reset_index(drop=True)


    # In[28]:


    Marriage_df.head()
    return Marriage_df


# In[ ]:




