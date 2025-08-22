# Write A Program which is taking 5 int value and calculate sum of cube of all numbers [Write cube function]

def cube(a,b,c,d,e):
    """sum of cube of all numbers"""
    sum=a+b+c+d+e
    print(f"The sum of cube of all numbers is: {sum}")
    
a=int(input("Enter 1st number: "))**3
b=int(input("Enter 2nd number: "))**3
c=int(input("Enter 3rd number: "))**3
d=int(input("Enter 4th number: "))**3
e=int(input("Enter 5th number: "))**3

cube(a,b,c,d,e)