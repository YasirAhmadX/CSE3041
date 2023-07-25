#25th July (Problem 1) 22MIA1064 Yasir Ahmad

b_pay = float(input("Enter basic pay: "))
da = 0.8*b_pay
hra = 0.3*b_pay
pf = 0.12*b_pay

gross = b_pay + da + hra - pf

print("Gross salary:",gross)
   
