"""

# Program1
Number = 21

# If Else condition
if Number%2 == 0:
    print("Its Even Number")
else:
    print("Odd Number")


# Nested If else Condition
 
  if <logical>:  
       statement
          if  logic2:
              statement
          else:
              statement
  else:
     statement


# Program2
Number = 22

if Number%2 == 0:

    print("Its Even Number")
    if Number%5 == 0:
        print("Great, Its divisible by 5")
    else:
        print("Choose another number, cant divide by 5")
else:
    print("Its Odd Number")



# Program 3 : Nested if else conditions

# Take user input
user_input = input("Please Enter your input :")

# condition1
if user_input == 'male':
    print("We can ask his age")
    user_age = input("Please Enter your age :")

    # condition2
    if int(user_age) > 16:
        print("He is in college")

        # condition3
        if int(user_age) > 16 and int(user_age) < 20:
            print("He is doing Batchlor Degree")
        else:
            print("He is doing Master Degree")

    else:
        print("He is in school")
else:
    print("We can't ask her Age")

"""
# Program4

'''
if cond1

elif cond2

elif cond3

else:
     print statement

'''

# Get greater number among these three


# and  : all conditions should be True
# or   : Any one should be True

"""
### and ###

True  True = True
True  False = False
False True  = False
False False = False

#### OR ######

False True = True
False False = False
True False = True
True True  = True

"""
a = 35
b = 30
c = 40

if  a > b or  a > c:
    print("A has greater value")
elif b > a or b > c:
    print("B has greater value")
elif c > a or c > b:
    print("C has greater value")
else:
    print("Please provide valid input")

###################
"""
>=  : Value either greater or equal to that specific number
<=  : value ether less or equal to that specific number
==  : Equal operator, means to verify two variable have same value
=   : Assignment operator , assign one value to another variable.
 """
####################
# 1. Get student grade as per the marks.
# if marks greater than 50 thn grade C and less than 60
# if marks greater than 60 and less than 70 Grade B
# if marks greater than 70 and less than 80 grade A


marks = int(input("Please enter your marks:"))
stu_cat = input("Please confirm you are girl or boy :")

if marks > 100:
    print("Please enter valid number, marks can not be more than 100")
else:
    if stu_cat == 'boy':
        if marks >= 50 and marks <= 60:
            print("He got C grade in Exam")

        elif marks > 60 and marks <= 70:
            print("He got B grade in exam")

        elif marks > 70 and marks <= 80:
            print("He got A grade in exam")

        elif marks > 80 and marks <= 90 or marks > 90 :
            print("He got A++ grade in exam")
        else:
            print("He failed in Exam")

    elif stu_cat == 'girl':

        if marks >= 40 and marks <= 60:
            print("She got C grade in Exam")

        elif marks > 60 and marks <= 70:
            print("She got B grade in exam")

        elif marks > 70 and marks <= 80:
            print("She got A grade in exam")

        elif marks > 80 and marks <= 90 or marks > 90:
            print("She got A++ grade in exam")
        else:
            print("She failed in Exam")
    else:
        print("Please enter valid Input Either it can be girl or Boy")





