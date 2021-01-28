tuple1 = (1, 4, 7)
print(type(tuple1))

# 1. It Follow index similar like list and string
# 2. Can add any type of data in the tuple
# 3. Tuple is immutable , we can not change its values.

# Method :

print(dir(tuple1))


#count', 'index'
        #  0  1  2  3    4     5
tuple2 = (3, 6, 8, 'a', 'xyz', 3, 7, 2, 8)

print("index :", tuple2.index('a'))
print("count : ", tuple2.count(8))


# Slicing
print(tuple2[0: 5])

print(tuple2[:2])

print(tuple2[3:])

tp3  = (4, 6, 8, 9, 2)
tp4  = (6, 8, 0, 3, 4)

tp5 = tp3 + tp4
print(tp5)

tp5 = tp3

print(tp5)


# check any number available in tuple or not.

x = 6

tp_new = (4, 7, 9, 3, 5)

if x in tp_new:
    print(True)
else:
    print(False)

result = True if x in tp_new else False

print(result)

"""
if condition:  
   code
elif condition
    code
elif condition
    code
else:

###### Nested If condition ##########

if condition
    code
    if condition
         code
         if condition
             code
             
             
# 


print(1)
print(2)
print(3)

for i in range(10):
    print(i)


for i in range(10):
    for j in range(3):
        print(i, j)


"""
