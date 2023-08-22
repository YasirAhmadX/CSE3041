#22nd August (File handling Problem1 copy) Yasir Ahmad 22MIA1064

f1 = open("note.txt","r")
f2 = open("s2.txt","w")

content = f1.readlines()
f2.writelines(content)

f1.close()
f2.close()
