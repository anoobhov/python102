#Factorial via recursion
def factorial(x):
    if x==0:
        return 1
    return x*factorial(x-1)

print(factorial(5))

"""
* * * * * 
* * * *
* * *
* *
*

"""
def pattern(n):
    if n == 6:
        return

    pattern(n+1)

    for i in range(n):
        print("*",end=" ")
    print("")


pattern(1)


