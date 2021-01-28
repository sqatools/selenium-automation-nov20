""""dic1={'a':2,'b':3,'c':21,'d':12,'e':5}
dic2={}
dic3={}
for key,value in dic1.items():
    #value=value**2
    if(value%2==0):
        dic2[key]=value
    #print(dic2)
    else:
        dic3[key]=value
print(dic2)
print(dic3)"""
dic1={'x':'HellO','y':'Good'}
dic2={}
for key,vlaue in dic1.items():
    v1=vlaue.swapcase()
    dic2[key]=v1
print(dic2)
