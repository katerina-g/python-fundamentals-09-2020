import re

pattern = r"\d+"

while True:
    data = input()
    if not data:
        break
    else:
        numbers = re.findall(pattern, data)
        for n in numbers:
            print(n, end=" ")
