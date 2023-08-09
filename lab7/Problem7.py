#9th August (Problem 7 lab tests) 22MIA1064 Yasir Ahmad

report = ()
table = ([20,30],[35.5,40],[12,15],[120,150],[80,120])

for i in range(5):
    report += (input("Enter lab report {0}: ".format(i+1)),)

for i in range(5):
    if (report[i]=="N"):
        print(f"Test {i+1} not performed ?")
    elif (min(table[i])<=float(report[i])<=max(table[i])):
        print(f"Test {i+1} Passed.")
    else:
        print(f"Test {i+1} Failed !")


