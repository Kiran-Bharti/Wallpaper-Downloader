
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.co.in/imghp?hl=en&tab=wi")
elem = driver.find_element_by_name("q")
elem.clear()
x=input("enter the name of the wallpaper you want to download : ")
x=x+" wallpaper hd "
elem.send_keys(x)
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source



# In[ ]:


from bs4 import BeautifulSoup as bs


# In[19]:


import requests


# In[20]:


url=driver.current_url


# In[21]:


webdata=requests.get(url)


# In[22]:


if webdata.status_code==200:
    print("fetching done")
else:
    print("not done")


# In[23]:


data=webdata.text
soup=bs(data,'lxml')


# In[24]:


anchors=soup.find_all('a')


# In[25]:


div_article=soup.find_all('img')


# In[26]:


flink=div_article[1].attrs.get('src')


# In[27]:


import random
import urllib.request


# In[28]:


address = input('Address to save image (eg: d:/): ')
name = random.randrange(1,1000)
full_name = str(address)
full_name += str(name) + '.jpg'

urllib.request.urlretrieve(flink,full_name)
print('Your image is being downloaded and saved to ' + full_name)


# In[29]:


driver.close()

