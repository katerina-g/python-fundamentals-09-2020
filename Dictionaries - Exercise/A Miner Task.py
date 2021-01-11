resources = {}

command = input()

while not command == "stop":
    value = int(input())
    if command not in resources:
        resources[command] = value
    else:
        resources[command] += value
    command = input()

for k, v in resources.items():
    print(f"{k} -> {v}")

