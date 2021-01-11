quantity = int(input())
days = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights = 15

christmas_spirit = 0
day = 1
budget = 0
while day <= days:
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget += ornament_set_price * quantity
        christmas_spirit += 5
    if day % 3 == 0:
        budget += (tree_skirt_price * quantity) + (tree_garlands_price * quantity)
        christmas_spirit += 13
    if day % 5 == 0:
        budget += tree_lights * quantity
        christmas_spirit += 17
    if day % 15 == 0:
        christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        budget += tree_lights + tree_garlands_price + tree_skirt_price
    day += 1
if days % 10 == 0:
    christmas_spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {christmas_spirit}")

