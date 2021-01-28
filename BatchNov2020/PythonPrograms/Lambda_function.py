from functools import reduce
x = lambda a: a + 10

print(x(40))

output = lambda x, y : x+y

print(output(40, 30))

# use with map :

list1 = [3, 6, 8, 9, 10]

result = list(filter(lambda x : x%2==0, list1))
print(result)

result2 = list(map(lambda x: x**2, list1))
print(result2)


result3 = reduce(lambda x,y :x+y, list1)
print(result3)

def function1(n):
    return n**2

result4 = list(map(function1, list1))
print(result4)
#________________________________________________________________



