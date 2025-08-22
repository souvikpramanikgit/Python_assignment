# write a function to return simple interest.

def si(p,r,t):
    """Calculate simple interest"""
    s_i=(p*r*t)/100
    return s_i

simple_interest=si(p=1000,r=7,t=2)

print(f"The simple interest is : {simple_interest}")