"""
class : class cam be defined as collection of objects or blue print of object, which has some
specific attribute and methods.

object : object is entity which has some state and behviour
when we define a class , need to create an object to allocate the memory.

list1 = [2, 3.0, 'str']
"""
"""
class ABC:

    # Method, object method
    def display(self):
        print("Hello We are in class")

    def addition(self):
        a = 30
        b = 40
        print(a+b)


# create object of class ABC
obj = ABC()
obj1 = ABC()
obj2 = ABC()

# call class method
obj.display()
obj1.display()
obj2.display()
obj2.addition()

"""
# constructor in class


class xyz:
    # class variable
    age = 40

    # constructor
    def __init__(self, address, rollno):
        # Instance variable
        self.name = 'SQATools'
        self.add = address
        self.roll = rollno
        #self.show_data(8000)

    # method, object method, instance method.
    def show_data(self, salary):
        print(f"Name :{self.name}, Age ; {xyz.age}, Salary : {salary}")
        print(f"Address : {self.add}, Roll No: {self.roll}")

    def greeting(self):
        print("Hello, Good Morning ")


obj1  = xyz('Pune', 45667)

obj1.show_data(9000)
#obj1.greeting()

#xyz('Mumbai', 45445567).greeting()




















