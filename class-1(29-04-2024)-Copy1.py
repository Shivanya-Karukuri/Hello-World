#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(100):
    if i%2==0:
        print(i,"even")
    else:
        print(i,"odd")


# In[5]:


list2=[10,"raed",56,4.5,"gdjk",4.5,"IOT",45.6]
strlist=[]
intlist=[]
floatlist=[]
for i in list2:
    if type(i)==int:
        intlist.append(i)
        print("intlist",intlist)
    elif type(i)==float:
        floatlist.append(i)
        print("floatlist",floatlist)
    else:
        strlist.append(i)
        print("str list",strlist)


# In[3]:


#list comprehension
intlist=[ i for i in list2 if type(i)==int]
floatlist=[ i for i in list2 if type(i)==float]
strlist=[ i for i in list2 if type(i)==str]
print(intlist,floatlist,strlist)


# In[4]:


def add(x,y):
    return x+y
add(1,57)


# In[5]:


def separater():
    intlist=[ i for i in list2 if type(i)==int]
    floatlist=[ i for i in list2 if type(i)==float]
    strlist=[ i for i in list2 if type(i)==str]
    print(intlist,floatlist,strlist)
separater()


# In[6]:


def separater(x):
    intlist=[ i for i in list2 if type(i)==int]
    floatlist=[ i for i in list2 if type(i)==float]
    strlist=[ i for i in list2 if type(i)==str]
    print(intlist,floatlist,strlist)
list1=[10,"raed",56,4.5,"IOT",45.6]
separater(list1)


# In[4]:


def recusum(n):
    if n<=1:
        return 0
    return n+recusum(n-1)
n=10
print(recusum(n))


# In[2]:


def recur_fib(n):
    if n<=1:
        return n
    else:
        return (recur_fib(n-1)+recur_fib(n-2))
n=10
for i in range(n):
    print(recur_fib(i))
    


# In[4]:


# fact program
def recur_fact(n):
    if n==0:
        return 1
    else:
        return n*recur_fact(n-1)
n=5
print(recur_fact(n))


# In[ ]:



        


# In[2]:


#generate numbers
def gen_num(n):
    v=0
    while v<n:
        yield v
        v+=1
    for v in gen_num(100):
        print(v)


# In[11]:


print(next(gen_num(3)))
value=gen_num(3)
print(next(value))


# In[27]:


dict1={"jay":[1998,"Hyderabad"],"prajyoth":[1995,"Hyderabad"],"sudril":[1989,"Delhi"],"Sonu":1999}
len(dict1)
dict1.keys()
dict1.values()


# In[30]:


dict1={"jay":[1998,"Hyderabad"],"prajyoth":[1995,"Hyderabad"],"sudril":[1989,"Delhi"],"Sonu":1999}
count=0
for i in dict1.keys():
    if type(dict1[i]==list):
        count=count+1
count


# In[32]:


x=50
y=0
try:
    x/y
except:
    print("your code has error")
else:
    print(x/y)
finally:
    print("your code has run succesfully")


# In[34]:


import pandas as pd
df=pd.DataFrame(dict1)
df


# In[66]:


df.to_csv("dictionary.csv")


# In[16]:


file=open("text.txt","w")
file.write("this is first line")
file.close()


# In[17]:


file=open("text.txt","a")
file.write("\n this is second line")
file.close()


# In[18]:


file=open("text.txt","r")
file.read()


# In[34]:


def find_longest_word(filename):
        with open("text.txt", 'r') as file:
            content = file.read()
            words = content.split()
            longest_word = max(words, key=len)
            return longest_word
        print("The longest word in the file is:",longest_word)
find_longest_word("text.txt")


# In[13]:


with open("text.txt","r") as file:
    print(file.read())


# In[115]:


with open("text.txt","r") as file:
    word_list=file.read().split()
    print(word_list)
    len_word=[]
    for i in word_list:
        print(i,len(i))
        len_word.append(len(i))
    print("longest_word",max(word_list))


# In[116]:


df1=pd.read_csv(r"D:\data sets\employee.csv")
df1


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[117]:


#lamda functions
x=lambda r:r**2
x(10)


# In[120]:


l1=[2,4,5,7,9,11]
for i in l1:
    if i%2==1:
        print("odd",i)


# In[122]:


odd_num=list(filter(lambda i:i%2==1,l1))
print(odd_num)


# In[128]:


fruit_list=[["Mango",200],["Grapes",140],["Apples",198]]
#sort them based on quality
fruit_list.sort()
fruit_list


# In[129]:


fruit_list.sort(key=lambda i:i[1])
print(fruit_list)


# In[12]:


a=[i for i in range(10)]
x=5
a=[int(x) for x in input("enter number").split(",")]
print(a)


# In[37]:


x=lambda a,b,c:"a is great" if (a>b and a>c) else ("b is graet" if ( b>a and b>c) else c)
a=10
b=20
c=30
x(a,b,c)


# In[ ]:




