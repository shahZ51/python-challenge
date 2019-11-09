#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
import pandas as pd


# In[2]:



csvpath = ('Resources/budget_data.csv')
df = pd.read_csv(csvpath)
df.head()
 
          
              
#csv_header = pd.DataFrame(csvreader)
#csv_header.head()


# In[3]:


total_months = df['Date'].count()
total_months
#print(total_months +1) 





# In[4]:


nrows = 0
for row in df['Date']:
    nrows = nrows+1
nrows


# In[5]:


total_value = 0
for index, row in df.iterrows():
    total_value = total_value + row['Profit/Losses']
    
total_value
    


# In[6]:






Monthly_Change = df['Profit/Losses'].diff()

Monthly_Change 

df.insert(2,'Change',Monthly_Change)

df.head()






# In[7]:


df.to_csv('budget_data_output.csv')


# In[8]:


Avg_change = df['Change'].mean()
Avg_change


# In[9]:


Greatest_Increase = df['Change'].max()
Greatest_Increase


# In[10]:


Greatest_decrease = df['Change'].min()
Greatest_decrease


# In[11]:


max_date = df.loc[df['Change' ] == Greatest_Increase ] ['Date'].iloc[0]

max_date


# In[12]:


min_date = df.loc[df['Change' ] == Greatest_decrease ] ['Date'].iloc[0]
min_date


# In[13]:


# Printing terminal
output = (
f"Financial Analysis\n"
f"---------------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${total_value}\n"
f"Average change: ${Avg_change}\n"
f"Greatest Increase in Profits: {max_date} (${Greatest_Increase})\n"
f"Greatest Decrease in Profits: {min_date} (${Greatest_decrease})\n"
f"```\n"
)
print(output)


# In[ ]:




