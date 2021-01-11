def integer_numbers(n_1, n_2, n_3):
    smallest_number = min(n_1, n_2, n_3)
    return smallest_number


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(integer_numbers(number_1, number_2, number_3))

