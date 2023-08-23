#23rd August (CSE3041 – Programming for Data Science Practice Questions)
#Yasir Ahmad 22MIA1064
#Q4
m = int(input("Enter m: "))
n = int(input("Enter n: "))

def gcd_euclid(a,b):
    if b==0:
        return a
    else:
        return gcd_euclid(b,a%b)

print(gcd_euclid(m,n))
