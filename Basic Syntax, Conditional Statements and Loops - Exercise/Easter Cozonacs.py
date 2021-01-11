budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_liter_price = flour_price * 1.25
milk_needed_price = milk_liter_price / 4
cozonac_price = eggs_price + flour_price + milk_needed_price

colored_eggs = 0
count_cozonacs = 0

while budget >= cozonac_price:
    count_cozonacs += 1
    colored_eggs += 3
    if count_cozonacs % 3 == 0:
        colored_eggs -= count_cozonacs - 2
    budget -= cozonac_price
print(f"You made {count_cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")