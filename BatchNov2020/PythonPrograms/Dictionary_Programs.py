dict1 = {}

"""
1. Dict store data unstructure manner means there is no index.
2. Dict store in key value format
3. Key should always be unique
4. All immutable data type can be key , string, int, tuple
5. we can not add list as key : Muttable
6. Any type of data can be added as value
"""
"""
print(type(dict1))

# Add data in dict
#dict1['key'] = value

dict1['name'] = 'John'

print(dict1)

dict1[1] = [3, 5, 7]

dict1[(3, 5, 7)] = 2

dict1['data'] = {'city':'Mumbai', 'Address': 'Voriwali'}

print(dict1)

# add list as key : it wont allow to add list as key

#dict1[[3, 5, 7]]  = 'Listdata'

#print(dict1)

# add dict as key in dictionary wont allow.
# dict1[{2:4}] = 'Hello'
#
# print(dict1)


############################ Method available for dict ###############

print(dir(dict1))

#clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

dict1['name']  = 'John'

# Clear method
print(dict1)
dict1.clear()
print(dict1)

# copy

dict2 = {}
dict2['name'] = 'Rahul'
dict2['city'] = 'Mumbai'

dict3 = dict2
dict4 = dict2.copy()

# dict3['address'] = 'East Mumbai'
# dict3['Language'] = 'Marathi'

dict4['Address'] = 'West Mumbai'
dict4['Language'] = 'Hindi'

# Shallo copy
# print("dict2:", dict2)
# print("dict3:", dict3)

#
print("dict2:", dict2)
print("dict4:", dict4)


# Get all keys and values
dict4 = {'name': 'Rahul', 'city': 'Mumbai', 'Address': 'West Mumbai', 'Language': 'Hindi'}

keys  = dict4.keys()
values = dict4.values()

print(keys)
print(values)

# apply loop in dict
print(dict4.items())

for k, v, in dict4.items():
    print(f"key : {k}, value: {v}")


if 'name' in dict4:
    print('it is available')
else:
    print("it is not available")


dict1 = {}

dict1['name'] = 'Manoj'

value = 2

dict1[2] = 2**2

print(dict1)


for key, value in dict1.items():
    print(key,":",value)

dict1 = {'name': 'Rahul', 'city': 'Mumbai', 'Address': 'West Mumbai', 'Language': 'Hindi'}

# remove specific with key and return value
output = dict1.pop('name')

print(output)

print(dict1)


# Remove complete item and return and tuple 
output1 = dict1.popitem()
print(output1)
print(dict1)


# Update : update one dict from another dictionary

dict1 = {'name': 'hary', 'city' : 'newyork'}

dict2 = {'Address' : 'Valley',  'mob': 23456}

#
dict1.update(dict2)
print(dict1)
print(dict2)


# Program : get all char along with their count:
str1 = "Random data that can pick for practice"
dict_data = {}
dict2 = {}

for char in str1:
    #print(char)
    #print(dict1)
    char_count = str1.count(char)
    dict_data[char] = char_count

print(dict_data)

for char in str1:
    if char in dict2:
        dict2[char] += 1
    else:
        dict2[char] = 1

print(dict2)

# dict1['a']  = 4
# dict1['a']  = 5
#
# print(dict1)


student_dict = {}
teacher_dict = {}

while True:
    print("1. Add students \n"
          "2. Remove student \n"
          "3. show student data\n"
          "4. Add Teachers\n"
          "5. Remove Teachers\n"
          "6. Show teacher details\n")

    user_input = int(input("Please select your option :"))

    if user_input == 1:
        student_id = input("Please enter student id number")
        st_name = input("Please enter student name")
        st_email = input("Please enter student email")
        student_dict[student_id] = [st_name, st_email]

    elif user_input == 2:
        student_id = input("Please enter student id number")
        student_dict.pop(student_id)
        print("Student data has been removed successfully")

    elif user_input == 3:
        for key, value in student_dict.items():
            print(key, ":", value)
    else:
        print("Choose another number")



    print("__"*50)

#############################################

"""

import random

list1 = [3, 5, 7, 8]
random.shuffle(list1)
print(list1)