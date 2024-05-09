def printNames(i,n):
    if i > n :
        return
    
    print("Subhasish")

    printNames(i+1,n)


# if __name__=='__main__':
n = int(input("no of times: "))
    # name = input("enter a name: ")
    # print("hello")
printNames(1,n)
