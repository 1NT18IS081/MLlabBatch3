
import math
import statistics as st
import sklearn.preprocessing
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
print("mean:",mean/len(l))
print("min:",min)
print("max:",max)
#print(statistics.mode(l))
m=int(length/2)
if(length%2==0):
    n=(l[m]+l[m-1])/2
    print(n)
else:
    print(l[m])
meann=sum(l)/len(l)
var =sum(pow(j-meann,2) for j in l)/(len(l)-1)
std=math.sqrt(var)
print("standard deviation:",std)
print(st.stdev(l))
print(st.variance(l))



# In[16]:


arr=[4,6,3,2,1,10,7,9,8]
n=len(arr)
for i in range(n-1):
    for j in range(0,n-i-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
for i in range(n): 
    print(arr[i])


# In[38]:


import math
arr=[4,6,3,2,1,10,7,9,8]
type(arr)


# In[39]:


for i in arr:
    print(i)


# In[43]:


minv = 0
maxv = 1
for k in arr:
    x =((k-minv)/(maxv-minv))
    print(x)


# In[ ]:




