def perfect_number(n):
    result = 0
    for x in range(1, n):
        if n % x == 0:
            result += x

    if result == n:
        return f"We have a perfect number!"
    else:
        return f"It's not so perfect."


number = int(input())
print(perfect_number(number))
