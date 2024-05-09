def palindrome(y):
    N = y
    dup = y
    rev = 0

    while N != 0 :
        digit = N %10
        rev = rev * 10 + digit
        N = N //10

    if dup == rev:
        return True
    else:
        return False
    
x= int(input("enter a number: "))
print(palindrome(x))
       


