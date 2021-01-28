'''
def fun1(x):
    print(x+20)
fun1(30)

output = lambda x:x+20
print(output(40))

output1 = lambda x, y, z: x+y+z

print(output1(30, 40, 50))

# Map Function : Provide multiple inputs to single function using map

def function2(n):
    return n**2

list1 = [4, 6, 8, 12, 14]
for val in list1:
    function2(val)

print("#"*20)
result = list(map(function2, list1))
print(result)

result2 = list(map(lambda x:x**2, list1))
print(result2)
'''
# Filter :  It return all the true values as per expectation.

list2 = [4, 7, 8, 23, 45, 50]

result = list(filter(lambda x: x%2!=0, list2))
print(result)

