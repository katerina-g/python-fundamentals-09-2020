import re
text = input()
word = input()

pattern = rf'\b{word}\b'
res = re.findall(pattern, text, flags=re.IGNORECASE)
print(len(res))
