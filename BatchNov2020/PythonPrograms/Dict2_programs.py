# Program1 : addition of two dict in single dict

dict1 = {'p': 300, 'q': 500, 'r': 200, 's':250}
dict2 = {'p': 400, 'q': 600, 'r': 500,  't': 100}

output = {}

# sum of all matching keys in both dict
#output1 = {'p' : 700, 'q':1100, 'r':700}

# sum of all keys in dict1 and dict2
#output2 = {'p' : 700, 'q':1100, 'r':700, 's': 250, 't': 100}

# sum of all non matching keys
#output3 = {'s':250, 't':100}

# output1 = {}
# for k, v in dict1.items():
#     print(k, v)
#     if k in dict2:
#         output1[k] = dict1[k] + dict2[k]
#
# print(output1)

################################
"""
output2 ={}

for k, v in dict1.items():
    if k in dict2:
        output2[k] = dict1[k] + dict2[k]
    else:
        output2[k] = dict1[k]

for k, v in dict2.items():
    if k in output2:
        continue
    else:
        output2[k] = dict2[k]

print(output2)


#########################

output2 = {}

for k, v in dict1.items():
    print(k, v)
    for k1, v1 in dict2.items():
        print(k1, v1)
        if k == k1:
            output2[k] = dict1[k] + dict2[k]
        elif k not in dict2:
            output2[k] = dict1[k]
        elif k1 not in dict1:
            output2[k1] = dict2[k1]


print("Output2 :", output2)

output3 = {}

for k, v in dict1.items():
    for k1, v1 in dict2.items():
        if k not in dict2:
            output3[k] = dict1[k]
        elif k1 not in dict1:
            output3[k1] = dict2[k1]
        else:
            continue

print("Output3 :", output3)

# Program :

dict1 = {'a': 2, 'b':4, 'c': 8, 'd': 16}

#outputdict = {'a': 1, 'b':2, 'c':4, 'd': 8}

#output2 = {'a': 4, 'b': 16,  'c': 64, 'd': 256}

outputdict = {}
output2 = {}

for k, v in dict1.items():
    outputdict[k] = v//2
print(outputdict)


for k, v in dict1.items():
    output2[k] = v**2
print(output2)


# Program : separate all odd and even value in two diff dict.
input_dict = {'a' : 4, 'b' : 3, 'c': 21, 'd': 12, 'e': 5}
#evendict = {'a ' : 4, 'd' : 12}
#odddict = {'b' : 3, 'c': 21, 'e': 5}
evendict = {}
odddict = {}

dict1={'a':4,'b':3,'c':21,'d':12,'e':5}
for k,v in dict1.items():
   if v%2==0:
       evendict[k] = v
   else:
      odddict[k] =v
print(evendict)
print(odddict)



# Program : Convert all string value from lower to upper and upper to lower
input_dict1 = {'x' : 'Hello', 'y' : 'Good', 'z': 'Morning'}
outputdict1 = {'x' : 'hELLO', 'y' : 'gOOD', 'z' : 'mORNING'}



# Program : Get sum of each list and get max value from output list.
input_dict = {'a': [2, 5, 8], 'b': [5, 7, 9], 'c': [23, 7, 9, 34]}
#output1  = {'a' : 15, 'b' : 21, 'c' : 73}
#max_value = 73

output1 = {}
max_value = 0
for k, v in input_dict.items():
    print(k ,":", v, ":", sum(v))

    output1[k] = sum(v)

    if sum(v) > max_value:
        max_value = sum(v)
                        

print(output1)
print(max_value)
                        

for i in range(1, 11):
    fact=1
    for j in range(1, i+1):
        fact= fact*j

    print(i,":", fact)

"""

dict1 = {'a' :10, 'b': 20, 'c': 40, 'd':50, 'e':70}

dict2 = {'a' : 10, 'b': 30, 'p':30, 'c':40, 'd': 60}
output_dict = {}

for k, v in dict1.items():
    for k1, v1 in dict2.items():
        if (k in dict2 and dict1[k] == dict2[k]):
            continue
        elif (k in dict2 and dict1[k] > dict2[k]):
            output_dict[k] = dict1[k]
        elif (k in dict2 and dict1[k] < dict2[k]):
            output_dict[k] = dict2[k]
        elif k not in dict2:
            output_dict[k] = dict1[k]
        elif k1 not in dict1:
            print(k1)
            output_dict[k1] = dict2[k1]

print(output_dict)


input1= {1:['a', 'b', 'c'], 2:['e', 'f', 'g']}
list1=[]
for key,value in input1.items():
    list1.append(value)
for first in list1[0]:
    for second in list1[1]:
        print(first+second)
