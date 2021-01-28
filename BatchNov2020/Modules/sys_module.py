import sys

# Get Platform detail
print(sys.platform)

# get version information
print(sys.version)

# Get python version information
print(sys.version_info)

# get platform version details
print(sys.getwindowsversion())


userinput = input("Please enter the details: ")
print(userinput)

print(sys.argv)

print("Name :", sys.argv[1])

print("Age :", sys.argv[2])

print("Salary :", sys.argv[3])

print("Email :", sys.argv[4])

for email in sys.argv[4].split(","):
    print(email)