#!/usr/bin/env python
# coding: utf-8

# # 1.Hello world

# In[19]:


#printing my first messages
print("hello world!")


# In[20]:


"hello world!"


# In[21]:


print("kaushal" + "22")


# # 2.Data Type

# In[23]:


type(1)


# In[24]:


type(2.33)


# In[26]:


type("ww")


# In[28]:


1 + 33


# In[30]:


type(False)


# In[32]:


type(True)


# In[35]:


55 / 44.55


# In[38]:


x = input()
print(x + "hello")


# In[40]:


type("hhh")


# In[44]:


"hello world".title()


# In[49]:


"hello world".replace('o', 'u')


# # 3. Variable

# In[52]:


message_1 = ("i'm learing python again")


# In[53]:


message_1


# In[54]:


message_2 = ("and it's Fun")


# In[55]:


message_2


# In[56]:


print(message_1)


# In[61]:


print(message_1 + message_2)


# In[63]:


message = message_2 +' '+ message_1


# In[65]:


message


# In[67]:


f'{message_1}'


# In[69]:


f'{message_1} {message_2}'


# # 3.List

# In[71]:


countries = ['us', 'india', 'china', 'brazil', 123]


# In[73]:


countries


# In[81]:


print(countries[-1])
print(countries[1])
print(countries[-2])
print(countries[3])
print(countries[4])


# In[82]:


print(countries[-2])


# In[83]:


#slicing
list_name[start:stop]


# In[84]:


(countries[0:3])


# In[85]:


(countries[1:3])


# # 4. Adding element to a list

# In[87]:


countries


# In[88]:


countries.append('canada')


# In[89]:


countries


# In[91]:


countries.insert(0, 'spain')


# In[92]:


countries


# In[96]:


countries_2 = ['Uk', 'Germany', 'Austria']


# In[98]:


countries + countries_2


# In[102]:


nested_list = [countries, countries_2]


# In[103]:


nested_list


# # 4.1 Removing an element 

# In[105]:


countries


# In[110]:


countries.insert(0, 'us')


# In[112]:


countries


# In[114]:


countries.pop(-1)


# In[116]:


countries.append('canada')


# In[117]:


countries


# In[118]:


del countries[0]


# In[119]:


countries


# In[120]:


countries.append('us')


# In[121]:


countries


# # 4.2 Sorting List

# In[123]:


number = [3, 4, 4, 2, 7, 89, 56]


# In[124]:


number.sort()


# In[125]:


number


# In[127]:


number = [3, 4, 4, 2, 7, 89, 56]
number.sort(reverse=True)
number


# In[128]:


number = [3, 4, 4, 2, 7, 89, 56,45,455,33,4343]


# In[129]:


number.sort()


# In[130]:


number


# In[135]:


number = [3, 4, 4, 2, 7, 89, 56,45,455,33,4343]
number.sort(reverse=True)
number


# # 4.3 Update an Element 

# In[141]:


number [0] = 1000
number


# In[142]:


number [-1] = 1000
number


# # 4.4 Copying a List

# In[145]:


countries


# In[146]:


countries[:]


# In[149]:


countries = ['us', 'india', 'china', 'brazil', 123]
new_list = countries[:]


# In[150]:


new_list


# In[151]:


countries.copy()


# In[152]:


new_list2 = countries.copy()


# In[157]:


new_list2


# In[161]:


#5. Dictionary


# In[162]:


My_dict ={'key1':'value1','key2':'value2','key3':'value3'}


# In[163]:


my_data = {'name':'kaushal','age':22, 'state': 'delhi'}


# In[164]:


my_data


# In[165]:


new_list2


# In[166]:


new_list2.pop(-1)


# In[167]:


new_list2


# In[169]:


my_data.keys()


# In[170]:


my_data.values()


# In[171]:


my_data.items()


# In[172]:


my_data['hight'] = 1.9


# In[173]:


my_data


# In[190]:


my_data.update({'hight':1.9})


# In[191]:


my_data


# # 5.1 Copy a Dictionary

# In[181]:


my_data.copy()


# In[183]:


new_dict = my_data.copy()


# In[187]:


new_dict


# In[188]:


new_dict2 = my_data


# In[192]:


new_dict2


# # 5.2 Removin Element

# In[194]:


my_data.pop('name')


# In[195]:


my_data


# In[196]:


del my_data['age']


# In[197]:


my_data


# In[198]:


my_data.clear()


# In[199]:


my_data


# # 6 If Statement 

# 
# if <condiotion>:
#     <code>
#         elif <condition>:
#         ...
#         else:
#         <code>

# In[213]:


age = 14

if age>=18:
    print("you're an adult")
elif age>=13:
    print("you're a teenager")
elif age>=50:
        print("you're going to die")
else:
        print("you're a kid")


# # 7 Foor Loop

# for<variable> in <list>:
#     <code>

# In[222]:


countries


# In[223]:


for countries in countries:
    print(countries)


# In[219]:


for i, country in enumerate(countries):
    print(i)
    print(country)


# In[1]:


countries


# In[2]:


countries


# In[3]:


countries = ['us', 'india', 'china', 'brazil', 123]


# In[4]:


countries = ['us', 'india', 'china', 'brazil', 123]


# In[5]:


countries


# In[6]:


for countries in countries:
    print(countries)


# In[8]:


for i, country in enumerate (countries):
    print(i)
    print(country)


# In[9]:


countries.pop(-1)


# In[10]:


del countries(123)


# In[11]:


countries


# In[12]:


countries


# In[14]:


countries = ['us', 'india', 'china', 'brazil']


# In[15]:


countries


# In[16]:


for i, country in enumerate (countries):
    print(i)
    print(country)


# In[17]:


my_data


# In[18]:


my_list


# In[19]:


my_data = {'name':'kaushal','age':22, 'state': 'delhi'}


# In[20]:


my_data


# In[21]:


for key, value in my_data.items():
    print(key)
    print(value)


# # 8 Function

# def funtion<params>:
#     <code>
#         return <data>

# In[49]:


def sum_valuess(c,d):
    x = c*d
    return


# In[47]:


sum_values(5, -6)


# In[42]:


def sum_valuess(c,d):
    x = c*d
    return


# In[44]:


sum_values(5, 8)


# In[45]:


sum_values(5, 68)


# # 8 Built-in Function 

# In[50]:


countries


# In[51]:


len(countries)


# In[56]:


min([10,20,30,40,364,44,33,44,])


# In[57]:


max([10,20,30,40,364,44,33,44,])


# In[58]:


type(countries)


# In[59]:


type(12)


# In[65]:


for i in range(1, 1000, 300):
    print(i)


# In[66]:


for i in range(3, 9, 1):
    print(i)


# #  Module

# In[ ]:


import


# # 9.1 Os module

# In[68]:


import os


# In[69]:


os.getcwd()


# In[70]:


os.listdir()


# In[72]:


os.makedirs("new_folder")


# In[73]:


os.listdir()


# In[10]:


import numpy as np


# In[12]:


get_ipython().system('pip install panda')


# In[13]:


import panda as pd


# In[7]:


pip install panda


# In[11]:


get_ipython().system('pip install requests')


# # 1 Creating a dataframe from an array

# # 1.1 Option 1

# In[4]:


# creating an array
data = np.array([[1,4], [5,6], [5,5]])


# In[5]:


# creating a dataframe
pd.DataFrame(data)


# In[ ]:


# showing adataframe


# In[ ]:





# In[ ]:




