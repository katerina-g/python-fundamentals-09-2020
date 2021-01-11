text = input()

for i in range(len(text)):
    ch = text[i]
    if i + 1 == len(text) or not ch == text[i + 1]:
        print(ch, end="")