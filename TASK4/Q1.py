#Problem-1

#Write a program to find if a given number is divisible by 3, without using the ‘%’ operator explicitly (like N % 3 == 0).

n = int(input("enter a number"))
while n>0:
    n = n-3
if n==0:
    print("True")
else:
    print("False")