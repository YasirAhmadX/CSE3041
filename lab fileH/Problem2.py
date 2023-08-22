#22nd August (File handling Problem2 longest sentence) Yasir Ahmad 22MIA1064

f1 = open("note.txt","r")

max_len_i = 0
lines = f1.readlines()

for i in range(len(lines)):
    if len(lines[i]) > len(lines[max_len_i]):
        max_len_i = i
        
print(i,lines[i])
