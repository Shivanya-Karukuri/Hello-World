#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data={"name":["A","B","C","D"],"Age":[23,24,21,25],"salary":[23000,24000,25000,26000]}


# In[2]:


df=pd.DataFrame(data)


# In[3]:


df["location"]=["Hyderabad","Pune","Bangaluru","Karimnagar"]


# In[4]:


df


# In[5]:


df_fil=df[df["Age"]>22]
df_fil


# In[6]:


df.replace(23,21)


# In[7]:


df.replace(23,21,inplace=True)


# In[8]:


df


# In[9]:


df["salary"].mean()
df["salary"].sum()


# In[10]:


df.isna().sum()


# In[11]:


df.drop("location",axis=1)


# In[12]:


df.drop(index=1)


# In[13]:


df.drop(index=1).reset_index().drop("index",axis=1)


# In[14]:


#matplotlib
import matplotlib.pyplot as plt


# In[15]:


plt.plot(df["name"],df["Age"])
plt.show()


# In[16]:


plt.bar(df["name"],df["Age"])
plt.show()


# In[17]:


data1={"ID":[1,2,3,4],"Name":["s","p","h","r"],"Age":[23,24,25,26]}
df1=pd.DataFrame(data1)
data2={"ID":[5,3,7,8],"occupation":["data analyst","Civil","eng","acc"],"City":["Hyd","KNR","GDK","HYD"]}
df2=pd.DataFrame(data2)
concate_df=pd.concat([df1,df2],ignore_index=True)
concate_df


# In[18]:


merge_data=pd.merge(df1,df2,on="ID")


# In[19]:


merge_data


# In[20]:


pivot_df=df.pivot(index="name",columns="location",values="Age")
pivot_df


# In[21]:


plt.pie(df["salary"],labels=df["name"],colors=["pink","green","yellow","blue"],autopct="%1.0f%%",shadow=True)
plt.show()


# In[22]:


x=[11,23,45,67]
y=[23,78,56,46]
plt.plot(x,y)
plt.title("gvxchk")
plt.xlabel("rty")
plt.ylabel("cvbn")


# In[23]:


#plot the graf for y=x*2
x=[1,2,3,4,5,6,-5,-4,-3,-2,-1]
y=[]
for i in x:
    i=i**2
    print(y)
    y.append(i)
plt.plot(x,y)
plt.title("gvxchk")
plt.xlabel("rty")
plt.ylabel("cvbn")


# In[24]:


x=[x for x in range(-10,10)]
y=[i**2 for i in x]
print(x)
print(y)
plt.plot(x,y)
plt.title("gvxchk")
plt.xlabel("rty")
plt.ylabel("cvbn")


# In[25]:


x=[x for x in range(-10,10)]
y=[i**3 for i in x]
print(x)
print(y)
plt.plot(x,y)
plt.title("gvxchk")
plt.xlabel("rty")
plt.ylabel("cvbn")


# In[26]:


n=int(input("enter the power:"))
x=[x for x in range(-10,10)]
y=[i**n for i in x]
print(x)
print(y)
plt.plot(x,y)
plt.title("gvxchk")
plt.xlabel("rty")
plt.ylabel("cvbn")
plt.show()
plt.savefig("graph")


# In[27]:


import numpy as np
x=np.linspace(-10,10,20)
n=int(input("enter num:"))
y=[i**n for i in x]
print(x)
print(y)
plt.plot(x,y)
plt.title("gvxchk")
plt.xlabel("rty")
plt.ylabel("cvbn")


# In[28]:


def plot_equation():
    import numpy as np
    x=np.linspace(-10,10,20)
    n=int(input("enter num:"))
    y=[i**n for i in x]
    print(x)
    print(y)
    plt.plot(x,y)
    plt.title("gvxchk")
    plt.xlabel("rty")
    plt.ylabel("cvbn")


# In[29]:


plot_equation()


# In[30]:


m=(y[1]-y[0])/(x[1]-x[0])
m


# In[31]:


#plot the graph for y=mx+c
c=int(input("constant:"))
y=(m*x)+c
plt.plot(x,y)
plt.show()


# In[32]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x=np.linspace(0,10,400)
y=1/np.tan(x)
plt.plot(x,y)
plt.title("Graph of tan x")
plt.xlabel("x")
plt.ylabel("cot(X)")
plt.show()


# In[33]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x=np.linspace(0,10,400)
y=1/np.sin(x)
plt.plot(x,y)
plt.title("Graph of tan x")
plt.xlabel("x")
plt.ylabel("cosec(X)")
plt.show()


# In[34]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x=np.linspace(0,10,400)
y=1/np.tan(x)
plt.plot(x,y)
plt.title("Graph of tan x")
plt.xlabel("x")
plt.ylabel("cot(X)")
plt.show()


# In[35]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x=np.linspace(0,10,400)
y=1/np.cos(x)
plt.plot(x,y)
plt.title("Graph of tan x")
plt.xlabel("x")
plt.ylabel("sec(X)")
plt.show()


# In[36]:


import numpy as np
m1=np.array([[1,2,3],[4,5,6]])
m1


# In[37]:


m2=np.array([[4,5,6],[3,4,5]])
mat_add=m1+m2
mat_add
#or
a=np.add(m1,m2)
a


# In[38]:


a[0]


# In[39]:


m2[0:3,1:3]


# In[40]:


mat_mul=np.multiply(m1,m2)
mat_mul


# In[41]:


mat_mod=np.mod(m1,m2)
print(mat_mod)


# In[42]:


mprod=m1*m2
print(mprod)


# In[43]:


m3=[2,3,4]
m_dot_prod=np.dot(m1,m3)
print(m_dot_prod)


# In[44]:


mat_tranve=np.transpose(m1)
mat_tranve


# In[45]:


matrix=np.array([[2,3,7],[4,7,8],[3,7,5]])
inverse=np.linalg.inv(matrix)
inverse


# In[46]:


det_matrix=np.linalg.det(matrix)
det_matrix


# In[47]:


#solve 2x+y=8, 3x+4=18 using matrix
m1=np.array([[2,1],[3,4]])
co_m2=np.array([8,18])
solution=np.linalg.solve(m1,co_m2)
print(solution)


# In[48]:


#solve 3x+4y=10, x+y=5
m1=np.array([[3,4],[1,5]])
co_m2=np.array([10,10])
solution=np.linalg.solve(m1,co_m2)
print(solution)


# In[49]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv(r"D:\data sets\Amazon.csv",encoding='unicode_escape')
df


# In[50]:


df.info()


# In[51]:


df.info()


# In[52]:


df.isna().sum()


# In[53]:


df.drop(["Status","unnamed1"],axis=1,inplace=True)


# In[54]:


df.isna().sum()


# In[55]:


df.info()


# In[56]:


print(df)


# In[57]:


sales_gen = df.groupby(["Gender"])["Amount"].sum().reset_index()
print(sales_gen)


# In[58]:


import seaborn as sns
import pandas as pd

# Assuming 'df' is your DataFrame containing sales data
sales_gen = df.groupby(['Gender'], as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False)
sns.barplot(x="Gender", y="Amount", data=sales_gen)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




