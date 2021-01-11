import re

pattern = r"\|([A-Z]{4,})\|:#([A-Za-z]+\s[A-Za-z]+)#"

n = int(input())

for _ in range(n):
    line = input()
    match = re.findall(pattern, line)
    if match:
        for el in match:
            name = el[0]
            prof = el[1]
            print(f"{name}, The {prof}")
            print(f">> Strength: {len(name)}")
            print(f">> Armour: {len(prof)}")
    else:
        print("Access denied!")
