command = input()
quantities_dict = {}
prices_dict = {}
while not command == "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    prices_dict[name] = price

    if name not in quantities_dict:
        quantities_dict[name] = 0
    quantities_dict[name] += quantity
    command = input()

for key, price in prices_dict.items():
    total = price * quantities_dict[key]
    print(f"{key} -> {total:.2f}")
