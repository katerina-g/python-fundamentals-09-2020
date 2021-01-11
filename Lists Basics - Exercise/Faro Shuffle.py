cards = input().split()
num_of_shuffles = int(input())

top_card = cards[0]
bottom_card = cards[-1]

half_deck = int(len(cards) / 2)

shuffle_cards = []
for n_of_shuffle in range(num_of_shuffles):
    left_deck = []
    right_deck = []

    for index in range(1, half_deck):
        left_deck.append(cards[index])

    for index in range(half_deck, len(cards) - 1):
        right_deck.append((cards[index]))

    for index in range(len(right_deck)):
        shuffle_cards.append(right_deck[index])
        shuffle_cards.append(left_deck[index])

    cards = shuffle_cards.copy()
    shuffle_cards = []
    cards.append(bottom_card)
    cards.insert(0, top_card)

print(cards)
