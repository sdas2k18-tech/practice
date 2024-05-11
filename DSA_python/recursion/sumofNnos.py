#calculate sum of n natural nos.
# may ways parameter wise, for loop, formula, recursive= parameterised and functionl
#best TC= formula method n*(n+1)/2

#recursive functional method-

def func(n):
    #base condition
    if n == 0 :
        return 0
    
    return n + func(n-1)

n= int(input("input: "))
print(func(n))
