#23rd August (CSE3041 – Programming for Data Science Practice Questions) 
#Yasir Ahmad 22MIA1064 
#Q6

x1,y1 = list(map(int,input("Enter x1,y1: ").split(",")))
x2,y2 = list(map(int,input("Enter x2,y2: ").split(",")))
x3,y3 = list(map(int,input("Enter x3,y3: ").split(",")))

#print(a,b,c)

#area in determinant form
area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2


print(f"Its a triangle of area {area} sq. units" if area>0 else "Not a triangle")
