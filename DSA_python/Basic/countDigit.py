                                
# # Function to count the number
# # of digits in an integer 'n'.
# def countDigits(N):

#     cnt = 0

#     while N > 0:
#         cnt = cnt +1

#         N= N // 10
    
#     return cnt

    
    


# if __name__ == "__main__":
#     N = int(input())
#     print("N:", N)
#     digits = countDigits(N)
#     print("Number of Digits in N:", digits)
import math

n= 10000
y= int(math.log10(n)) +1 
print(y)


