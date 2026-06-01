# Question 1 - ATM Withdrawal Validator

balance = int(input("Enter your bank balance: "))
withdrawn = int(input("Enter money already withdrawn today: "))
amount = int(input("Enter the amount you want to withdraw: "))

if amount % 500 != 0:
    print("Amount must be multiple of 500")

elif amount > balance:
    print("Not enough balance")

elif withdrawn + amount > 50000:
    print("Daily limit reached")

else:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance is NPR", balance)