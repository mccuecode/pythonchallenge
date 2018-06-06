
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from collections import Counter


# In[121]:


df = pd.read_csv('election_data_1.csv')
df2 = pd.read_csv('election_data_2.csv')


# In[4]:


df.head()


# In[5]:


df.shape


# In[61]:


total_votes = df['Voter ID'].count()


# In[8]:


df['County'].value_counts()


# In[10]:


df['Candidate'].value_counts()


# In[103]:


percentage = df['Candidate'].value_counts() / df['Voter ID'].count()


# In[12]:


print(percentage)


# In[14]:


print(percentage)


# In[24]:


winner = df['Candidate'].value_counts().nlargest(1)


# In[26]:


print (winner[0])


# In[33]:


print (winner)


# In[35]:


len(winner)


# In[37]:


winner


# In[38]:


winner.shape


# In[87]:


winner2 = df['Candidate'].value_counts()


# In[89]:


print (winner2["Vestal"])


# In[41]:


winner_name = df['Candidate'].value_counts().keys().tolist()


# In[43]:


print (winner_name)


# In[44]:


print (winner_name[0])


# In[46]:


df.head ()


# In[49]:


df['Votes'] = df['Candidate'].value_counts() / df['Voter ID'].count()


# In[53]:


#


# In[54]:


len(percentage)


# In[58]:


print (percentage)


# In[90]:


percentage.index


# In[91]:


winner2.index


# In[120]:


#percentage["total_count"] = percentage.index.apply(lambda x: winners2[x]  )


# In[116]:


pd.DataFrame(percentage).reset_index()


# In[117]:



df = pd.DataFrame(np.array([percentage.index.values, percentage.values, np.array([winner2[name] for name in percentage.index])]).T, columns=['Candidate','Percentage','Votes'])
df


# In[119]:


print ('Election Results')
print ("----------------")
print ('Total Votes'), print (total_votes)
print ('----------------')
print (df)
print ('----------------')
print ("Winner")
print (winner_name[0])


# In[84]:





# In[86]:


print(winner_name)

