dic1={'a':2,'b':4,'c':6,'d':8}
dic2

for key,value in dic1.items():
    value=value/2
    dic1[key]=value
print(dic1)
