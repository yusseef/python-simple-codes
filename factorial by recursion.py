def recursion_factorial(n):
    if n == 0:
        return 1
    return n*recursion_factorial(n-1)


x = int(input())

print(recursion_factorial(x))
