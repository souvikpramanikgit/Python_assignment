# write a function to return compound interest.
# CI = P (1 + r/n) ^ nt

def compound(p,r,n,t):
    """calcualte compound interest"""
    c_i=p*((1+(r/n))**(n*t))
    return c_i

print(f"The compound interest is: {compound(10000,8,1,2)}")