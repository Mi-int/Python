#!/usr/bin/env python
# coding: utf-8

# In[1]:


# def 함수명([입력 매개변수 목록]):
#  수행할 일
def addxy(x,y):
  return x+y
# 두개 인자를 전달받아 더한 값을 반환하는 함수


# In[2]:


# 함수명([입력 인자 목록])
print(addxy(2,3))
print(addxy(1,3))
print(addxy(2,5)) # addxy 함수로 호출


# In[3]:


# 자주 사용하는 코드를 함수로 정의 > 호출
def print_one():
  print("one") # one을 출력하는 함수 정의


# In[4]:


print_one()
print_one()
print_one() # 함수 호출


# In[5]:


# 인자 개수 확인을 위해 함수 정의
def printn(message, n):
  for _ in range(n):
    print(message,end=' ') # 메세지와 횟수를 전달 후 출력
  print() 


# In[6]:


printn("whatchamacallit",3) # 메세지 반복 출력 확인


# In[7]:


printn("whatchamacallit") # 인자 개수 없으면 Error 발생


# In[8]:


def print_area(radius, radian=2*3.14): # 원의 면적 출력 함수
  print(f'area:{radius*radius*radian/2}') # radian은 2 PI로 디폴드값 지정


# In[9]:


print_area(1,3.14) # 디폴드 매개 변수도 호출시 값 전달 사용 가능


# In[10]:


print_area(1) # 디폴트 매개변수 값을 전달하지 않으면 디폴트 값으로 동작


# In[11]:


def foo(a,b=0,c=1):
  print(f"a:{a} b:{b} c:{c}")

foo(2)
foo(2,b=2)
foo(2,c=2)
foo(2,c=2,b=4) # 두개 이상 있을때, 매개변수의 전달 순서가 바뀌어도 작동


# In[13]:


def whatisay(*args): # 가변 입력 매개변수는 입력 매개변수의 개수가 정해지지 않음.
  for arg in args: #입력 매개변수 앞에 *를 붙여 가변임을 표시
    print(arg)

whatisay(1,2,3,'whatchamacallit')


# In[14]:


def getsum(ls): #return으로 수행결과 반환
  s = 0
  for e in ls:
    s += e
  return s #return뒤에 값 표현.

s = getsum([1,4,2,3])
print(s)  


# In[15]:


def soo(num):
  print('soo 1')
  if num>0:
    print(num) 
  else:
    return #함수를 끝내기 위한 목적으로도 사용 가능
  print('soo 2')  


# In[16]:


soo(4)


# In[17]:


soo(-1) # 양수가 아닐시 return으로 인한 종료


# In[ ]:




