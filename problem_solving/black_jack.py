if __name__ == "__main__":
    card_count, max_num = list(map(int, input().split(' ')))
    card_list = list(map(int, input().split(' ')))

    card_sum = 0
    length = len(card_list)

    for card1 in range(0, length):
        for card2 in range(card1 + 1, length):
            for card3 in range(card2 + 1, length):
                temp_card_sum = card_list[card1] + card_list[card2] + card_list[card3]

                if temp_card_sum <= max_num:
                    card_sum = max(card_sum, temp_card_sum)

    print(card_sum)
