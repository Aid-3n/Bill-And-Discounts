product_list = { "Item A": 20, "Item B": 40, "Item C": 50 } #Items_List as per question given
quantities = {}
giftwrap = {}
for product in product_list:
    quantities[product] = int(input(f"Enter the number of {product}: "))
    giftwrap[product] = input(f"Should {product} need gift wrap? (y/n): ") == "y"

ship_fee = 5 * (sum(quantities.values()) // 10 + (1 if sum(quantities.values()) % 10 > 0 else 0)) 
gift_fee = sum(quantities[product] if giftwrap[product] else 0 for product in product_list) 
subtot = sum(product_list[product] * quantities[product] for product in product_list) #Calculaing subtoal

discounts = {
    "flat10": 10 if subtot > 200 else 0, 
    "bulk5": sum(product_list[product] * quantities[product] * 0.05 if quantities[product] > 10 else 0 for product in product_list), 
    "bulk10": subtot * 0.1 if sum(quantities.values()) > 20 else 0, 
    "dis50": sum(product_list[product] * max(0, quantities[product] - 15) * 0.5 if quantities[product] > 15 else 0 for product in product_list) }

discountt = max(discounts, key=discounts.get) 
dis_amt = discounts[discountt]
subto_with_disc = subtot - dis_amt

total = subto_with_disc + ship_fee + gift_fee #Total bill with disco

print("\nDetails of Product chosen")
for product in product_list:
    print(f"{product}: {quantities[product]} units, total amount: ${product_list[product] * quantities[product]}")
print(f"Subtotal: ${subtot}")
print(f"Discount applied ({discountt}): -${dis_amt}")
print(f"Shipping fee: ${ship_fee}")
print(f"Gift wrap fee: ${gift_fee}")
print(f"Total Amount: ${total}")
