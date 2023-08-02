#2nd August (Problem 3 validity of mobileNo and PAN) 22MIA1064 Yasir Ahmad

# valid PAN number
# valid mobile number
# format for integer number
# format for float number

import re

# valid PAN number

pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]$"

PAN = input("Enter PAN number: ").upper()

print("Valid" if re.match(pattern,PAN) else "Not Valid")

# valid mobile number

pattern2 = r"^[1-9][0-9]{9}"

MobNo = input("Enter Mobile No: ")

print("Valid" if re.match(pattern2,MobNo) else "Not Valid")

# format for integer number

patternInt = r"^\-?[0-9]+$"

Int = input("Enter Integer: ")

print("Valid" if re.match(patternInt,Int) else "Not Valid")

# format for float number

patternFloat = r"^\-?[0-9]+[.]{1}[0-9]+$"

Float = input("Enter Float: ")

print("Valid" if re.match(patternFloat,Float) else "Not Valid")
