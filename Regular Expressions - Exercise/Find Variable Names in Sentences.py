import re
data = input()

pattern = r"\b_{1}[a-zA-Z]*\d*\b"

result = re.findall(pattern, data)
new = [res[1:]for res in result]
print(",".join(new))
