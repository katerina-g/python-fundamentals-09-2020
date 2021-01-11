line = input().split()

str_1 = line[0]
str_2 = line[1]

min_len = min(len(str_1), len(str_2))

total = 0

for i in range(min_len):
    result = ord(str_1[i]) * ord(str_2[i])
    total += result

biggest_word = str_1
if len(str_2) > len(str_1):
    biggest_word = str_2

for i in range(min_len, len(biggest_word)):
    total += ord(biggest_word[i])

print(total)