#2nd August (Problem 2 validity of registration number) 22MIA1064 Yasir Ahmad

"""
<2Xnumber><3Xalpha><4Xnumber>
"""

import re

pattern = r"^[1-9][0-9][a-zA-Z]{3}[0-9]{4}$"

reg = input("Enter registration no.: ")

print("Valid" if re.match(pattern,reg) else "Not Valid")

