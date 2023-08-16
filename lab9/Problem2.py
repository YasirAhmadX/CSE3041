#16th August (arae of triangle) 22MIA1064 Yasir Ahmad

x1,y1 = [int(i) for i in input("a: ").split(',')]
x2,y2 = [int(i) for i in input("b: ").split(',')]
x3,y3 = [int(i) for i in input("c: ").split(',')]
"""
def perimeter(a,b,c):
    s = 0
    s += (((a[0]-b[0])**2) + (a[1] - b[1])**2)**.5
    s += (((b[0]-c[0])**2) + (b[1] - c[1])**2)**.5
    s += (((a[0]-c[0])**2) + (a[1] - c[1])**2)**.5
    return s

def heron_sArea(a,b,c):
    s = perimeter(a,b,c)/2

    area = (s*(s-((a[0]-b[0])**2 + (a[1] - b[1])**2)**.5)*(s-((b[0]-c[0])**2 + (b[1] - c[1])**2)**.5)*(s-(a[0]-c[0])**2 + (a[1] - c[1])**2)**.5)

    return area
#ar = heron_sArea((x1,y1),(x2,y2),(x3,y3))
"""

def area_determinant(a,b,c):
    area = abs(a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1]))/2
    return area

ar = area_determinant((x1,y1),(x2,y2),(x3,y3))
print(ar)
