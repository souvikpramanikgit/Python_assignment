# write a program to find given number is positive ,negative or zero.

a=int(input("Enter a number: "))

if a>0:
    print(f"{a} is a positive number")
elif a==0:
    print(f"{a} is a negative number")
else:
    print(f"{a} is zero")
