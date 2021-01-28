"""
Hiding the data from outside access of the class is know as Ecapsulation and data hiding
"""

class A:
    _name = 'Rahul'
    age = 30
    __Address = 'Bangalor'

    def __init__(self, job, salary, comp):
        self._job = job
        self.__salary = salary
        self.comp = comp

    def display_instance_var(self):
        print(self._job)
        print(self.comp)
        print(self.__salary)

    def display_class_var(self):
        print(A._name)
        print(A.age)
        print(A.__Address)


obj = A("QA", 50000, 'facebook')

obj.display_class_var()
print("#"*50)
obj.display_instance_var()

# print(obj.age)
# print(obj.comp)
#
print(obj._name)

#print(obj.__Address)

print(dir(obj))
print(obj._A__Address)
print(obj._A__salary)


