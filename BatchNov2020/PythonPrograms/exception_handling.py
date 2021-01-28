# a = 10
# print(a/0)
'''
try:
    a = 10
    print(a / 0)

except:
    print("We can not divide any number by 0")
'''

'''
try:
    a = 10
    print(a / 0)

except Exception as e:
    print("We can not divide any number by 0")
    print(e)

try:
    a = 'b' + 23
    print(a)
except Exception as e:
    print(e)
'''

########################################
#Exception condition
'''
try:
    a = 20
    b = 30
    c = a + b
    print(c)

except Exception as e:
    print(e)
    print("We can not add numbers with string")
else:
    print("Number are added successfully")

#############################################
'''

# Finally : Finally code execute by default , even there is exception in code or not.
'''
try :
    a = 20
    b = 5
    c = a//b
    print(c)
except:
    print("There is error in division of number")
else:
    print("Number division successfull")
finally:
    p = 30
    q = 40
    print(p*q)

'''
'''
########################################################
#Raise Exception and verify

name = input("Please enter your name:")
age = input("Please enter you age :")

if name != 'john':
    #raise("input name is not expected")
    #raise ValueError("input name is not expected")
    #raise ArithmeticError("input name is not expected")
    raise IsADirectoryError
else:
    print(f"Name : {name}, Age : {age}")

'''

####################################################
# Execute all code even there is error in code.

list1 = [23, 45, 56, 34, 'q', 20]

for value in list1:
    try:
        if value%2 == 0:
            print(value, end= ' ')
        else:
            continue
    except Exception as e:
       pass




