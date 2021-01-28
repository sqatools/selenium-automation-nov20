# Immutable Datatype : Can not modify the the data value


str1 = """
Hello , Everyone
"""
       #0123456789010
str2 = "Good Morning"
       #      -3-2-1 

str3 = 'Its training session'

#print(str1)
#print(str2)
#print(str3)

# It will print 0 index value in string
print(str2[0])

# It will print value from 1-to-4 and skip 5th index
print(str2[1:5])

# It reverse substring from 0-3 
print(str2[3::-1])

# It reverse substring from 0-5
print(str2[5::-1])

# It will print last value of string 10 times
print(str2[-1]*10)

# It will reverse complete string
print(str2[::-1])

output = str2[::-1]
print("output :", type(output), output)





