def fact(n):
    f =1
    for i in range(1,n+1):
        f = f * i

    return f

def fact2(n):
    if n==0:
        return 1

    return n * fact2(n-1)


N = int(input("enter a number: "))

# result = fact(N)
# print(" the factorial of " + str(N) + " is " + str(res2))


# using recursion
res2 = fact2(N)
print(" the factorial of " + str(N) + " is " + str(res2))