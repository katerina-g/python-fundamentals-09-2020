str_of_num = input().split()

numbers = []

for num in str_of_num:
    numbers.append(int(num))

remover = int(input())

for _ in range(remover):
    numbers.remove(min(numbers))

print(numbers)
