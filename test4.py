
# coding: utf-8

# In[1]:

import datetime
 
if __name__ == '__main__':
 
    # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print(datetime.date.today().strftime('%d/%m/%Y'))
 
    # 创建日期对象
    miyazakiBirthDate = datetime.date(1941, 1, 5)
 
    print(miyazakiBirthDate.strftime('%d/%m/%Y'))
 
    # 日期算术运算
    miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)
 
    print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))
 
    # 日期替换
    miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)
 
    print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))
    


# In[5]:

import string
s = input('请输入一个字符串:\n')
letters = 0
space = 0
digit = 0
others = 0
i=0
while i < len(s):
    c = s[i]
    i += 1
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print ('char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others))


# In[13]:

from functools import reduce
Tn = 0
Sn = []
n = int(input('n = '))
a = int(input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print (Tn)

Sn = reduce(lambda x,y : x + y,Sn)
print ("计算和为：",Sn)


# In[19]:

from sys import stdout
for j in range(2,1001):
    k = []
    n = -1
    s = j
    for i in range(1,j):
            if j % i == 0:
                n += 1
                s -= i
                k.append(i)
    
    if s == 0:
        print(j) 
        for i in range(n):
            print(str(k[i]),end=" ")
        print(k[n]) 


# In[20]:

tour = []
height = []
 
hei = 100.0 # 起始高度
tim = 10 # 次数
 
for i in range(1, tim + 1):
    # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
    if i == 1:
        tour.append(hei)
    else:
        tour.append(2*hei) 
    hei /= 2
    height.append(hei)
 
print('总高度：tour = {0}'.format(sum(tour)))
print('第10次反弹高度：height = {0}'.format(height[-1]))


# In[ ]:



