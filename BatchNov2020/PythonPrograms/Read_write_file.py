"""
file = open("filepath", 'access')

r, : Read Operation
w, : Write Operation
a, : Append Operation
"""
"""
# Read data from file
fileobj = open('testfile.txt', 'r')
data = fileobj.read()
print(data)
fileobj.close()

print("#"*50)
fileobj = open('testfile.txt', 'r')
data2 = fileobj.read()
print("data2:", data2)

# C:\\testdata\\filename.txt

print(len(data2))

words = data2.split(" ")
print(words)
print(len(words))



# Write Data into the file.
# 1. In case of write , new file will be created if it is not available
# 2. Existing content of file will be overwrite.

write_file = open("writefile.txt", 'w')
content = "This Training session where we are learning Python"
write_file.write(content)
content2 = " \n Its automation training session"
write_file.write(content2)
write_file.close()


obj2 = open("writefile.txt", 'w')
obj2.write("New data Entered")
obj2.close()


# 3. Append data to the file.

Filename = 'append_data.txt'

new_cont = "\nSite speed no longer just impacts your conversion rate, " \
           "but it also affects how high your site can rank in search engines"

new_cont2 = "\n More content to be added"

file_obj = open(Filename, 'a')
file_obj.write(new_cont)
file_obj.close()


file_obj2 = open(Filename, 'a')
file_obj2.write(new_cont2)
file_obj.close()
"""
#####################################################
"""
# Read File with readlines

fileobj = open("C:\\Testdata\\testreadfile.txt", 'r')


# read data in byte
bytedata = fileobj.read(10)
print(bytedata)

# read single line
line = fileobj.readline()
print(line)

# read multiple lines
lines = fileobj.readlines()
print(lines)

# Program : read last three lines of file
for i in range(-1, -4, -1):
    print(lines[i])

# read content of file using loop.
for line in fileobj:
    print(line)


fileobj.close()
"""

###########################File cursor and its position ################
"""
obj = open("C:\\Testdata\\testreadfile.txt", 'r')

# tell : which provides information about cursor position

print(obj.tell())

# seek : set cursor position

print(obj.seek(50))
print(obj.tell())

data = obj.readline()
print(data)

print(obj.tell())
print(obj.seek(100))
data2 = obj.readline()
print(data2)
obj.close()

"""
##################Context Manager ###########
# context manager have in build enter and exit method.
# It means no need to close file object explicitly.

"""
with open("filepath", 'access mode') as file
    file.read


with open('testfile.txt', 'r') as file:
    data = file.read()
    print(data)

print("#"*20)
with open('testfile.txt', 'r') as file:
    data = file.readline()
    print(data)

print("#"*20)
with open('testfile.txt', 'r') as file:
    data = file.readlines()
    print(data)


with open('testfile.txt', 'r') as file:
    print(file.mode)
    print(file.name)
    print(file.readable())

"""
# Program : Read file1 and put content in file2

with open('testfile.txt', 'r') as file1:
    file1_data = file1.read()

with open('testfile2.txt', 'w') as file2:
    file2.write(file1_data)