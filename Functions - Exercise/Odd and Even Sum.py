def sum_of_digits(str_number):
    even_sum = 0
    odd_sum = 0

    for ch in str_number:
        num = int(ch)

        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return f" Odd sum = {odd_sum}, Even sum = {even_sum}"


str_num = input()
print(sum_of_digits(str_num))



