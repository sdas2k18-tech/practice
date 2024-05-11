def find_gcd(a,b):

    while a >0 and b > 0:
        if a > b:
            a= a%b
        else:
            b= b%a
    
    if a==0:
        return b       
    else:
        return a



def main():
    n1 = int( input("n1: "))
    n2 = int( input("n2: "))

    # Find the GCD of n1 and n2
    gcd = find_gcd(n1, n2)

    print(f"GCD of {n1} and {n2} is: {gcd}")


if __name__ == "__main__":
    main()