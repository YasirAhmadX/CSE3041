#22nd August (File handling Problem2 longest sentance) Yasir Ahmad 22MIA1064

f1 = open("note.txt","r")

lines = f1.readlines()

lines.sort(key = lambda x: len(x) ,reverse = True)

print(lines[0])
