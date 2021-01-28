"""
# Continue : It uses for continue the continue with executing other part of program
# Break  : It uses for breaking the for loop iteration

for i in range(20):
    if i > 10:
        print("We are in continue condition", i)
        continue

    if i == 9:
        print("We are breaking the loop")
        break

    if i < 15:
        print(i**2)

#________________________________________________________________
# Program : Find out factorial of any number

#5 = 5*4*3*2*1 = 120
# 1. Get a number to find out factorial
# 2. use loop to iterate on the given number  : for num in range(6, 1, -1)
# 3. Multiple each number to each and store in a variable


num = int(input("PLease enter number for factorial:"))

fact = 1

for i in range(num, 0, -1):
    print(i, fact)
    fact = fact*i

print("Factorial :", fact)

#___________________________________________________

# Program2 : Find out fabonaci series till given number 10
#  a, b, a+b
#  1, 2, 3, 5, 8, 13, 21, .....
# 1. We have to iterate loop till given number 10,: for i in range(10)
# a, b = 0, 1, will take two variable which initial by 0 and 1
# a, b = b, a+b'
'''
a = 1, b = 2
a , b = 2, 3
a = 2, b = 3
'''
a = 0
b = 1
for i in range(10):
    a, b = b, a+b
    print(b, end=" ")

"""
# __________________________________________________
# While loop

# while (condition):
#    logi
#    increament

# Print table of any number using while loop
n=1
while n <= 10:
    print(n, "*", 2, ":", n*2)
    n = n+1


# Run Infinite while loop

while True:
    print("Hello")


