#!/usr/bin/env python
# coding: utf-8

# In[1]:


tup1 = (1,2,3)
print(type(tup1))
print(tup1) #tuple 형태 확인. 소괄호에 값을 열거하는 형태


# In[2]:


tup2 = 1,2,3
print(type(tup2))
print(tup2) # 소괄호 없어도 값 열거


# In[3]:


tup3 = (1,2.0, 'a')
print(type(tup3))
print(tup3) # 다른 형태여도 tuple 형식.


# In[4]:


tup4 = (1,'a',tup2)
print(type(tup4))
print(tup4) # 다른 tuple 도 요소로 사용 가능


# In[5]:


for e in tup4:
  print(e, end=' ') # tuple for 문의 in 뒤에 올수 있음.
                    # for문은 같은 작업을 수행할때 유용


# In[6]:


print(tup4[0])
print(tup4[1]) # 인덱스 연상 사용


# In[7]:


lst1 = [1,2,3]
print(type(lst1))
print(lst1) # 대괄호에 요소 열거


# In[8]:


lst2 = [1,'a',[1,2,3]]
print(type(lst2))
print(lst2) #tuple과 같이 다양한 형식 요소 확인


# In[9]:


print(lst2[0])
print(lst2[1]) # 인덱스 연산 사용


# In[10]:


for e in lst2:
  print(e, end=' ') # for 문의 in 뒤에 표현 가능


# In[11]:


lst3 = [1,2,3,4,5]
lst3[0] = 9
for e in lst3:
  print(e, end=' ') # tuple과 다르게 요소 변경 가능


# In[ ]:


print(len(lst3))
print(sum(lst3)) # 길이는 len, 합계는 sum 함수 사용

