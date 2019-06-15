
# coding: utf-8

# In[29]:


from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd


# In[30]:


analyzer=SentimentIntensityAnalyzer()


# In[33]:


ncount=0
pcount=0
ncorrect=0
pcorrect=0
with open('WhatsApp Chat with A.txt','r',encoding='cp850') as f:
    for line in f.read().split('\n'):
        a=TextBlob(line)
        if a.sentiment.polarity <=0:
            ncount+=1
            ncorrect+=1
        else:
            pcount+=1
            pcorrect+=1
        


# In[37]:


print('positive accuracy = {}% via {} samples'.format(pcorrect/pcount*100.0,pcount))
print('negative accuracy = {}% via {} samples'.format(ncorrect/ncount*100.0,ncount))


# In[36]:


ncount=0
pcount=0
ncorrect=0
pcorrect=0
with open('WhatsApp Chat with Mamta.txt','r',encoding='cp850') as f:
    for line in f.read().split('\n'):
        a=analyzer.polarity_scores(line)
        if a['compound'] > 0:
            ncount+=1
            ncorrect+=1
        else:
            pcount+=1
            pcorrect+=1
        

