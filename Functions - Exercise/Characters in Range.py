def character_in_range(c_1, c_2):
    a = ord(c_1)
    b = ord(c_2)
    for i in range(a + 1, b):
        print(chr(i), end=" ")


chr_1 = input()
chr_2 = input()

character_in_range(chr_1, chr_2)

