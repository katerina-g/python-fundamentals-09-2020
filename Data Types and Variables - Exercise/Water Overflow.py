WATER_TANK_CAPACITY = 255

n = int(input())
total_quantity = 0

for i in range(n):
    water_quantity = int(input())
    if total_quantity + water_quantity > WATER_TANK_CAPACITY:
        print("Insufficient capacity!")
    else:
        total_quantity += water_quantity
print(f"{total_quantity}")
