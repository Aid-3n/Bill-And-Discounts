product_list = { "Item A": 20, "Item B": 40, "Item C": 50 } #Items_List as per question given


discounts = {
    "flat10": 10 if subtotal > 200 else 0, #Discount option 1
    "bulk5": sum(products[product] * quantities[product] * 0.05 if quantities[product] > 10 else 0 for product in products), #Discount option 2
    "bulk10": subtotal * 0.1 if sum(quantities.values()) > 20 else 0, #Discount option 3
    "dis50": sum(products[product] * max(0, quantities[product] - 15) * 0.5 if quantities[product] > 15 else 0 for product in products) #Discount option 4 }
  
quantities = {}
giftwrap = {}
for product in product_list:
    quantities[product] = int(input(f"Enter the number of {product}: "))
    gift_wrap[product] = input(f"Should {product} need gift wrap? (y/n): ") == "y"
  
  
