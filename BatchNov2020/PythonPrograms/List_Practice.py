# Mutable data type : The data can be modified
"""
list1 = []

list1 = [2, 'a', 'Hello', 3.0, True]
        #0   1     2       3    4

print(type(list1))

print(list1[0])

output = list1[0:2]
print("output", type(output), output)

reverse_list = list1[::-1]
print(reverse_list)

list1.append(34)

print("list1", list1)

############################################################

list1 = [3, 5, 6]

print(dir(list1))

# append', 'clear', 'copy', 'count', 'extend',
# 'index', 'insert', 'pop', 'remove', 'reverse', 'sort, max, mini, sum
#  list comprehension, deep copy and shallow copy.


# Append : Append data in a list at the end.

list1 = [4, 6, 7, 8]

list1.append(10)
list1.append("Hello")
list1.append(23.0)
print(list1)

# append list inside a list
list2 = [12, "Morning", 22.5]

list1.append(list2)

print(list1)

print(list1[7])

print(list1[7][1])


# Extend : This method add two list together or merge two list

lista = [5, 7, 9]
listb = [7, 3, 'a']

listc = lista + listb
print(listc)
print(lista)
print(listb)


# lista.extend(listb)
# print("lista:", lista)
# print("listb:", listb)

listb.extend(lista)

print("lista:", lista)
print("listb:", listb)

#######################################
# Insert  :  insert data at specific position.
       #  0   1     2    3
list1 = ['a', 'b', 123, 21.0]
       #  -4   -3   -2    -1

val = "abc123"

list1.insert(2, val)

print(list1)
val2= 45
list1.insert(-1, val2)
print(val2)

print(list1)
list1.insert(-2, 50)
print(list1)

list2 = [3, 5, 6]

list1.insert(-1, list2)

print(list1)

###############################
# Remove : Remove data from list by its value

list1 = [4, 6, 8, 23, [4, 6, 7]]

output = list1.remove(8)
print(list1)
print(output)

list1.remove([4, 6, 7])

print(list1)

# pop : remove data from list on given , it also return same value .

lista = [23, 7, 8, 34, 45]

#use pop without index : it remove value from last index
output = lista.pop()

print("pop output:", output)

print(lista)

# user pop with index

output2 = lista.pop(0)
print(output2)
print(lista)

# Program : put all data of list1 in list2
#input :
list1 = [3, 5, 7, 89, 67, 3, 5, 'abc', 'xyz']
list2 = []
#output :
#list2 = [67, 89, 7, 5, 3]
#list1 = []

list_len = len(list1)
print(list_len)
for i in range(list_len):
    data = list1.pop()
    list2.append(data)

print("list1:", list1)
print("list2:", list2)


########################## Put data using remove and append #################
list3 = list2.copy()
for val in list3:
    #print(val)
    list1.append(val)
    list2.remove(val)

print("list1:", list1)
print("list2:", list2)


newlist = [4, 6, 8, 4, 5, 'a', 5]

output= newlist.pop()
print(output)
#newlist.remove(5)

print(newlist)

#newlist.remove(5)

print(newlist)

# Delete list : It removes complete list from the memory.

del newlist

print(newlist)


# Reverse : reverse list, reverse all the list data from negative index

lista = [3, 5, 7, 8, 10]
listb = [3, 5, 7, 8, 10]

#It modifies the list in place and reverse the data
output = lista.reverse()
print(output)
print(lista)

# It does not modify the list , it will return reverse value as output
output = listb[::-1]
print(output)
print(listb)

list2 = [5, 7, 8, 23, 67, 'a', 'b', 'c']
print(list2[2:4])
print(list2[2:])
print(list2[:4])

# One jump from negative index
print(list2[::-1])

# Three jump from negative index
print(list2[::-3])

# Four jump from negative index
print(list2[::-4])

# Three jump from positive index
print(list2[::3])

listp = [3, 5, 7, 8, 9, 3, 5, 1]

# Get how many time 3 is repeated in the list
print(listp.count(3))

# Get max value from list
print(max(listp))

# Get Min value from the list
print(min(listp))

# sort list
print(listp.sort())
print(listp)

"""
'''
# Program1: find particular element is available in list of not.
elem = 23
list1 = [3, 5, 6, 7, 8, 21]

if elem in list1:
    print("True")
else:
    print("False")

# Program to get sum of all elements in the list

list11 = [4, 6, 8, 9, 23]

listsum = 0

for num in list11:
    listsum = listsum + num

print(listsum)


print(sum(list11))


# Program 2:
lista = [2, 4, 6, 9, 'a', 'b', 4, 6, 8, 11, 12]
listb = [4, 5, 8, 10, 'c', 'd', 'e', 234, 456, 'p', 'q', 'r', 'x', 'y', 'z']

#listc  = [[2, 4], [4, 5], [6, 8], [9, 10], ['a', 'c'], ['b', 'd']]
#listd = [6, 9, 14]

rang_len = 0

lista_len = len(lista)
listb_len = len(listb)

if lista_len > listb_len:
    rang_len = lista_len
else:
    rang_len = listb_len

listc = []

for i in range(rang_len):
    if i < lista_len and i < listb_len:
        print(lista[i], listb[i])
        var_list = [lista[i], listb[i]]
        listc.append(var_list)
    elif i < listb_len:
        listc.append(listb[i])
    elif i < lista_len:
        listc.append(lista[i])
    else:
        continue

print(listc)
'''
###################### Get sum of individual Element ###################
#Program : Add two list data and append in third list
'''
listp = [2, 5, 7, 9]
listq = [4, 7, 9, 10]

#listr = [6, 12, 16, 19]

listr = []
for i in range(len(listp)):
    sum_value = listp[i] + listq[i]
    listr.append(sum_value)

print(listr)

'''
'''
# Program : Add both list integer and string value and store list3.

listp = [2, 5, 7, 9, 'abc', 'hello',  124]
listq = [4, 7, 9, 10, 'pqr', 1234, 'data' ]

#listr = [6, 12, 16, 19]

listr = []
for i in range(len(listp)):
    if type(listp[i]) == type(listq[i]):
        sum_value = listp[i] + listq[i]
        listr.append(sum_value)
    else:
        continue

print(listr)
'''
#######################################################
# Program : Get factorial of each value in the list.
'''
list11 = [3, 6, 9, 12, 8]
fact_list = []

#num = 5
# 5*4*3*2*1
for val in list11:
    fact = 1
    for i in range(val, 1, -1):
        fact = fact*i

    fact_list.append(fact)

print(fact_list)



################################### Deep Copy and Shallow Copy #####################

# Shallow Copy : In shallow we pass reference of one list to another list, does
# Not copy data.

list1 = [2, 4, 6, 8]

list2 = list1

list2.append(34)

print("list1", list1)
print("list2", list2)


# Deep Copy : Actual data copy from list1 to list2.

listp = [4, 5, 7, 8]
listq = listp.copy()
listq.append(12)

print("listp", listp)
print("listq", listq)


############### list comprehension ###################


list1 = [2, 5, 7, 9, 10]

for elem in list1:
    print(elem**2)

# Example : list comprehension
output = [x+2 for x in list1]

print(output)

# Get square of all even number :
output2 = [x**2 for x in list1 if x%2 != 0]

print(output2)

listqq = []
for x in list2:
    if x%2 == 0:
        listqq.append(x**2)
    else:
        continue




output3 = [x*y*z for x in range(1, 3) for y in range(1, 3) for z in range(1, 3)]

print(output3)

num = 21

result = num if num%2 == 0 else "odd"

print(result)

if num%2 ==0 :
    print(num)
else:
    print("odd")



######################################################

input = 'abcd'
#output = 'aaaabbbbccccdddd'
output = ""
for char in input:
    output = output + char*4

print(output)

input2 = 'abcd'
output2 = ""
for i in range(len(input2)):
    output2 = output2 + input[i]*4
print(output2)



#####################################################
# 16 Nov 2020

#Program1 :

list1 = [4, 3, 8, 23, 34]
list2 = []

for i in list1:
    list2.append(i**2)

print(list2)

# Program2 : get combination of two number which sum is 10 in given list.

list1 = [3, 6, 8, 23, 2, 5, 4, 6, 7]
# output = [3, 7], [8, 2] [4, 6]
# output2 = ()

#1. Iterate through each number : for i in list1
#2. second loop to sum with remaining numbers.

for i in list1:
    #print(i)
    for j in list1:
        #print(i, j)
        if i == j:
            continue
        else:
            if i + j == 10:
                print(i, j)

print("*"*20)
for p in range(len(list1)):
    for q in range(len(list1)):
        if p == q:
            continue
        else:
            if list1[p] + list1[q] == 10:
                print(list1[p], list1[q])
            else:
                continue



# Program3 : Get combination all three number which sum is 15.
        #  i  j  k
# list1 = [3, 6, 8, 23, 2, 5, 4, 6, 7]
         # 0  1  2  3   4  5  6  7  8


for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        for k in range(j+1, len(list1)):
            #print("i :{}, j: {}, k: {}".format(list1[i], list1[j], list1[k]))
            if list1[i]+list1[j]+list1[k] == 15:
                print("[", list1[i], list1[j], list1[k], "]")
            else:
                continue
        #print("*"*30)
        


# Program4 :  Get greater number in the list:
                                #max
list1 = [45, 67, 23, 45, 20, 31, 87]

#print(max(list1))

max_value = list1[0]

for value in list1:
    if value > max_value:
        max_value = value
    else:
        continue
print(max_value)
'''

# Program5 : Get greater sum in list of list.

list1 = [[4, 5, 6], [6, 7, 8, 9], [3, 5, 2], [4, 7, 9, 2]]

max_value = 0
result_list = []
for listdata in list1:
    #print(i)
    #list1_sum = 0
    # for data in listdata:
    #     list1_sum = list1_sum + data

    list_sum = sum(listdata)
    if list_sum > max_value:
        max_value = list_sum
        result_list = listdata

print(max_value)
print(result_list)



############################################################

list1 = ['AHello', 'Good', 'Morning', 'Happy', 'Diwali']
list2 = []

for str1 in list1:
    #print(str1)

    for char in str1:
         print(char,":", ord(char))

    list2.append(str1.swapcase())

print(list2)



# Ascii value for capital and small alphabates
for i in range(1, 123):
    print(i, ":", chr(i))


# ord() : It return ascii value of any char
# chr() : It return char using ascii value

# A-Z : 65 : 90
# a-z : 97 : 122
# 0-9 : 48 : 57