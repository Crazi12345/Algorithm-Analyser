import math
a = 0 
b = 1
d = 0 


def MasterTheorum(a,b,d):
    print(str(d)+"  "+str(math.log(a,b)))
    if(d>math.log(a,b)):
        return "O(n^"+str(d)+") and maybe with an added extra function like log n"

    if(d == math.log(a,b)):
        return "O(n^"+str(d)+"*"+"log(n))"

    if(d< math.log(a,b)):
        return "O(n^"+str(math.log(a,b))+") OR O(n^log("+str(a)+"))" 
    return "ERROR"



inputVal = input("please input an a value: ")
if (float(inputVal)>a):
    a = float(inputVal)
else:
    print("unsolveable")

inputVal = input("please input an b value: ")
if (float(inputVal)>b):
    b = float(inputVal)
else:
    print("unsolveable")
inputVal = input("please input an d value: ")
if (float(inputVal)>=d):
    d = float(inputVal)
else:
    print("unsolveable")
print(MasterTheorum(a,b,d))
