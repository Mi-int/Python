#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = int(input("정수:")) 
print(num)


# In[2]:


print(type(3))
print(type(3.2))
print(type('a')) # 특정 값이 어떤 자료형인지 확인


# In[3]:


a = 2
b = 2.3
c = 'hello'
print(type(a))
print(type(b))
print(type(c)) # 특정 변수가 어떤 타입인지 확인


# In[4]:


ls = [1,2,3]
a = 2.3
if isinstance(ls,list): #isinstance 특정 변수가 list형식인지 판별
  print("Yes")
else:
  print("No")

if isinstance(a,list):
  print("Yes")
else:
  print("No")


# In[5]:


print(ord('a'))
print(ord('z'))
print(ord('A'))
print(ord('Z'))
print(ord('0'))
print(ord('9')) # 문자 코드 값을 확인하는 ord 함수


# In[6]:


# 데이터 분석이나 머신러닝 등의 작업을 할 때 는 분류를 위해 영문 알파벳으로 클래스 지정
for code in range(ord('a'),ord('z')+1):
  print(code,':',chr(code)) #소문자 a~ z사이의 문자 코드 값을 통해 문자를 확인


# In[7]:


print(len('abc'))
ls=[1,4,2,5,6,7,3]
print(len(ls)) # len 함수로 문자열의 길이나 컬렉션의 요소 개수 확인


# In[8]:


print(sum(ls)) # sum 컬렉션 내 요소 합계 반환
print(min(ls)) # min 최솟값 반환
print(max(ls)) # max 최댓값 반환


# In[9]:


print(range(10))


# In[10]:


for r in range(10):
  print(r, end =' ') # range 함수는 시작, 끝, 간격을 입력인자로 전달


# In[11]:


for r in range(2,10):
  print(r, end =' ') #range 함수에시작과 끝 입력


# In[12]:


for r in range(2,10,3):
  print(r, end =' ') # range 함수에 시작 끝 간격 입력


# In[13]:


for r in range(10,-10,-3):
  print(r, end =' ') # range 함수에 음수 값으로 더 줄어드는 구간 형성


# In[15]:


names = ['나','너','우리']
nums = [3,2,7]
for i, name in enumerate(names): #enumerate 함수로 요소 뿐 아니라 인덱스로 참조
  print(nums[i],':',name) # 2개 이상 컬렉션으로 관리하는 자료를 같은 인덱스로 접근하고 자 할때 사용


# In[16]:


sorted_nums = sorted(nums)
print(sorted_nums) #sorted 함수로 정렬한 컬렌션 반환


# In[17]:


# zip 함수는 두 개의 컬렉션을 같은 요소끼리 결합, 열거
for num, name in zip(nums,names):
  print(num,':',name) # 입력 인자가 두개의 컬렉션. for문에서 같은 인덱스 요소 참조 가능


# In[ ]:




