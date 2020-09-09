#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=int(input("enter the lattitude"))

if num <= 1000:
  print("safe to land")
elif num > 1000 and num < 5000:
  print("bring down to 1000")
else:
  print("turn around")


# In[ ]:




