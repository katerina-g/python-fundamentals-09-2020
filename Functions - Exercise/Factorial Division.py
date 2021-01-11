def factorial_num(n_1, n_2):
    fact_1 = 1
    fact_2 = 1
    for num_1 in range(n_1, 0, -1):
        fact_1 *= num_1

    for num_2 in range(n_2, 0, -1):
        fact_2 *= num_2

    return fact_1 / fact_2


number_1 = int(input())
number_2 = int(input())
print(f"{factorial_num(number_1, number_2):.2f}")








