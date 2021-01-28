"""
def function_name():
    logic or code

function_name()
"""
"""
def function1():
    print("Hello World")


#function1()
# function1()
# function1()

###########################################################
# Function Parameter
def function2(name):
    print("Good Morning, ", name)

# 1. Pass by value
function2("SQA Tool")

# 2. Pass by reference
name2 = "Sagar"
function2(name2)

function2(name='Saturday')

#######################################################
# Function with Multiple Parameter

def function3(name, age):
    print("My name is,", name)
    print("My age is, ", age)


function3('Sagar', 25)   # Pass by value

function3(25, 'Sagar')  # Position of parameter will be noticed

function3(age=25, name='Rahul')  #  if param name is given then position does not matter.

function3('John', age=25) # if only specific param is given then position matters.

function3('Hary')  # It will through error to show positional argument is missing

# TypeError: function3() missing 1 required positional argument: 'age'
"""
###########################################################
# Function with multiple parameters and default value

def function4(city, student_id=3456, rollno=4567):
    print("My roll no is:", rollno)
    print("Student ID is:", student_id)
    print("I live in this City :", city)


#function4(4567, 'stud456', 'Pune')
#function4('Hyderbad', rollno=45678,  student_id='3456')


################################################
# *args in function , through which we can provide list of argument

def function5(*args):
    for var in args:
        print(var)

    print("Name :", args[0])
    print("Age :", args[1])
    print("City :", args[2])
    print("Rollno :", args[3])
    print("StudentID :", args[4])


#function5('Rahul', 25, 'Mumbai', 'roll234', 'stu123')

# *args with other parameter
def function6(school_name, *args):

    for var in args:
        print(var)

    print("School Name:", school_name)

#function6('John', 45, 'stud234', 'Junior Convent')


def function7(*args, school_name):

    for var in args:
        print(var)

    print("School Name:", school_name)

#function7('John', 45, 'stud234', 'Junior Convent', school_name='Senior School')

#######################################################################
#**kwagrs   : pass parameter data with key value pair or dictionary format

def function8(ID,**kwargs):

    print("Person ID is :", ID)
    for k, v in kwargs.items():
        print(k, " : ", v)

#function8(3456, name='John', age='25', college='IIT', city='Bangalore')
#function8(ID=3456, name='John', age='25', college='IIT', city='Bangalore')
#function8(name='John', age='25', college='IIT', city='Bangalore', ID=3456)
#function8(name='John', age='25',ID=3456, college='IIT', city='Bangalore')


def function9(ID, *args, **kwargs):

    print("Person ID is :", ID)
    for k, v in kwargs.items():
        print(k, " : ", v)
    print("#"*20)

    for var in args:
        print("var :", var)

#function9(5678, 'Hello', 'Good' , 'Morning', name=['John', 'Ambika', 'Sagar'], age='25', college='IIT', city='Bangalore')

################################# Variable Types in Functions ###################

# local variable : variable that we define inside is known as local variable
# Global Variable : variable that define outside of function is known global variable
# Non Local variable : variable that is not a local and not a global is know as non local variable.


x = 30  # global variable
z = 40

def chetna():
    print("We are in addition")
    a = 20   # local variable
    b = 30   # local variable
    c = a + b
    print(c)
    print(a*b)
    print(a//b)
    print("x:", x)
    print("z:", z)
    print("p:", p)

def function3():
    print("We are in function3")
    global p
    p = 60
    x = 40  # local variable with same name as global variable
    global z
    z = 50
    print("x:", x)
    print("z:", z)
    y = x//10
    print(y)
    # print(a)   : we can't user other function local variable

def test_fun():
    print("We are in test_function")
    print("x:", x)
    print("z:", z)
    print("p :", p)


#function3()
#chetna()
#test_fun()


############### Non local variable #######

m = 30  # Global

def outer1():
    x1 = 40  # Non local variable
    z = 60  # non local variable

    def inner_function():
        print("We are in inner1")
        nonlocal x1
        m = 60
        x1 = 'local_data'
        y = 60
        print("x :", x1)
        print("m :", m)
        print("y :", y)
        print("z :", z)

    def inner_function2():
        nonlocal x1
        x1 = "inner_fucn2"
        print("We are in inner2")
        print("x1 :", x1)
        print("m :", m)
        print("z :", z)

    def inner_function3():
        x1 = "inner_fucn3"
        print("We are in inner3")
        print("x1 :", x1)
        print("m :", m)
        print("z :", z)

    inner_function3()
    inner_function()
    inner_function2()




def outer2():
    print("We are in operation")
    print(x1)

#outer1()
#outer2()



################################## Return Statement #####################
def learning(name):
    var = "We are learning:"+name
    #print("We are learning:",name)
    return var

#learning("Python")
#learning("Java")

var2 = learning("Python")
print(var2)

for char in var2:
    print(char)

def addition(a, b):
    return a+b


output = addition(30, 20)

print(output)
output2 = output//10
print(output2)

def multiplication(c):
    number = addition(30, 50)
    multi = number*c
    return multi


multi_out = multiplication(3)
print(multi_out)







