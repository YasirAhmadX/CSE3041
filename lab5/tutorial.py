#2nd August (Regular expression tutorial) 22MIA1064 Yasir Ahmad

import re

"""
The special characters are:
        "."      Matches any character except a newline.
        "^"      Matches the start of the string.
        "$"      Matches the end of the string or just before the newline at
                 the end of the string.
        "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
                 Greedy means that it will match as many repetitions as possible.
        "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
        "?"      Matches 0 or 1 (greedy) of the preceding RE.
        *?,+?,?? Non-greedy versions of the previous three special characters.
        {m,n}    Matches from m to n repetitions of the preceding RE.
        {m,n}?   Non-greedy version of the above.
        "\\"     Either escapes special characters or signals a special sequence.
        []       Indicates a set of characters.
                 A "^" as the first character indicates a complementing set.
        "|"      A|B, creates an RE that will match either A or B.
        (...)    Matches the RE inside the parentheses.
"""

if re.match("f.o$","fooo"): #start anywhere, f<anything>o<end>
    print("Matched")
else:
    print("Not matched")
if re.match("..","lol"): #any two characters
    print("Matched")
else:
    print("Not matched")
if re.match(".end","bends"): # start anywhere, <anything>end<anything(if)>
    print("Matched")
else:
    print("Not matched")
if re.match(".end$","bends"): # start anywhere, <anything>end<end>
    print("Matched")
else:
    print("Not matched")
