# Write a Python function to find the maximum of three numbers.

def maximum(a,b,c):
    """Write a Python function to find the maximum of three numbers"""
    max=0
    if a>b and a>c:
        max=a
    elif b>a and b>c:
        max=b
    else:
        max=c
    return max

print(f"The maximum number is {maximum(1,5,6)}")