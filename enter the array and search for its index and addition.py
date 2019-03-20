from numpy import *
arr = ([])
n = int(input("enter the length"))
for i in range(n):
    x = int(input("enter values"))
    arr.append(x)
print(arr)
val = int(input("enter the value to search"))
k = 0
for e in arr:
    if e == val:
        print("the index = ",k)
    k+=1
w = 0
for q in arr:
    w = w+q
print("All indexs equals ", w)
