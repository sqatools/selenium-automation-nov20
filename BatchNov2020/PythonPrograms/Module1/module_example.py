#import operation.py


# calling specific data from module
from PythonPrograms.test_package.operation123 import substraction, a

# rename module called its data by name
import PythonPrograms.test_package.operation123 as pkg
from PythonPrograms.FilePrograms import get_employee_details

print(a)

print(substraction(20, 10))

print(pkg.multiplication(45, 23))

print(pkg.addition())


get_employee_details(8)