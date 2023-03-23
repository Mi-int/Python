#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(type(True))
print(type(False)) #형식이 bool 인 것을 확인


# In[2]:


# and 일 때 연산 결과
print(f"False and False = {False and False}")
print(f"False and True = {False and True}")
print(f"True and False = {True and False}")
print(f"True and True = {True and True}") 


# In[3]:


# or 일 때 연산 결과
print(f"False or False = {False or False}")
print(f"False or True = {False or True}")
print(f"True or False = {True or False}")
print(f"True or True = {True or True}")


# In[4]:


# not일 때 연산 결과
print(f"not True = {not True}")
print(f"not False = {not False}")


# In[5]:


#정수가 짝수인지 아닌지 확인 판별
# 같을땐 == 을 사용
i = int(input("정수:"))
i%2 == 0


# In[6]:


# 정수가 홀수인지 판별
# 다를땐 != 사용
i = int(input("정수:"))
i%2 != 0


# In[7]:


# 두개의 정수끼리 크기 비교
num1 = int(input("정수:"))
num2 = int(input("정수:"))

num1<num2, num1<=num2, num1>num2, num1>=num2


# In[8]:


# if 조건 표현 : 참일 때 수행할 표현
# 점수를 벗어나지 않을때 출력
num = int(input("0 ~ 100 사이의 입력값 :"))
if 0<=num<=100: #if 조건:
  print(f"입력한 값은 {num}.")


# In[13]:


# 참일때 수행할 구문은 들여쓰기 잘 봐야함
# 들여쓰기를 하지 않으면 if 문은 끝난 것으로 간주
num = int(input("0 ~ 100 사이의 입력값 :"))
if 0<=num<=100: #if 조건:
  print(f"입력한 값은 {num}.")
  print("들여쓰기 해서 보임")
print("그냥 보임")


# In[17]:


# if 조건 표현 : 참일 때 수행할 표현  
# else: 거짓일 때 수행할 표현

#점수를 입력 받은 뒤 벗어나지 않을 때 출력
num = int(input("0 ~ 100 사이의 입력값 :"))
if 0<=num<=100: #if 조건:
  print(f"입력한 값은 {num}.")
else:
  print("범위를 벗어난 값을 입력.")


# In[23]:


# if 조건 표현 A:  A 조건이 참일 때 수행할 표현  
# elif 조건 B:  B 조건이 참일 때 수행할 표현(A조건은 거짓)
# else:  모든 조건이 거짓일 때 수행할 표현

num = int(input("0 ~ 100 사이의 입력 값 :"))
if 0<=num<=100: #if 조건:
  print(f"입력한 값은 {num}.")
  if num>=80:
    print("A")
  elif num>=60:
    print("B")
  elif num>=40:
    print("C")
  elif num>=20:
    print("D")
  else:
    print("E")
else:
  print("범위를 벗어난 값을 입력.")


# In[24]:


# while 조건 표현: 참일 때 수행할 표현 (반복 수행할 구문)
#1부터 10까지 정수의 합계

sum = 0 #sum를 0으로 초기화  
i = 1 #i를 1로 초기화
while i<=10: #반복 i가 10보다 작거나 같다면
  sum += i #sum 에 i를 더하기
  i += 1#i를 1증가
print("1부터 10까지 정수의 합계:",sum)#결과를 확인


# In[26]:


#사용자가 입력한 정수의 합계를 구하라.
#사용자가 음수를 입력하면 멈춘다.

sum = 0 #sum 를 0으로 초기화
number = 0 #number를 0으로 초기화
while number>=0:#반복 number가 음수가 아니라면
  sum += number #sum에 number를 더하다.
  number = int(input("정수: "))#number = 사용자로부터 정수를 입력받는다.
print("결과: ",sum)#결과를 확인


# In[27]:


# for 변수 in 컬렉션: 반복 수행할 구문
i=0
while i<10:
  print(i,end=' ') #i를 출력 (개행 대신 공백을 출력)
  i+=1


# In[28]:


for i in range(0,10): #range는 특정 구간의 순차적인 수로 구성
  print(i,end=' ')


# In[ ]:




