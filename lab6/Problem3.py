#8th August (Problem 3 ) 22MIA1064 Yasir Ahmad

"""
Watson gives Sherlock a list of N numbers. Then he asks him to determine if
there exists an element in the list such that the sum of the elements on its
left is equal to the sum of the elements on its right. If there are no elements
to the right/left, then the sum is considered to be zero.
"""

N = int(input("Enter N: "))
l = []
s = 0

for i in range(N):
    l.append(int(input("Enter number {0}: ".format(i+1))))



for i in range(N):
    Ll = l[0:i]
    Rl = l[i+1:N]

    if (sum(Ll)==sum(Rl)):
        print(f"Required Number: l[{i}] = {l[i]}")
        break
else:
    print("Condition not satisfied.")
