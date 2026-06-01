# Question 2 - Online Store Discount System

purchase = float(input("Enter your total shopping amount: "))
member = input("Are you a loyalty member? yes or no: ")

if purchase < 1000:
    discount = 0

elif purchase < 5000:
    discount = 5

elif purchase < 15000:
    discount = 10

else:
    discount = 20

discount_money = purchase * discount / 100
final_price = purchase - discount_money

if member == "yes":
    extra = final_price * 5 / 100
    final_price = final_price - extra

print("Final amount to pay is NPR", final_price)