# String is immutable
# String Follows Sequence or indexing
"""
str1 = "Hello"

#print(dir(str1))

# Methods od string :
'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', ''
 __getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '
__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__','
' '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__','
 '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
  'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',
 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper',
 'zfill']
'''

str2 = "Good Morning"

# Convert all character in upper case
print(str2.upper())

# Convert all characters in lower
print(str2.lower())

# Separate string by space or any character
output = str2.split("o")
print(output)

inputstr = input("Please enter your string :")

print(inputstr[:5],":", inputstr[6:])

# verify any char is in given string or not.

char = 'o'

if char in inputstr:
    print(True)
else:
    print(False)


# Capitalize : It capitalize first character of string

str1 ="hello"

print(str1.capitalize())

# Count : It will return number of time particular or sub string repeated in input string

print(str1.count('l'))

print(str1.count.__doc__)


# endswith : ti checks that given string is ended desired character or string
print(str1.endswith('h'))   #  It will return False

print(str1.endswith('o'))  # It will return True


# find : it return the initial index of substring

str2 = "We are working on python language"


output = str2.find('on')  # it should index of sub string
print(output)


output1 = str2.find('SS')  # it will return -1 if string does exist in given string
print(output1)

# format : It help to format string as per requirement

var1 = 'John'
var2 = 23

str1 = "Hello, This is {}, and my age is {}".format(var1, var2)
print(str1)

str2 = "Hello, This is "+ var1 + ", and my age is "+ str(var2)
print(str2)

str3 = f"Hello, This is {var1}, and my age is {var2}"
print(str3)


# raw string
str4 = r"'Today's is \n \s \d Thursday'"

print(str4)

str5 = "Hello, This is {}, and my age is {}Hello, This is {}, and my age is {}" \
       "Hello, This is {}, and my age is {}Hello, This is {}, and my age is {}" \
       "Hello, This is {}, and my age is {}Hello, This is {}, and my age is {}" \
       "Hello, This is {}, and my age is {}"


print(str5)

"""
str6 = """It help to format string as per requirement
It help to format string as per requirement
It help to format string as per requirement
It help to format string as per requirement
"""
"""
print(str6)

print(str6.count("format"))

print(str6[12:18])

# index : get index of specific sub string or character

index = str6.index('format')
print(index)


list1 = ["Hello", "Good", "Morning"]

# join : join list of string with any delimeter

output = " ".join(["Hello", "Good", "Morning"])
print(output)
output1 = "_".join(["Hello", "Good", "Morning"])
print(output1)
output2 = "#".join(["Hello", "Good", "Morning"])
print(output2)

print("%".join([output, output1, output2]))

# Replace : Replace any substring from given string
print("#"*50)
str1 = "We with learning automation with python"

newstr = str1.replace("with", "sagar", 0)

print(newstr)

# remove space : trailing and spacing from the string
print("#"*50)
str8 = " automation "
print(str8)
print(str8.strip())

# verify given string in alpha numeric


str9 = "HelloGood"
str11 = "$%$%%%"
str10 = "2345"
str12 = "Hello123"

print(str9.isalnum())
print(str12.isalnum())
print(str10.isalnum())

print(str11.isalnum())

# check for numeric

print(str9.isnumeric())

print(str10.isnumeric())

print(str12.isnumeric())

print("#"*30)


newstr = "hhh"

# Pad a numeric string with zeros on the left, to fill a field of the given width.
# The string is never truncated.

print(str1.zfill.__doc__)
print(len(newstr))
newoutput = newstr.zfill(10)

print(newoutput)
print(len(newoutput))


##################################
# Program 1 : Count total number of character repeated in given string.

str1 = "This series is designed to help you establish " \
       "an online marketing presence for your business. " \
       "These courses will enable you to learn digital skills, " \
       "connect with customers and start advertising with"

#1. Iterate through the string : for char in str1
#2. Count each char presence and ncrease and store

dict1 = {}

for char in str1:
    print(char)
    # T {"T": 1}, T {T: 2}, T {T:3}
    if char in dict1:
       dict1[char] += 1
    else:
       dict1[char] = 1

print(dict1)




# Solve same problem with inbuilt method.
dict2 = {}
for char in str1:
    dict2[char] = str1.count(char)

print(dict2)


##############################################################

# Program 2: Get longest length word in a given string.


newstr1 = "This series is designed to help you establish " \
       "an online marketing presence for your business. " \
       "These courses will enable you to learn digital skills, " \
       "connect with customers and start advertising with"

#1. Get list of all words in string using split method
#2. Get length of each word using loop and len method.

word_list = newstr1.split(" ")
print(word_list)

longest_word = ''
max_len = 0

for word in word_list:
    print(word, ":", len(word))
    wordlen = len(word)
    if wordlen > max_len:
        max_len = wordlen
        longest_word = word
    else:
        continue

print("Longest word:", longest_word)
print("Longest Length:", max_len)
"""

#####################################################
# Program 3 : Get longest repeated char in sequence in given string.
        #0123
str1 = "helllo aaaabcccccccc defffffffgghieee jjjjjsddds  ssssfffgg"

# 1. iterate through each char in loop, for char in str1
# 2. will each char should repeated in sequence.

max_len = 1

max_value = 1
result_char = ''
for i in range(len(str1)-1):
    print(i, str1[i])
    if str1[i] == str1[i+1]:
        print("Max_value:", max_value)
        print("Result_char:", result_char)

        max_len += 1
        if max_len > max_value:
            max_value = max_len
            result_char = str1[i]

        else:
            continue
    else:
        max_len = 1
        continue

print("Max value :", max_value)
print("Result char :", result_char)
