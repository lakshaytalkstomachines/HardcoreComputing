"""
    Find the remaining balance after deducting the money and fees and if the withdrawn_amount is divisible by 5. 
    First number is the amount to be withdrawn, second is the original bank balance.
"""
withdrawn_amount, bank_balance = map(float, input().split(" "))
fees = 0.50

if (withdrawn_amount % 5 == 0) and (withdrawn_amount + fees) <= bank_balance:
    print(bank_balance-(withdrawn_amount + fees))
else:
    print(bank_balance)
