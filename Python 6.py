#!/usr/bin/env python
# coding: utf-8

# In[2]:


lst = []
for x in range(1,20,3):
  lst.append(x)
print(lst) # 1부터 20까지의 3간격의 요소를 리스트에 추가


# In[3]:


lst = [x for x in range(1,20,3)]
print(lst) #다음과 같이 컴프리헨션으로 표현 가능


# In[4]:


lst=[]
for x in range(1,20):
  if x%3 == 0 or x%5==0:
    lst.append(x)
print(lst) # 1에서 19까지 3의 배수와 5의 배수 리스트


# In[6]:


#변수 = [표현 for 변수 in 컬렉션 if 조건]
lst = [x for x in range(1,20) if x%3==0 or x%5 == 0]
print(lst) # 리스트 컴프리헨션


# In[7]:


lst=[]
for x in range(1,20):
  if x%3 == 0 or x%5==0:
    lst.append(x)
  else:
    lst.append(-x)
print(lst) # 위 조건 외의 값은 음수


# In[8]:


#변수 = [표현1 if 조건 else 표현2 for 변수 in 컬렉션]
# 표현 1은 if 조건 참일 때, 표현 2는 else일 때
lst = [x if x%3==0 or x%5 == 0 else -x for x in range(1,20) ]
print(lst) # 


# In[1]:


# dictionary는 중괄호에 아이템을 열거하는데 키와 값은 콜론으로 구분함.
# 변수 = {키:값, 키:값, 키:값, …}
num_dic = {1:"One",2:"Two",3:"Three" }
print(num_dic) #정수를 키, 문자열을 값으로 하는 사전을 표현


# In[2]:


print(num_dic[1]) # 인덱스 연산에 키를 넣으면 값 참조 가능


# In[3]:


num_dic[4] = "Four"
print(num_dic) # dictionary에 보관할때도 인덱스에 키를 넣고 값을 대입 연산을 이용


# In[4]:


del num_dic[2]
print(num_dic) #dictionary에 아이템을 삭제할 때는 del 이용


# In[5]:


number = int(input("번호:"))
if number in num_dic:
  print(num_dic[number])
else:
  print(number," 없음.") #키를 이용하여 멤버쉽 연산(in)을 사용


# In[6]:


for elem in num_dic:
  print(elem,end=' ') # for 문의 in 뒤에 dictionary 변수가 오면 키를 반복 참조 가능


# In[7]:


for item  in num_dic.items():
  print(item) # 키와 값을 모두 확인하려면 dictionary의 items 메서드를 이용


# In[8]:


for key,value in num_dic.items():
  print(key,":",value) # 위와 같은 응용 가능


# In[9]:


group_dic = {}
group_dic["kor"] = ["하나","둘","셋"]
group_dic["eng"] = ["One","Two","Three"]
print(group_dic) # dictionary의 키와 값은 어떠한 형식도 올 수 있음
#다음은 키로 문자열 값으로 리스트인 dictionary


# In[10]:


# set은 단어 그대로 집합
s = {1,3,4,5,3,2,4,5}
print(s) # set은 중괄호 표현, 같은 원소를 보관하지 않습니다.


# In[11]:


number = int(input("번호:"))
if number in s:
  print("있음.")
else:
  print("없음.") #set도 멤버쉽 연산 in 사용 가능


# In[12]:


s.add(6)
print(s) # set에 원소 추가할 때는 add 메서드 사용


# In[13]:


s.add(4)
print(s) # 이미 있는 원소는 변화하지 않음.


# In[14]:


s.remove(4)
print(s) # remove로 원소 삭제 가능


# In[15]:


s.remove(4)
print(s) # 없는 원소를 KeyError


# In[17]:


s.discard(4)
print(s) #discard를 이용해 원소 삭제 가능.
#remove와 다르게 오류가 발생하지 않음


# In[18]:


s1 = {x for x in range(2,30,2)} # 30미만 2의 배수 집합
s2 = {x for x in range(3,30,3)} # 30미만 3의 배수 집합
print(s1)
print(s2)


# In[19]:


s3 = s1|s2 #합집합 |
print(s3)
s3 = s1.union(s2) #합집합 union
print(s3)


# In[20]:


s4 = s1 & s2 # 교집합 &
print(s4) 
s4=s1.intersection(s2) # 교집합 intersection
print(s4) 


# In[21]:


s5 = s1 - s2 #차집합 -
print(s5) 
s5 = s1.difference(s2) #차집합 difference
print(s5)


# In[22]:


s6 = s1 ^ s2 # 대차집합 ^
print(s6)
s6 = s1.symmetric_difference(s2) # 대차집합 symmetric_difference
print(s6)


# In[ ]:




