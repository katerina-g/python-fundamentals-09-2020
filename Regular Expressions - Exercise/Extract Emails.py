import re

pattern = r"(^|\s)([a-z0-9]+[a-z0-9._-]+)@([a-zA-Z0-9-]+)\.([a-zA-Z0-9.]+)\b"
text = input()

matches = re.finditer(pattern, text)
for match in matches:

    print(match.group())
