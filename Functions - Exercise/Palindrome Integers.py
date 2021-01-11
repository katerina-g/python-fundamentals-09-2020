def palindrome_numbers(text):
    counter = len(text) // 2
    is_palindrome = True

    for i in range(counter):
        second_index = len(text) - 1 - i
        if text[i] != text[second_index]:
            is_palindrome = False
            break

    return is_palindrome


def solution(items):
    for item in items:
        print(palindrome_numbers(item))


list_of_int = input().split(", ")
solution(list_of_int)




