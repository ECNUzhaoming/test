
# coding: utf-8

# In[2]:

x2 = 1
for day in range(9,0,-1):
    x1 = (x2 + 1) * 2
    x2 = x1
print (x1)


# In[4]:

for i in range(ord('x'),ord('z') + 1):
    for j in range(ord('x'),ord('z') + 1):
        if i != j:
            for k in range(ord('x'),ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print ('order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k)))


# In[28]:

from sys import stdout
for i in range(4):
    for j in range(3-i):
        print(' ',end="")
   
    for k in range(2 * i + 1):
        print('*',end="")
    print(" ")
for i in range(3):
    for j in range(i + 1):
        print(' ',end="")
    
    for k in range(4 - 2 * i + 1):
        print('*',end="")
    print(" ")


# In[29]:

a = 2.0
b = 1.0
s = 0
for n in range(1,21):
    s += a / b
    t = a
    a = a + b
    b = t
print (s)


# In[30]:

n = 0
s = 0
t = 1
for n in range(1,21):
    t *= n
    s += t
print ('1! + 2! + 3! + ... + 20! = %d' % s)


# In[32]:

def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * fact(j - 1)
    return sum
 
print (fact(5))


# In[33]:

def age(n):
    if n == 1: c = 10
    else: c = age(n - 1) + 2
    return c
print (age(5))


# In[40]:

x = int(input("请输入一个数:\n"))
a = int(x / 10000)
b =int(x % 10000 / 1000)
c = int(x % 1000 / 100)
d = int(x % 100 / 10)
e =int(x % 10)
 
if a != 0:
    print ("5 位数：",e,d,c,b,a)
elif b != 0:
    print ("4 位数：",e,d,c,b,)
elif c != 0:
    print ("3 位数：",e,d,c)
elif d != 0:
    print ("2 位数：",e,d)
else:
    print ("1 位数：",e)


# In[ ]:



