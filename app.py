#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


import pandas as pd


# In[14]:


df = pd.read_excel("C:\\Users\\nikhi\\Downloads\\WBJEE2.xlsx")


# In[ ]:





# In[15]:


# df.drop('Unnamed: 0', axis = 1, inplace = True)
df


# In[6]:


import streamlit as st
import pandas as pd

# Recommendation function
def recommend_colleges(rank, quota):
    # Filter the dataframe based on rank and quota
    recommendations = df[
        (df["Opening Rank"] <= rank) &
        (df["Closing Rank"] >= rank) &
        (df["Quota"].str.lower() == quota.lower())
    ]
    
    # Check if there are any matches
    if not recommendations.empty:
        return recommendations[["Institute", "Program", "Stream", "Category", "Opening Rank", "Closing Rank"]]
    else:
        return "No matching colleges found for your rank and quota."

# Streamlit UI
st.title("College Recommendation System")

# Input for rank and quota
rank = st.number_input("Enter Your Rank:", min_value=1, max_value=100000, value=10000)
quota = st.selectbox("Select Your Quota:", ["Home State", "Other State", "All India"])

# When the user clicks the button, get the recommendations
if st.button("Get Recommendations"):
    result = recommend_colleges(rank, quota)
    
    if isinstance(result, pd.DataFrame):
        st.dataframe(result)  # Display the recommendation in a table format
    else:
        st.write(result)  # If no results, display the message


# In[12]:





# In[ ]:




