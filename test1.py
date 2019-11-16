
# coding: utf-8

# In[4]:

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j)and(j!=k)and(1!=k):
                print(i,j,k)


# In[6]:

i=int(input("月利润："))
lr=[1000000,600000,400000,200000,100000,0]
tc=[0.01,0.015,0.03,0.05,0.075,0.1]
jj=0
for j in range(0,6):
    if lr[j]<i:
        jj+=(i-lr[j])*tc[j]
        i=lr[j]
print(jj)
        


# In[9]:

for i in range(1,85):
    if i%2==0:
        j=168/i;
        if (j%2==0)and(i>=j)and((i+j)%2==0)and((i-j)%2==0):
            n=(i-j)/2
            print(n*n-100)


# In[6]:

year=int(input("year:"))
month=int(input("month:"))
day=int(input("day:"))
months=[31,28,31,30,31,30,31,31,30,31,30,31]
days=0
tt=0
if ((year%4==0)and(year%100!=0))or(year%400==0) :
    tt=1
if (tt==1)and(month>1):
    days+=1
for i in range(1,13):
    if 13>month>i:
        days+=months[i-1]
    if month>12:
        print("error")
else:
    days+=day
print(days)
    


# In[ ]:




# 
