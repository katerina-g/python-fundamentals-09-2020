divisor = int(input())
bound = int(input())
max_num = 0
for n in range(divisor, bound + 1):
    if n % divisor == 0 and bound >= n > 0 and n > max_num:
        max_num = n
print(max_num)