text = input()
numbers_string = text.split()
numbers = []

for num_str in numbers_string:
    number = -int(num_str)
    numbers.append(number)

print(numbers)
