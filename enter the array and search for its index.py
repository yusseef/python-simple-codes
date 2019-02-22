from array import *
arr=array('i',[])
n=int(input("enter the length "))
for i in range(n):
    x=int(input("Enter value "))
    arr.append(x)
print(arr)
k=0
val=int(input("Enter the value to search "))
for e in arr:
    if e==val:
        print("the index= ",k)
    k+=1
