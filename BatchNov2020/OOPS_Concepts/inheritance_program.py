"""
Single Inheritance : Inherit the property of one class to another class
Class1 ------> Class2


"""

# parent class, super class
class xyz:
    def __init__(self, religion, surname):
        self.religion = religion
        self.surname = surname

    def display_details(self):
        print(f"Religion : {self.religion}, Surname : {self.surname}")

    def xyz_method1(self):
        print("I am in xyz method1")

    def xyz_method2(self):
        print("I am in xyz method 2")

# child class , sub class
class ABC(xyz):
    def __init__(self, name, job, religion, surname):
        super().__init__(religion, surname)
        self.name = name
        self.job = job

    def ABC_method1(self):
        print("We are in ABC Method1")

    def ABC_method2(self):
        print("We are in ABC Method2")

    def child_details(self):
        print(f"Name : {self.name}, Surname {self.surname}, Religion : {self.religion}, Job: {self.job}")


# father ki class
obj = xyz('rahul', 20)
obj.xyz_method2()
obj.xyz_method1()


# child ki class
abc_obj = ABC('Rahul', 'Software Engineer', 'Hindu', 'Sharma')
abc_obj.xyz_method2()
abc_obj.xyz_method1()
abc_obj.ABC_method1()
abc_obj.display_details()
abc_obj.child_details()
