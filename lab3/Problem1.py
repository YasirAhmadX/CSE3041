#28th July (Problem 1 average of marks) 22MIA1064 Yasir Ahmad
"""
find avergae of marks, terminate if marks < 0
"""


n = int(input("Number of students: "))
i = 0
avg = 0
while i<n:
    a = int(input("Enter marks:" ))
    if(a<0):
        print("Invalid input")
        break
    else:
        avg += a/n
        i+=1
else:
    print(f"average marks: {avg:.2f}");
