"""
first we want to print
        # # # #
        # # # #
        # # # #
        # # # #
"""
for i in range(4):
    for j in range(4):
        print("# ",end="")
    print("")
"""
sec. 
   #
   # #
   # # #
   # # # #
"""
for i in range(4):
    for j in range(i+1):
        print("# ", end="")
    print("")
"""
third.
   # # # #
   # # #
   # #
   #
"""
for i in range(4):
    for j in range(4-i):
        print("# ",end="")
    print("")
