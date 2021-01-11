user_names = input().split(", ")

for name in user_names:
    if not 3 <= len(name) <= 16:
        continue

    is_valid = True

    for ch in name:
        if not (ch.isalnum() or ch == "-" or ch == "_"):
            is_valid = False
            break
    if not is_valid:
        continue

    print(name)
