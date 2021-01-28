
"""
print("Hello World")

# List : []

# list is kind of array , where we can store any type of values

list1 = [2, 'hello', 3.5, 3, 6, [3, 6, 8], 'Morning']

print(list1)

print("Zero :", list1[0])
print("Second :", list1[2])
print("Last value:", list1[-1])

print("child list element:", list1[-1][2])


list2 = [3, 6, 8, 9]


for var in [2, 3, 4, 5]
    print(var)


for num in list2:
    print(num**2)


# -------------------------------------------

dict1 = {}

dict1['name'] = 'John'
dict1['MObile'] = 2345678
dict1['sub_list'] = ['math', 'sci', 'IT']

print(dict1.keys())
print(dict1.values())

print(dict1)

print(type(dict1))

print(dict1['name'])


allkeys = dict1.keys()

print(type(allkeys))

print(list(allkeys)[0])


dict1[2] = 4

print(dict1)

list2 = [3, 5, 7, 8]

dict1[list2] = 'Number'

print(dict1)


# _________________________Tuple _________________________


# Tuple = ()
#      -> Tuple also store value in form of index
#      -> Tuple is immutable , we can not change tuple values


tuple1 = (2, 5, 6, 'Hello', [3, 5, 7, 8])

print(tuple1)
print(type(tuple1)) 

print(tuple1[0])

print(tuple1[-1])

print(tuple1[2:4]) 

"""
# ___________________________set _________________________

set1 = {}

# It does not follow index, it store the value in unorder manner
# Set store only unique values
 

set1 = {2, 5, 7, 8, 3, 4, 3, 2}

print(type(set1))

print(set1)


for i in set1:
    print(i*2)

list1 = [3, 6, 8, 2, 5, 6, 7, 8, 7]

print(set(list1))

    
    
