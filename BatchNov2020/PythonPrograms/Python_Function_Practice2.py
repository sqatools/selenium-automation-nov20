"""

def outer_function():
    name = 'Chetna'

    def inner_function1():
        nonlocal name
        name = 'Sagar'
        print("*"*50, "\n")
        print("inner_function1")
        print("My name is :", name)

    def inner_function2():
        print("*"*50, "\n")
        print("inner_function2")
        print("My name is :", name)

    def inner_function3():
        print("*"*50, "\n")
        print("inner_function2")
        print("My name is :", name)


    inner_function1()
    inner_function2()
    inner_function3()

#outer_function()

########################################################

def odd_or_even(num):
    if num%2 == 0:
        print("Hello")
        return True
    else:
        return False

n = 30
output = odd_or_even(n)

print(output)


####################### Calc ##################
def addition(a, b):
    return a+b

def multiplication(a, b):
    return a*b

def divide(a, b):
    return a//b

def substraction(a, b):
    return a-b


while True:
    print("1. Addition \n"
          "2. Multiplication \n"
          "3. Divide \n"
          "4. Substraction \n")

    user_input = int(input("Please select your operation"))
    if user_input == 1:
        print("Please provide two numbers to add")
        num1 = int(input("Please provide num1 :"))
        num2 = int(input("Please provide num2 :"))
        output = addition(num1, num2)
        print(f"Addition of two number is : {output}")
    elif user_input == 2:
        print("Please provide two numbers to multiply")
        num1 = int(input("Please provide num1 :"))
        num2 = int(input("Please provide num2 :"))
        mul_out = multiplication(num1, num2)
        print(f"Multiplication of two number is : {mul_out}")
    elif user_input == 3:
        print("Please provide two numbers to Divide")
        num1 = int(input("Please provide num1 :"))
        num2 = int(input("Please provide num2 :"))
        div_out = divide(num1, num2)
        print(f"Division of two numbers is : {div_out}")
    elif user_input == 3:
        print("Please provide two numbers to Substraction")
        num1 = int(input("Please provide num1 :"))
        num2 = int(input("Please provide num2 :"))
        sub_out = substraction(num1, num2)
        print(f"Substraction of two numbers is : {sub_out}")


#_________________________________________________________________________
"""

# Program 1 : print square of each number from 1 to n.

def get_square(n):
    sqr_list = []
    for i in range(1, n):

        sqr_list.append(i**2)

    return sqr_list

#result= get_square(10)
#print(result)


# Program 2 : get factorial of given number n.   n=5 , 120

# 5 : 5*4*3*2*1

def factorial(n):
    fact =1

    for i in range(1, n+1):
        fact =fact*i

    return fact

#print(factorial(6))

# Program 3 : print sum of list number.   *arg

def get_sum(*args):
    sum = 0
    for num in args:
        sum = sum + num

    return sum

#print(get_sum(3, 4))




# 4. find out given number is divisible by 3 if yes return True else False

# 5. Find out list of number which are divide by 5 and 7 from 1 to n.

# 6. find out particular key is available in dict or not, c Tru, d False

dict1 = {'a':34, 'b':45, 'c': 3}





def divide_num(n1):
    #n1 = int(input("Please enter your limit :"))
    list1 = []
    for i in range(1, n1+1):
        if i%5 == 0 and i%7 == 0:
            list1.append(i)
        else:
            continue

    return list1



#result = divide_num(50)
#print(result)



def divide_num2(*args):
    list1 = []
    for i in args:
        if i%5 == 0 or i%7 == 0:
            list1.append(i)
        else:
            continue

    return list1

#print(divide_num2(5, 35, 50, 60, 67, 77))




############

def check_key(key):
    dict1 = {'a': 34, 'b': 45, 'c': 3, 4: 16, 5:20}
    if key in dict1:
        return True
    else:
        return False


#print(check_key(4))

def function(key,value):
    dict1={'a':34,'b':45,'c':3 ,4:16}
    if key in dict1 and dict1[key] == value:
        return True
    else:
        return False


#print(function(4))

def keyfunction(key,value):
    dict1={'a':34,'b':45,'c':3 ,4:16}

    if key in dict1 and dict1[key] == value:
        return True
    else:
        return False


def keyfunction(key):
    dict1 = {'a': 34, 'b': 45, 'c': 3, 4: 16, 5:20}

    if key in dict1 and dict1[key] == key**2 :
        return True
    else:
        return False

print(keyfunction(5))


def get_average(*args):
    sum = 0
    for i in args:
        sum = sum + i
    average = sum\
              //len(args)
    return average

print(get_average(46, 7, 8, 9, 19, 3))

def print_fabonaci(n):
    a = 0
    b = 1
    list1 = []
    for i in range(n):
         a, b = a+b , a
         #print(a, end=" ")
         list1.append(a)

    return list1

print(print_fabonaci(10))

# Program : write a program to check given value of key is square of itself.


