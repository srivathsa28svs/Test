#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
print("Problem1")
list=[0,1,2,3,4,5,6,7,8,9]
array=np.array(list)
print(array)
array[array%2!=0]=-1
print(array)


# In[5]:


print("Problem2")
array=np.arange(10)
print(array)
arr=np.arange(10).reshape(2,5)
print(arr)


# In[6]:


print("Problem3")
arr=np.array([1,2,3])
print(arr)
so=np.concatenate((np.repeat(arr,3),np.tile(arr,3)))
print(so)


# In[7]:


print("Problem4")
a=np.array([1,2,3,2,3,4,3,4,5,6])
b=np.array([7,2,10,2,7,4,9,4,9,8])
c=np.intersect1d(a,b)
print(c)


# In[8]:


a=np.array([1,2,3,2,3,4,3,4,5,6])
b=np.array([7,2,10,2,7,4,9,4,9,8])
d=np.where(a==b)
print(d)


# In[9]:


print("Problem6")
print(np.random.random_sample((5,3))+5)


# In[13]:


print("Problem7")
arr=np.arange(15)
np.set_printoptions(threshold=5)
print(arr)


# In[11]:


print("Problem8")
np.random.seed(100)
rand_arr=np.random.random([3,3])/1e3
np.set_printoptions(suppress=True,precision=6)
print(rand_arr)


# In[14]:


print("Problem9")
arr=np.arange(9).reshape(3,3)
print(arr)
arr[:,[0,1]]=arr[:,[1,0]]
print(arr)


# In[15]:


print("Problem10")
arr=np.arange(9).reshape(3,3)
print(arr)
arr[[0,1],:]=arr[[1,0],:]
print(arr)


# In[ ]:





# In[ ]:




