
# coding: utf-8

# In[2]:

class A(object):
  def caller(self):
    print ('A caller')
    self.called()
  def called(self):
    print ('A called')
class B(object):
  def called(self):
    print ('B called')
class C(B,A):
  pass
if __name__ == '__main__':
  c=C()
  c.caller()


# In[5]:

class A(object):
  def caller(self):
    print ('A caller')
    self.called()
  def called(self):
    print ('A called')
class B(object):
  def called(self):
    print ('B called')
class C(A,B):
  pass
if __name__ == '__main__':
  c=C()
  c.caller()


# In[ ]:



