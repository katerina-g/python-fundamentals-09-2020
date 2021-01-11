cards = input().split(", ")
n = int(input())

for i in range(n):
    command = input().split(", ")
    action = command[0]
    if action == "Add":
        card_name = command[1]
        if card_name in cards:
            print("Card is already bought")
        else:
            cards.append(card_name)
            print("Card successfully bought")
    elif action == "Remove":
        card_name = command[1]
        if card_name in cards:
            cards.remove(card_name)
            print("Card successfully sold")
        else:
            print("Card not found")
    elif action == "Remove At":
        index = int(command[1])
        if index > (len(cards)):
            print("Index out of range")
        else:
            cards.remove(cards[index])
            print("Card successfully sold")
    elif action == "Insert":
        index = int(command[1])
        card_name = command[2]
        if index > len(cards):
            print("Index out of range")
        else:
            if card_name in cards:
                print("Card is already bought")
            else:
                cards.insert(index, card_name)
                print("Card successfully bought")
print(", ".join(cards))
