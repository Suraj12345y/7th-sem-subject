# def greatest(a,b,c):
#     if(a>=b and a>=c):
#         return a
#     elif(b>=c and b>=a):
#            return b
#     elif(c>=a and c>=b):
#         return c


# a=int(input("Enter no1: "))
# b=int(input("Enter no2: "))
# c=int(input("Enter no3: "))

# print(greatest(a,b,c))

####################################

# def sumOf(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n + sumOf(n-1)

# print(sumOf(4))    

##################################

def patten(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        print("\n")

print(patten(5))
