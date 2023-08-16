#16th August (GCD in recursion) 22MIA1064 Yasir Ahmad
"""
GCD in recursion
"""

n = int(input("n: "))
m = int(input("m: "))

def hcf(a,b):
    if a%b==0:
        return b
    else:
        return hcf(b,a%b)
    
print(hcf(n,m))
