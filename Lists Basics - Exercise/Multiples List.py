factor = int(input())
count = int(input())
multiples = factor * count
multiples_list = []

for num in range(factor, multiples + 1, factor):
    multiples_list.append(num)
print(multiples_list)
