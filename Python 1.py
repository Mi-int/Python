#!/usr/bin/env python
# coding: utf-8

# In[1]:


2+3


# In[2]:


2-3


# In[3]:


2*9


# In[4]:


a = 10
a = a+2
a


# In[5]:


a = a*2
a


# In[6]:


print(a)


# In[7]:


b = a - 2 #b에 a-2 입력


# In[8]:


b


# In[9]:


print(a,b,20)


# In[10]:


print("python")


# In[11]:


print("python")
print(10)
print("jupyter")


# In[12]:


print('\tself\nmade\torange')


# In[15]:


print('I\'m a boy') # \' 로 따옴표 표시 가능


# In[16]:


print('He said\"Hi\"to me')# \" 로 따옴표 표시 가능


# In[18]:


A = """
\'Cause I know what you like boy
You're my chemical hype boy
내 지난날들은
눈 뜨면 잊는 꿈
Hype boy 너만 원해
Hype boy 내가 전해
"""
print(A) # """ 으로 여러줄로 표현한 문자열 생성


# In[19]:


B = """\'Cause I know what you like boy
You're my chemical hype boy
내 지난날들은
눈 뜨면 잊는 꿈
Hype boy 너만 원해
Hype boy 내가 전해\
"""
print(B) # """ 으로 여러줄로 표현한 문자열 생성, \으로 앞 뒤 개행 삭제


# In[20]:


width = 10
height = 15
rect_area = width * height
print("너비:",width, "높이:",height, "사각형 면적:",rect_area) # 변수 대입


# In[21]:


name = input("이름:")
num = input("번호:")
print("이름:",name, "번호:",num) # input 함수로 출력할 내용 입력 (문자열)


# In[22]:


n1 = input("첫 번째 수:")
n2 = input("두 번째 수:")
print("첫 번째:",n1, "두 번째:",n2)
print("합계:",n1+n2) # input으로 합할 값 입력


# In[23]:


print(type(n1)) # str 형태 확인


# In[24]:


n1 = int(n1)
n2 = int(n2)
print("첫 번째:",n1, "두 번째:",n2)
print("합계:",n1+n2) # int로 정수형 값 입력


# In[37]:


korea = int(input("국어 점수:"))
math = int(input("수학 점수:"))
print("국어:",korea, "수학 점수:",math, "합계:",korea+math) # input 함수 호출 후 정수형식으로 변환


# In[34]:


strkorea = str(korea)
print(type(korea),type(strkorea))
print(korea,strkorea)

strmath = str(math)
print(type(math),type(strmath))
print(math,strmath) # type 함수로 각 타입 확인 및 str num 별 출력값 확인


# In[35]:


print(korea+math, strkorea+strmath) # str 값은 문자열 값으로 합쳐진 것을 확인


# In[36]:


pi = float(input("파이:"))
print(pi)
print(type(pi)) # 실수를 입력 받을때는 float(input(프롬프트))


# In[ ]:




