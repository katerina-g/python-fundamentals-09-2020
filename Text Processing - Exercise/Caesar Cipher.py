text = input()

for ch in text:
    new = ord(ch) + 3
    print(chr(new), end='')
