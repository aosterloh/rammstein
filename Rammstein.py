#!/usr/bin/env python
# coding: utf-8

# In[129]:


from bs4 import BeautifulSoup
import requests


# In[167]:


# Here, we're just importing both Beautiful Soup and the Requests library
url = 'https://www.fansale.de/fansale/tickets/hard-heavy/ozzy-osbourne/478'
# this is the url that we've already determined is safe and legal to scrape from.
response = requests.get(url)
# here, we fetch the content from the url, using the requests library
soup = BeautifulSoup(response.content.decode('utf-8', 'ignore'), 'html.parser', )
cities = ['BERLIN', 'HAMBURG', 'FRANKFURT']


# In[174]:


data = soup.find_all("li", {'class':'Dropdown-ValuesEntry'})
for x in data: 
    y = x.string.strip().encode('utf-8')
    if y in cities:
        print ("Found new city "+ y) 


# In[ ]:




