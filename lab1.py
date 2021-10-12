#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=10


# In[2]:


a


# In[3]:


print(a)


# In[4]:


a="hello"


# In[5]:


a


# In[6]:


arr=[1,2,3,4,5]


# In[7]:


arr


# In[8]:


arr[0]


# In[9]:


arr[2]


# In[10]:


arr[1]=20


# In[11]:


arr


# In[ ]:





# In[12]:


arr[4]="string"


# In[13]:


arr


# In[14]:


arr[3]=2.44


# In[15]:


arr


# In[16]:


arr.min


# In[17]:


arr.min()


# In[18]:


min(arr)


# In[19]:


arr.pop()


# In[20]:


aee


# In[21]:


arr


# In[22]:


arr.pop(2)


# In[23]:


arr


# In[24]:


arr1=[6,7,8,9,10]


# In[25]:


arr+arr1


# In[26]:


for i in arr:
    print(arr[i])


# In[27]:


arr2=arr+arr1


# In[29]:


for i in arr2:
    print(i)


# In[53]:


n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
op=input("enter the operator:")
if(op=='+'):
    print(n1+n2)
elif (op=='-'):
    print(n1-n2)
elif (op=='*'):
    print(n1*n2)
else:
    print(n1/n2)


# In[44]:


dict={"first":"nmit","second":"ise"}


# In[46]:


dict["first"]


# In[48]:


dict["second"]


# In[49]:


dict["first"]="cse"


# In[50]:


dict["first"]


# In[54]:


a=[[1,2,3,4],5,6,{"1":"a","2":"b"}]


# In[55]:


a


# In[56]:


a.pop(2)


# In[57]:


a.pop()


# In[58]:


a


# In[60]:


a.pop(0)


# In[61]:


a.pop()


# In[62]:


a


# In[100]:


import statistics
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
length=len(l)
mean=0
min=l[0]
max=l[0]
for i in l:
    mean=mean+i
    if(i<min):
        min=i
    if(i>max):
        max=i
print(mean/len(l))
print(min)
print(max)
#print(statistics.mode(l))
m=int(length/2)
if(length%2==0):
    n=(l[m]+l[m-1])/2
    print(n)
else:
    print(l[m])
    



# In[ ]:





# In[ ]:




