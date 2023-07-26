#26th July (Problem 3 billing) 22MIA1064 Yasir Ahmad
"""
Given the number of hours and minutes browsed, write a program to calculate bill
for Internet Browsing. user time limit is 7 hours
Billing conditions:
    1 hr for Rs.50
    1 min for Rs.1
    Rs.200 for 5 hr
"""


hr = int(input("Enter hours: "))
mi = int(input("Enter minutes: "))

if(hr > 7):
    print("User time limit exceeded")
else:
    bill = 0
    while(hr > 5):
        hr -= 5
        bill += 200
    while(hr > 0):
        hr -= 1
        bill += 50
    bill += mi

    print(f"bill: {bill}")
