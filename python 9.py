#!/usr/bin/env python
# coding: utf-8

# In[1]:


# lambda 입력인자목록: 수행코드
# 명명하지 않은 알고리즘 코드로 간단하게 알고리즘 표현
# 전달 값에 1을 더한 함수
def add_one(x):
  return x+1
print(add_one(1))


# In[2]:


# lambda로 표현
fun = lambda x: x+1
print(print(fun(1))


# In[4]:


# 콜백은 함수 호출시 알고리즘을 입력인자로 전달.

def cb_fun(msg,ls):
  print(msg)
  for e in ls:
    print("this is callback:",e)


# In[5]:


# 전달받은 알고리즘은 호출하는 것도 가능
def print_sort_ba(ls,cb):
  cb("before",ls)
  ls.sort()
  cb("after",ls)


# In[6]:


# print_sort_be 함수를 호출할 때 두번째 인자로 알고리즘 전달
print_sort_ba([1,3,5,2,6,7,3],cb_fun)


# In[8]:


# print_sort_be 함수에서 cb_fun 함수 호출
# sorted의 key 파라미터에 람다식으로 알고리즘 전달
# sorted 함수에 문자, key에 숫자를 전달해 이름순으로 정렬
letters = [["나",3],["너",5],["우리",4],["너네",7]]
s_letters = sorted(letters,key=lambda m:m[0])
print(s_letters)


# In[9]:


# filter는 컬렉션에 특정 알고리즘을 적용했을때 참인 요소를 필터링하는 개체 생성
# filter(알고리즘, 컬렉션)
# map은 컬렉션의 모든 요소에 특정 알고리즘을 적용하는 개체를 생성
# map(알고리즘, 컬렉션)
#0~19 범위의 요소 지정
lst = list(range(20))
print(lst)


# In[10]:


even_filter = filter(lambda x:x%2==0,lst) # 2로 나눠 몫이 0이면 참
e_lst = list(even_filter) # 참인 요소만 추출
print(e_lst)


# In[11]:


sq_map = map(lambda x:x**2, lst) # 제곱계산 알고리즘
sq_lst = list(sq_map) #map은 컬렉션의 모든 요소에 해당 알고리즘 수행하는 개체 반환
print(sq_lst) #0~19 값의 제곱 요소


# In[12]:


a = 2,3 #튜플로 여러개의 값 반환
print(type(a))
print(a)


# In[14]:


def get_sum_average(lst):
  s = 0
  for e in lst:
    s += e
  return s, s/len(lst) # 요소 합계와 평균을 반환하는 함수


# In[15]:


lst = [1,6,3,7,9,5]
re = get_sum_average(lst)
print(re) # 값 반환


# In[16]:


s,aver = get_sum_average(lst)
print(f"합계:{s} 평균:{aver:.2f}") #튜플의 요소개수 만큼 변수 선언 사용


# In[ ]:




