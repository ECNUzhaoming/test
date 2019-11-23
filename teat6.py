
# coding: utf-8

# In[3]:


a = int(input("请输入一个数字:\n"))
x = str(a)
flag = True

for i in range(int(len(x)/2)):
   if x[i] != x[-i - 1]:
       flag = False
       break
if flag:
   print ("%d 是一个回文数!" % a)
else:
   print ("%d 不是一个回文数!" % a)


# In[9]:

letter = input("please input:")
#while letter  != 'Y':
if letter == 'S':
    print ('please input second letter:')
    letter = input("please input:")
    if letter == 'a':
        print ('Saturday')
    elif letter  == 'u':
        print ('Sunday')
    else:
        print ('data error')
    
elif letter == 'F':
    print ('Friday')
    
elif letter == 'M':
    print ('Monday')
    
elif letter == 'T':
    print ('please input second letter')
    letter = input("please input:")
 
    if letter  == 'u':
        print ('Tuesday')
    elif letter  == 'h':
        print ('Thursday')
    else:
        print ('data error')
        
elif letter == 'W':
    print ('Wednesday')
else:
    print ('data error')


# In[10]:

a = ['one', 'two', 'three']
for i in a[::-1]:
    print (i)


# In[12]:

L = [1,2,3,4,5]
s1 = ','.join(str(n) for n in L)
print (s1)


# In[14]:

def hello_world():
    print ('hello world')
 
def three_hellos():
    for i in range(3):
        hello_world()
if __name__ == '__main__':
    three_hellos()


# In[16]:

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print (bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)


# In[17]:

lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))
 
for num in range(lower,upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)


# In[19]:

if __name__ == "__main__":
    N = 10
    # input data
    print ('请输入10个数字:\n')
    l = []
    for i in range(N):
        l.append(int(input('输入一个数字:\n')))
    print
    for i in range(N):
        print (l[i])
    print
 
    # 排列10个数字
    for i in range(N - 1):
        min = i
        for j in range(i + 1,N):
            if l[min] > l[j]:min = j
        l[i],l[min] = l[min],l[i]
    print ('排列之后：')
    for i in range(N):
        print (l[i])


# if __name__ == '__main__':
#     # 方法一 ： 0 作为加入数字的占位符
#     a = [1,4,6,9,13,16,19,28,40,100,0]
#     print '原始列表:'
#     for i in range(len(a)):
#         print (a[i])
#     number = int(raw_input("\n插入一个数字:\n"))
#     end = a[9]
#     if number > end:
#         a[10] = number
#     else:
#         for i in range(10):
#             if a[i] > number:
#                 temp1 = a[i]
#                 a[i] = number
#                 for j in range(i + 1,11):
#                     temp2 = a[j]
#                     a[j] = temp1
#                     temp1 = temp2
#                 break
#     print '排序后列表:'
#     for i in range(11):
#         print (a[i])

# In[ ]:



