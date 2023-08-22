#22nd August (File handling Problem2 longest sentance) Yasir Ahmad 22MIA1064

f1 = open("note.txt","r")

def longest_line(filename):
    lngst_line = ""
    lines = filename.readlines()

    for line in lines:
        if len(line) > len(lngst_line):
            lngst_line = line
            
    return lngst_line

l = longest_line(f1)
print("longestLine: ",l)
