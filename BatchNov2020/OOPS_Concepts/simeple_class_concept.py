class pqr:
    def __init__(self, name, surname):
        #instance variable
        self.name = name
        self.surname = surname

    # instance method/obj method
    def print_greeting(self):
        print("Good Morning")

    def show_data(self):
        print(self.name)
        print(self.surname)

obj = pqr('John', 'Jany')
print(id(obj))

obj.print_greeting()

pqr.print_greeting(obj)

