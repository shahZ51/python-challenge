#!/usr/bin/env python
# coding: utf-8

# In[13]:


import os
import csv
import pandas as pd


# In[14]:


csvpath = ("Resources/election_data.csv")
df = pd.read_csv(csvpath)
df.head()


# In[15]:


total_votes = df['Voter ID'].count()
total_votes


# df.groupby('Candidate').sum()

# In[16]:


candidate_vote =df.groupby('Candidate').count()


candidate_vote = candidate_vote.reset_index(drop = False)
candidate_vote = candidate_vote.rename(columns={"Voter ID": "Number of Votes"})
candidate_vote = candidate_vote.drop(columns =['County'])

candidate_vote


# In[17]:


max_vote = candidate_vote['Number of Votes'].max()
max_vote


# In[18]:


unique_candidate =df.Candidate.unique()
unique_candidate


# In[19]:


df.head()


# In[20]:


vote_received = df.Candidate.value_counts()
vote_received


# In[21]:


percent_count = (vote_received / total_votes)*100

percent_count


# In[22]:


winner = candidate_vote.loc[candidate_vote['Number of Votes' ] == max_vote ] ['Candidate'].iloc[0]

winner


# In[25]:


# Printing terminal
output = (
f"Election Results\n"
f"---------------------------------\n"
f"Total Votes: {total_votes}\n"
f"---------------------------------\n"   
f"{percent_count}% {vote_received} \n"
f"---------------------------------\n" 
f" Winner: {winner}\n"
f"---------------------------------\n" 
f"```\n"
)
print(output)

