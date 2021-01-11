import math

numbers = list(map(int, input().split(", ")))

max_number = max(numbers)
groups_number = math.ceil(max_number / 10)

for i in range(1, groups_number + 1):
    upper = i * 10
    lower = upper - 10
    current = [n for n in numbers if lower < n <= upper]

    print(f"Group of {i * 10}'s: {current}")

