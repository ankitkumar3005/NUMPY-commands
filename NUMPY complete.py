#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


myarr = np.array([1,3,4,5,6])


# In[3]:


myarr


# In[4]:


myarr[0]


# In[5]:


myarr.shape


# In[6]:


myarr.dtype


# **Array creation :Conversion from other Python structures**

# In[7]:


listarray = np.array([[1,2,3],[3,5,6],[7,8,9]])


# In[8]:


listarray


# In[9]:


listarray.dtype


# In[10]:


listarray.shape


# In[11]:


listarray.size


# **Intrinsic array creation arrays:**

# In[12]:


zeros = np.zeros((2,3))


# In[13]:


zeros.dtype


# In[14]:


zeros


# In[15]:


zeros.shape


# In[16]:


rng = np.array(15)


# In[17]:


rng


# In[18]:


lspace = np.linspace(1,4,3)


# In[19]:


lspace


# In[20]:


emp =np.array((4,6))


# In[21]:


emp


# In[22]:


ide = np.identity(45)


# In[23]:


ide


# In[24]:


ide.shape


# In[25]:


arr = np.arange(99)


# In[26]:


arr


# In[27]:


arr.reshape(3,33)


# In[28]:


arr


# In[29]:


arr.shape


# In[30]:


x = [[3,5,7],[1,2,3],[5,6,8]]


# In[31]:


ar = np.array(x)


# In[32]:


ar.sum(axis=0)


# In[33]:


ar.sum(axis =1)


# In[34]:


ar.T


# In[35]:


ar.flat


# In[37]:


for item in ar.flat:
     print(item)


# In[38]:


ar.ndim


# In[39]:


ar.size


# In[40]:


ar.nbytes


# In[41]:


one = np.array([2,5,6,7,1])


# In[42]:


one.argmax()


# In[43]:


one.argmin()


# In[44]:


one.argsort()


# In[45]:


ar


# In[46]:


ar.argmin()


# In[49]:


ar.argsort(axis =0)


# In[50]:


ar.ravel()


# In[51]:


ar


# In[53]:


ar2 = np.array([[1,2,3],[3,4,5],[3,6,1]])


# In[54]:


ar +ar2


# In[55]:


ar*ar2


# In[57]:


ar-ar2


# In[58]:


ar%ar2


# In[59]:


np.sqrt(ar)


# In[60]:


ar.sum()


# In[61]:


ar.min()


# In[62]:


ar


# In[64]:


np.where(ar>5)


# In[65]:


type(np.where(ar<4))


# In[66]:


np.count_nonzero(ar)


# In[67]:


np.nonzero(ar)


# In[68]:


ar[1,2] = 0


# In[70]:


np.nonzero(ar)


# In[71]:


import sys


# In[72]:


ch_ar = [0,4,55,2]


# In[73]:


np_ar = np.array(ch_ar)


# In[74]:


sys.getsizeof(1)*len(ch_ar)


# In[75]:


np_ar.itemsize*np_ar.size


# In[76]:


np_ar.tolist()

