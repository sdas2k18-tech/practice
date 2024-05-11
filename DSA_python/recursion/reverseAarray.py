# reverse a array
# 3 methods
# iterative
# spacve optimised iterative
# recursive, iterate using recursion

#produce an array from user input
# # creating an empty list
# lst = []

# # number of elements as input
# n = int(input("Enter number of elements : "))

# # iterating till the range
# for i in range(0, n):
# 	ele = int(input())
# 	# adding the element
# 	lst.append(ele) 

# print(lst)

# # solution 1
# def printArray(arr,n):
#     print("reversed array is : ")
#     for i in range(n):
#         print(arr[i], end=" ")
#     print()#new line 
      

# def reverseArray(arr,n):
#     ans= [0] *n # [0,0,0,0,0,....ntimes]
#     for i in range(n-1,-1,-1):
#         ans[n-i-1]= arr[i]
#     printArray(ans,n)    
      
# #driver code
# if __name__ == "__main__":
#     arr=[4,3,6,7,7,8,9]
#     n= len(arr)
#     reverseArray(arr, n)

#solution 2- take 2 pointers and swap

# sol 3- recursive; call the finc ahain and again by start++ and end-- the pointer values


def printArray(arr, n):
    print("reverse array is: ")
    for i in range(n):
        print(arr[i], end=" ")
    print()
    
def reverseArray(arr, start, end):
    if start >= end:
        return
    arr[start],arr[end] = arr[end],arr[start]
    reverseArray(arr, start + 1, end - 1)
    

# Driver Code
if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    reverseArray(arr, 0, n - 1)
    printArray(arr, n)