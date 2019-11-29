#!/usr/bin/env python
# coding: utf-8

# In[49]:


r=input("sayı1:")
r=int(r)
b=input("sayı2:")
b=int(b)
if r<b:
    for x in range(r,b):
        print(x)
elif r>b:
    for x in range(r,b,-1):
        print(x)
else:
    print("sayılar eşit")
    


# In[93]:


list(range(1,20))


# In[96]:


for x in enumerate(list(range(10,20))):

    print(x)


# In[ ]:


##random 


# In[97]:


from random import randint


# In[98]:


randint(5,15)


# In[99]:


randint(5,15)


# In[100]:


new_list=[]
my_string="metalica"


# In[101]:


new_list=[element for element in my_string]


# In[102]:


new_list


# In[ ]:




