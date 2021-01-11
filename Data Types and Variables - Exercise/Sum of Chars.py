n = int(input())
sum_of_chr = 0
for i in range(1, n + 1):
    character = input()
    sum_of_chr += ord(character)

print(f"The sum equals: {sum_of_chr}")