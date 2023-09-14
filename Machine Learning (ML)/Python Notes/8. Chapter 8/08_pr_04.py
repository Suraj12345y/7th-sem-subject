# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n

def sumOf(n):
    if n==0 or n==1:
        return 1
    else:
        return n + sumOf(n-1)

print(sumOf(4))    