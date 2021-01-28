"""
# variable, int, str, list, dict, tuple, set
a = '1'
print(type(a))

a = 20 # Assignment operator
b = 30
# operator : +, - , *, /, //, %

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# data type
# logic we write

print("Hello word")


# Program get odd or even number
# == : equal to operator to compare to values

print(10%3)

n = int(input("Please enter your number :"))

if n%2 == 0:
    print("It's Even Number")
else:
    print("Odd Number")

# Program : Distribute student grade as per marks received.

# > : greater, < : less than, >= greater than equal to , <=   less than equal to

#
marks = int(input("Please enter your marks:"))

if marks > 40 and marks <= 50:
    print("He got C grade")

elif marks > 50 and marks <= 60:
    print("He got B Grade")

elif marks > 60:
    print("He got A grade")
else:
    print("He Failed in Exam")

"""
#################### print()
"""
for loop condition 
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(i)


for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(i)

print("#"*20)
# range(initial, endvalue, different)

for i in range(2, 10+1, 2):
    print(i)

print("#"*30)
# Program : Get all the number from 1 to 100 , which are divide by 3 and 5.

for i in range(1, 100+1):
    if i%3 == 0 and i%5 == 0:
        print(i)

print("_"*20)
# Program : Gell square of all even number from 1 to 20

for i in range(1, 20):
    print(i, ":", i**2)
"""
# Nested for loop considtion
'''
for i in range(3):
   for j in range(2)
      print(i, ":", j)
'''

for i in "pqr":            #   i=h   and j = h, j=i
    for j in "hixyz":
        print("i:", i, ", j:", j)

    print("-"*20)


""""
*
**
***
****
*****
"""

for i in range(6):
    for j in range(i):
        print(" * ", end="")
    print("\n")

# i = 0, j=0 to 0
# i = 1, j= 0, to 1
# i = 2, j= 0 to 2= 0, 1
# i = 3, j = 0 to 3 = 0, 1, 2