#1st August (Problem 3 PAN) 22MIA1064 Yasir Ahmad

"""
in a PAN card number check validity.
PAN = <char><char><char><char><char><digit><digit><digit><digit><char>
"""

PAN = input("Enter PAN card number: ")

characters = PAN[:5] + PAN[-1]
digits = PAN[5:-1]

#condition booleans
c1 = len(PAN) == 10  #length constraint
c2 = characters.isupper() #upper case constraint
c3 = characters.isalpha() #<char> constraint
c4 = digits.isdigit() #<digit> constraint

print("VALID" if c1 and c2 and c3 and c4 else "NOT VALID")
