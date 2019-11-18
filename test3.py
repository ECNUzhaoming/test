
# coding: utf-8

# In[11]:

def rabit(n):
    if n>2:
        return rabit(n-1)+rabit(n-2)
    else:
        return 1
for j in range(1,23):
    print(rabit(j),end=",")
    


# In[19]:

import math
count=0
for i in range(101,201):
    j=int(math.sqrt(i+1))
    m=0
    for k in range(2,j+1):
        if i%k==0:
            break
        else:
            m+=1
    if m==(j-1):
        print(i)
        count+=1
print("totoal is {}".format(count))


# In[35]:

for i in range(100,1000):
    a=int(i/100)
    b=int(i/10%10)
    c=i%10
    if a**3+b**3+c**3==i:
        print(i)
 


# In[47]:


def reduceNum(n):
    print ('{} = '.format(n),end="")
    if not isinstance(n, int) or n <= 0 :
        print ('请输入一个正确的数字 !')
        exit(0)
    elif n in [1] :
        print ('{}'.format(n))
    while n not in [1] : # 循环保证递归
        for index in range(2, n + 1) :
            if n % index == 0:
                n = int(n/index) # n 等于 n/index
                if n == 1: 
                    print (index )
                else : # index 一定是素数
                    print ('{} *'.format(index),end="")
                break
reduceNum(90)
reduceNum(100)


# In[50]:


score = int(input('输入分数:\n'))
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'

print ('%d 属于 %s' % (score,grade))


# In[ ]:



