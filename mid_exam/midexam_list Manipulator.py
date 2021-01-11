friends = input().split(", ")
count_lost = 0
count_blacklisted = 0
command = input()
while not command == "Report":
    command = command.split()
    if command[0] == "Blacklist":
        name = command[1]
        if name in friends:
            name_ind = friends.index(name)
            friends[name_ind] = "Blacklisted"
            count_blacklisted += 1
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")
    elif command[0] == "Error":
        index = int(command[1])
        for name in friends:
            name_ind = friends.index(name)
            if name != "Blacklisted" and name != "Lost" and name_ind == index:
                friends[name_ind] = "Lost"
                count_lost += 1
                print(f"{name} was lost due to an error.")
    elif command[0] == "Change":
        index = int(command[1])
        new_name = command[2]
        for name in friends:
            name_ind = friends.index(name)
            if index == name_ind:
                friends[name_ind] = new_name
                print(f"{name} changed his username to {new_name}.")
                break
    command = input()
print(f"Blacklisted names: {count_blacklisted}")
print(f"Lost names: {count_lost}")
print(" ".join(friends))
