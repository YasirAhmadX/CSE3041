#2nd August (Problem 1 Ceaser cipher) 22MIA1064 Yasir Ahmad

s = input("Enter message: ")
key = 3

for i in s.lower():
    
    c = (ord(i)-97 + key)%26
    c = chr(c+97)

    """
    c = ord(i)+key
    c = chr(c - (26 if c>122 else 0))
    """
    
    print(c,end="")
