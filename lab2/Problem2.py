#26th July (Problem 2 marks) 22MIA1064 Yasir Ahmad

cat1 = int(input("Enter cat1 mark: "))
cat2 = int(input("Enter cat2 mark: "))

if(cat1+cat2 >= 2*90):
    print("excellent")
elif(cat1 >= 90 or cat2 >=90):
    print("good")
else:
    print("need to improve")
