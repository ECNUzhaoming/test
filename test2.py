
# coding: utf-8

# In[3]:

i=[]
for k in range(0,3):
    j=int(input("please input three int number:"))
    i.append(j)
i.sort()
print(i)


# In[6]:

def fib(n):
    if n>2:
        return fib(n-2)+fib(n-1)
    elif n==2:
        return 1
    else:
        return 1
print(fib(10))


# In[7]:

a=[1,2,3]
b=a[:]
print(b)


# In[13]:

for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(i,j,i*j),end=" ")
    print("")
    


# In[17]:

import time
myD={1:'a',2:'b'}
for key,value in dict.items(myD):
    print(key,value)
    time.sleep(1)


# In[22]:

import time
print(time.strftime("%y-%m-%d %H:%M:%S",time.localtime(time.time())))
time.sleep(1)
print(time.strftime("%y-%m-%d %H:%M:%S",time.localtime(time.time())))


# In[ ]:



