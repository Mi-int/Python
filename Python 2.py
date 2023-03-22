#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(22)
a = "hello"
print(a)
print(22, a)


# In[2]:


num = 365
print("===num===")
print("10진수:",format(num,'d'))
print("8진수:",format(num,'o'))
print("16진수:",format(num,'x')) #format으로 진수별 출력


# In[3]:


print("10진수:{0:d}".format(num))
print("8진수:{0:o}".format(num))
print("16진수:{0:x}".format(num)) # 문자열 표현 뒤에 . 찍고 접근 가능


# In[8]:


a = 6
b = 8
print("a:{0} b:{1}".format(a,b))
print("{0}+{1}={1}+{0}={2}".format(a,b,a+b)) # 문자열에 {인덱스}로 출력


# In[12]:


a = 6
b = 8
print("a:{1} b:{2}".format(a,b))
print("{2}+{1}={1}+{2}={3}".format(a,b,a+b)) # 변수가 0부터 지정되지만, 0에 해당하는 값이 없으므로 오류


# In[13]:


a = 6
b = 8
c = 7
d = 2
print("a:{0} b:{1} c:{2} d:{3}".format(a,b,c,d))
print("{0}+{1}+{2}+{3}={4}".format(a,b,c,d,a+b+c+d))


# In[24]:


a = 6
b = 10
print("{0}+{1}={1}+{0}={2}".format(a,b,a+b))

print(f"a:{a} b:{b} {a}+{b}:{a+b}") #f""로 format 간편화 가능


# In[29]:





# In[ ]:




