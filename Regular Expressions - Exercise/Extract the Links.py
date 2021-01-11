import re

pattern = r"(^|(?<=\s))w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+"
line = input()

while line:
    for el in re.finditer(pattern, line):
        print(el.group())

    line = input()
