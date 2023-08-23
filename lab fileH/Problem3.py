#23rd August (File handling Problem3 CSV) Yasir Ahmad 22MIA1064

f = open("marks.csv","r")

hd = f.readline()
#print(hd)

r = open("result.csv","w")
hd = hd[:-2]+",Total\n"
r.write(hd)

for line in f.readlines():
    
    line = line.replace("\n","")
    l = line.split(",")
    
    #name = l[0]
    m = map(int,l[1::])
    total = sum(m)
    
    l.append(str(total)+"\n")
    l = ",".join(l)

    r.write(l)

f.close()
r.close()
