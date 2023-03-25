#!/usr/bin/env python
# coding: utf-8

# In[2]:


lst = list() #빈 리스트 생성
for i in range(1,10):
  lst.append(i) #요소를 append를 통해 순차 보관
print(lst)


# In[3]:


lst.append('a')
print(lst) # a가 맨 마지막에 추가 된 것을 확인


# In[4]:


lst.insert(2,'z')
print(lst) # 원하는 위치에 추가는 insert(index, 요소)를 사용


# In[6]:


lst1 = [1,2,3,4]
lst2 = ['a','b','c']

print(lst1)
print(lst2)
lst1.extend(lst2) #lst 1에 lst2를 병합하기 위해 extend() 사용
print(lst1) #lst1에 lst2추가
print(lst2) #lst2는 변화 없음


# In[7]:


lst = [10,11,12,13,14,15]
print(lst)
re = lst.pop()  #list.pop([index])
# pop 메서드는 맨 뒤 혹은 원하는 위치의 요소를 꺼냄
# pop 메서드에 입력 인자를 전달하지 않으면 맨 마지막 요소를 꺼냄. > 반환함
print("re:",re)
print(lst) 


# In[8]:


re = lst.pop(2) # pop 메서드에 입력 인자로 인덱스 전달해 해당 위치로 요소 꺼냄
print("re:",re)
print(lst)


# In[9]:


re = lst.remove(11) #list.remove(index) 
# remove 메서드는 특정 요소를 제거 할 때 사용
# remove 값은 아무런 값도 반환하지 않음
print("re:",re)
print(lst)


# In[10]:


lst.clear() # 리스트의 모든 요소를 제거 할 때는 clear를 사용
print(lst)


# In[12]:


lst1 = [1,2,3]
lst2 = [4,5,6]

lst3 = lst1 + lst2 # 연산 상자 병합

print(lst3)


# In[13]:


lst4 = lst1 * lst2
print(lst4) # 리스트 끼리의 연산에 곱셈은 제공되지 않음


# In[15]:


lst5 = lst1*3
print(lst5) # 곱셈은 요소 반복 배치할때 사용


# In[17]:


lst6 = lst2-lst1
print(lst6) # 뺄셈 연산은 제공되지 않음


# In[18]:


list1 = list()
for i in range(5):
  value = int(input("{i+1}번째 >>"))
  list1.append(value)
print(list1) # 5개의 정수를 입력 받는 코드 작성


# In[19]:


list1.sort()
print(list1) # sort 메서드를 통해 오름차순으로 배치


# In[20]:


list1.sort(reverse=True)
print(list1) # sort 메서드의 reverse = TRUE를 통해 내림차순으로 배치


# In[21]:


lst=[2,5,3,7,8,1]
lst.reverse()
print(lst) # 리스트에는 reverse 메서드 제공. 역순으로 재생되는 것을 확인


# In[22]:


lst2 = lst.copy()
print(lst2) # 리스트 복사


# In[23]:


lst = [1,5,2,9]
i = lst.index(9)
print(i) # 리스트에 보관한 요소의 위치 확인할때 index 메서드 사용


# In[24]:


i = lst.index(11)
print(i) # 보관하지 않은 값을 입력인자로 전달하면 예외 발생


# In[ ]:




