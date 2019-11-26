
# coding: utf-8

# In[2]:

if __name__ == '__main__':
    a = int(input('input a number:\n'))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    print ('%o\t%o' %(a,d))


# In[3]:

if __name__ == '__main__':
    a = 234
    b = ~a
    print ('The a\'s 1 complement is %d' % b)
    a = ~a
    print ('The a\'s 2 complement is %d' % a)


# In[1]:

from tkinter import *
if __name__ == '__main__':
     
 
    canvas = Canvas(width=800, height=600, bg='yellow')  
    canvas.pack(expand=YES, fill=BOTH)                
    k = 1
    j = 1
    for i in range(0,26):
        canvas.create_oval(310 - k,250 - k,310 + k,250 + k, width=1)
        k += j
        j += 0.3
 
    mainloop()


# In[3]:

if __name__ == '__main__':
    a = []
    for i in range(10):
        a.append([])
        for j in range(10):
            a[i].append(0)
    for i in range(10):
        a[i][0] = 1
        a[i][i] = 1
    for i in range(2,10):
        for j in range(1,i):
            a[i][j] = a[i - 1][j-1] + a[i - 1][j]
    from sys import stdout
    for i in range(10):
        for j in range(i + 1):
            stdout.write(str(a[i][j]))
            stdout.write(' ')
        print()


# In[6]:

from tkinter import *
if __name__ == '__main__':
 
    x = 360
    y = 160
    top = y - 30
    bottom = y - 30
    
    canvas = Canvas(width = 400,height = 600,bg = 'white')
    for i in range(20):
        canvas.create_oval(250 - top,250 - bottom,250 + top,250 + bottom)
        top -= 5
        bottom += 5
    canvas.pack()
    mainloop()


# In[8]:

from tkinter import *
if __name__ == '__main__':

    canvas = Canvas(width = 400,height = 600,bg = 'white')
    left = 20
    right = 50
    top = 50
    num = 15
    for i in range(num):
        canvas.create_oval(250 - right,250 - left,250 + right,250 + left)
        canvas.create_oval(250 - 20,250 - top,250 + 20,250 + top)
        canvas.create_rectangle(20 - 2 * i,20 - 2 * i,10 * (i + 2),10 * ( i + 2))
        right += 5
        left += 5
        top += 10

    canvas.pack()
    mainloop()


# In[10]:

if __name__ == '__main__':
    n1 = int(input('n1 = :\n'))
    n2 = int(input('n2 = :\n'))
    n3 = int(input('n3 = :\n'))
 
    def swap(p1,p2):
        return p2,p1
 
    if n1 > n2 : n1,n2 = swap(n1,n2)
    if n1 > n3 : n1,n3 = swap(n1,n3)
    if n2 > n3 : n2,n3 = swap(n2,n3)
 
    print (n1,n2,n3)


# In[12]:

def inp(numbers):
    for i in range(6):
        numbers.append(int(input('输入一个数字:\n')))
p = 0
 
def arr_max(array):
    max = 0
    for i in range(1,len(array) - 1):
        p = i
        if array[p] > array[max] : max = p
    k = max
    array[0],array[k] = array[k],array[0]
def arr_min(array):
    min = 0
    for i in range(1,len(array) - 1):
        p = i
        if array[p] < array[min] : min = p
    l = min
    array[5],array[l] = array[l],array[5]
 
def outp(numbers):
    for i  in range(len(numbers)):
        print (numbers[i])
 
if __name__ == '__main__':
    array = []
    inp(array)        # 输入 6 个数字并放入数组
    arr_max(array)    # 获取最大元素并与第一个元素交换
    arr_min(array)    # 获取最小元素并与最后一个元素交换
    print ('计算结果：')
    outp(array)


# In[15]:

if __name__ == '__main__':
    n = int(input('整数 n 为:\n'))
    m = int(input('向后移 m 个位置为:\n'))
 
    def move(array,n,m):
        array_end = array[n - 1]
        for i in range(n - 1,-1,- 1):
            array[i] = array[i - 1]
        array[0] = array_end
        m -= 1
        if m > 0:move(array,n,m)
        
    number = []
    for i in range(n):
        number.append(int(input('输入一个数字:\n')))
    print ('原始列表:',number)
 
    move(number,n,m)
 
    print ('移动之后:',number)


# In[16]:

if __name__ == '__main__':
    nmax = 50
    n = int(input('请输入总人数:'))
    num = []
    for i in range(n):
        num.append(i + 1)
 
    i = 0
    k = 0
    m = 0
 
    while m < n - 1:
        if num[i] != 0 : k += 1
        if k == 3:
            num[i] = 0
            k = 0
            m += 1
        i += 1
        if i == n : i = 0
 
    i = 0
    while num[i] == 0: i += 1
    print (num[i])


# In[19]:

N = 3
#stu
# num : string
# name : string
# score[4]: list
student = []
for i in range(5):
    student.append(['','',[]])
 
def input_stu(stu):
    for i in range(N):
        stu[i][0] = input('input student num:\n')
        stu[i][1] = input('input student name:\n')
        for j in range(3):
            stu[i][2].append(int(input('score:\n')))
 
def output_stu(stu):
    for i in range(N):
        print ('%-6s%-10s' % ( stu[i][0],stu[i][1]) )
        for j in range(3):
            print ('%-8d' % stu[i][2][j])
 
if __name__ == '__main__':
    input_stu(student)
    print (student)
    output_stu(student)


# In[ ]:



