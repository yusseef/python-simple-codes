import random
bomb=random.randint(0,3)
number=int(input("enter number between (0,3) "))
if number==bomb:
    print("sorry you are exploded")
else:
    print(" ***WINNER***")
print("your number = ",number ,"random = ",bomb)



