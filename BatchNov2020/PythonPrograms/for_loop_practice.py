"""
for i in [1, 2, 3, 4, 5]
    print(i)

range(initial, endvalue , different)

"""

"""

for var in [1, 2, 3, 4, 5]:
    #print(var)
    print(var, end= " ")

print("\n")
# print value from 0 to 10 it start from to 0-9
for var in range(10):
    #print(var)
    print(var, end= " ")

# print value from 3 to 10 , it starts from 3 to 9
print("\n")
for var in range(3, 10):
    #print(var)
    print(var, end=" ")

print("\n")

# print value from 3 - 10 with different of two

for var in range(3, 10, 2):
    #print(var)
    print(var, end=" ")

print("\n")


for chr in 'Hello':
    print(chr)

print(range(10))


print(1**2)
print(2**2)
print(3**2)
print(4**2)
print(5**2)
print(6**2)

for num in range(1, 25):
    if num%2 == 0:
        print(num**3)
"""

# print table of given number
num = int(input("Please Enter Number:"))
for i in range(1, 11):
    print(i, "*", num, "=", i*num)


# Get all the number which are divible by user input from 1- 100
userinput = int(input("PLease enter your number :"))

for i in range(1, 100):
    if i%userinput == 0:
        print(i)


