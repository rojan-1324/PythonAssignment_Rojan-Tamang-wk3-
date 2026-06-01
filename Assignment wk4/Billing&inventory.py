inventory={
"rice":{"price":120,"stock":20},
"milk":{"price":90,"stock":10},
"bread":{"price":60,"stock":15},
"eggs":{"price":15,"stock":30}
}

cart={
"rice":2,
"milk":3,
"eggs":12
}

def process_order(inventory,cart):
 total=0

 print("bill:")

 for item in cart:
  qty=cart[item]

  if qty<=inventory[item]["stock"]:
   cost=inventory[item]["price"]*qty
   total=total+cost

   inventory[item]["stock"]=inventory[item]["stock"]-qty

   print(item+" x"+str(qty)+" = NPR",cost)

  else:
   print("Sorry, not enough stock for",item)

 print("Grand Total: NPR",total)

 print("Updated stock:")
 for item in inventory:
  print(item+"="+str(inventory[item]["stock"]))

process_order(inventory,cart)