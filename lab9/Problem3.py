#16th August (student details) 22MIA1064 Yasir Ahmad

stud_details = []

for i in range(int(input("Enter no. of students: "))):
    details = []
    details.append(input("RegNo: "))
    details.append(int(input("Marks1: ")))
    details.append(int(input("Marks2: ")))
    details.append(int(input("Marks3: ")))
    stud_details.append(details)

def detail_augmentation(l):
    for i in l:
        mrks = i[1::]
        i.append(sum(mrks)/len(mrks))

def result(l):
    print("RegNo","mark1","mark2","mark3","avg","result",sep="#\t")
    for i in l:
        print(*i,"PASS" if i[-1]>59 else "FAIL" ,sep="  #\t ")

detail_augmentation(stud_details)
result(stud_details)
