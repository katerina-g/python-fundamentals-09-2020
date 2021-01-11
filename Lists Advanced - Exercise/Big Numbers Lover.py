line_of_numbers = input().split()

sort_num = sorted(line_of_numbers, reverse=True)

result = ''.join(sort_num)
print(result)


