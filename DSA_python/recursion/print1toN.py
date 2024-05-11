def printSDZ(n):
    if n ==0:
        return

    print(n,end= ' ' )# print statement before function call will give output in desc order
    
    printSDZ(n-1)
    
    print(n,end=" ")# print statement after function call will print no in asc order


n = int(input("enter a number: "))
printSDZ(n)