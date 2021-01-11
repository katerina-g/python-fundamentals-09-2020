n = int(input())

parking = {}

for _ in range(n):
    args = input().split()
    command = args[0]
    user = args[1]
    if command == "register":
        license_number = args[2]
        if user in parking:
            print(f"ERROR: already registered with plate number {parking[user]}")
            continue
        parking[user] = license_number
        print(f"{user} registered {license_number} successfully")
    elif command == "unregister":
        if user not in parking:
            print(f"ERROR: user {user} not found")
            continue
        parking.pop(user)
        print(f"{user} unregistered successfully")

for key, value in parking.items():
    print(f"{key} => {value}")
