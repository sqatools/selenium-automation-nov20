"""
Multiple Inheritance

Class A -----> Class c
Class B -----> Class C

"""
"""
class A:
    def methodA(self):
        print("We are in methodA")


class B:
    def methodB(self):
        print("We are in method B")


class C(A, B):
    def methodC(self):
        print("We are in method C")


objc = C()

objc.methodA()
objc.methodB()
objc.methodC()

print("#"*50)

objb = B()
objb.methodB()
#objb.methodA()

print("#"*50)

objb = A()
objb.methodA()
"""

class A:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def methodA(self):
        print("We are in methodA")

    def display_A(self):
        print(f"Name : {self.name},  surname : {self.surname}")


class B:
    def __init__(self, job, address):
        self.job = job
        self.address = address

    def methodB(self):
        print("We are in method B")

    def display_B(self):
        print(f"Job : {self.job},  Address : {self.address}")

# MRO : Method Resolution Order
class C(A, B):
    def __init__(self, salary, name, surname, job, address):
        super().__init__(name, surname)
        self.objb = B(job, address)
        self.salary = salary

    def methodC(self):
        print("We are in method C")

    def display_C(self):
        print(f"Name : {self.name}, Surname : {self.surname}")
        #print(f"Job : {self.objb.job}, Address : {self.objb.address}")
        print(f"Salary : {self.salary}")


objc = C(8000, 'Akshay', 'Sharma', "QA", "Mumbai")

objc.display_C()