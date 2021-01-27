"""
Multi Level Inheritance

class 1 ----> class 2 -----> class 3

"""
'''
# Grand father
class A:
    def class_methodA(self):
        print("We are in method A")

# father
class B(A):
    def class_methodB(self):
        print("We are in Method B")

# child
class C(B):
    def class_methodC(self):
        print("We are in Method C")

# grand father class
obja = A()
obja.class_methodA()
print("#"*20)

#Father class
objb = B()
objb.class_methodA()
objb.class_methodB()
print("#"*20)

# # Child class
#
objc = C()
objc.class_methodA()
objc.class_methodB()
objc.class_methodC()
'''

##############################################################

# Grand father
class A:
    def __init__(self, wealth):
        self.wealth = wealth

    def class_methodA(self):
        print("We are in method A")

    def display_wealth(self):
        print(f"Wealth : {self.wealth}")

# father
class B(A):
    def __init__(self, wealth, religion, surname):
        super().__init__(wealth)
        self.religion = religion
        self.surname = surname

    def class_methodB(self):
        print("We are in Method B")

    def father_data(self):
        print(f"wealth : {self.wealth}, religion :{self.religion}, surname : {self.surname}")

# child
class C(B):
    def __init__(self, wealth, religion, surname, name, job):
        super().__init__(wealth, religion, surname)
        self.name = name
        self.job = job

    def class_methodC(self):
        print("We are in Method C")

    def child_details(self):
        print(f"Name : {self. name}, Job : {self.job}")
        print(f"wealth : {self.wealth}, religion :{self.religion}, surname : {self.surname}")


objc = C('5 cr', 'Hindu', 'Gupta', 'Harry', 'Consultant')

objc.child_details()
print("#"*50)
objc.father_data()
print("#"*50)
objc.display_wealth()