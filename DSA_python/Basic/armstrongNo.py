def armstrongNo(y):
    N = y
    dup = y
    sum = 0
    if y < 0 :
        return False

    while N != 0 :
        digit = N %10
        sum = sum + digit * digit * digit
        N = N //10

    if dup == sum:
        return True
    else:
        return False
    
x= int(input("enter a number: "))
print(" result : " + str(armstrongNo(x)))
       


