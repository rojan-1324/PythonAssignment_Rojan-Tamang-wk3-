import random

random.seed(42)

friends = ["Ramesh", "Sunita", "Bikash", "Anjali", "Dipak"]
total_bill = 3750

def split_bill(friends, total):
    return total/len(friends)

def pick_lucky(friends):
    return random.choice(friends)

def final_summary(friends, total):
    base_share = split_bill(friends, total)
    lucky_person = pick_lucky(friends)
    
    print("Bill Split Summary:")
    for f in friends:
        if f == lucky_person:
            lucky_total = base_share+50 # local variable
            print(f, "pays:", lucky_total)
        else:
            print(f, "pays:", base_share)
            
    print("Lucky person who pays extra 50 is:", lucky_person)

final_summary(friends, total_bill)