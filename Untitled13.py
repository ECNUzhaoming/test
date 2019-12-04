
# coding: utf-8

# In[1]:

if __name__ == '__main__':
    sum = 4
    s = 4
    for j in range(2,9):
        print (sum)
        if j <= 2:
            s *= 7
        else:
            s *= 8
        sum += s
    print ('sum = %d' % sum)


# In[2]:

if __name__ == '__main__':
    n = 1
    while n <= 7:
        a = int(input('input a number:\n'))
        while a < 1 or a > 50:
            a = int(raw_input('input a number:\n'))
        print (a * '*')
        n += 1


# In[3]:

if __name__ == '__main__':
    import time
    start = time.time()
    for i in range(3000):
        print (i)
    end = time.time()
 
    print (end - start)


# In[ ]:



