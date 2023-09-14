# a=int(input("Enter a number: "))
# for i in range (1,11):
#     print(a ,"*",i ,"=",(a*i))
###############################
# l1=['harry','tomy','sam','suvo','asis','simran']

# for i in l1:
#     if i.startswith("s"):
#         print("Hello "+i)

########################################


# a=int(input("Enter a number: "))
# i=1
# while(i <= 10):
#     print(f"{a} x {i} = {a*i}")
#     i=i+1

###########################################


# a=int(input("Enter a number: "))
# c=0

# for i in range(1,a+1):
#     if (a%i==0):
#         c=c+1
# if c==2:
#     print("prime")
# else:
#     print("Not prime")

#######################################


# a=int(input("Enter a number: "))
# s=0
# for i in range(1,a+1):
#     s=s+i

# print(s)

###########################################

# a=int(input("Enter a number: "))
# f=1

# for i in range(1,a+1):
#     f=f*i
# print(f)

#########################################

# a=int(input("Enter a number: "))

# for i in range(a+1):
#     print("*" * (i+1))

###########################################

# a=int(input("Enter a number: "))

# for i in range(1,a+1):
#     if((i==1) or (i==a)):
#         print("*" *a)
#     else:
#         for j in range(1,a+1):
#             if(j==1 or j==a):
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#     print("\n")

############################################

num = int(input("Enter the number: "))
for i in range(-10, 0):
    # print(str(num) + " X " + str(i) + "=" + str(i*num))
    print(f"{num}X{abs(i)}={num*abs(i)}")