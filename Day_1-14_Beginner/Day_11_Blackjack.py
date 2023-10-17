import random

from Art.Day_11_Art import logo


cards = [{'Ace': 11}, {'Two': 2}, {'Three': 3}, {"Four": 4}, {"Five": 5}, {'Six': 6}, {'Seven': 7},
         {"Eight": 8}, {"Nine": 9}, {"Ten": 10}, {"Jack": 10}, {"Queen": 10}, {"King": 10}]


def print_lines():
    print(f"-----------------------------------------------------------------------------")


def deal_card(n=1):
    result = []
    for i in range(n):
        card = random.choice(cards)
        result.append(card)

    return result


def calculate_score(hand: list):

    score = 0
    for item in hand:
        for key in item:
            if key == 'Ace':
                if score > 10:
                    score += 1
                else:
                    score += item[key]
            else:
                score += item[key]
    return score


def winner(your_score, casino_score):

    if your_score > 21 and casino_score > 21:
        print(f"Draw!")
    elif your_score > 21 and casino_score < 21:
        print("Casino Win!")
    elif your_score < 21 and casino_score > 21:
        print('You win!')
    elif your_score > casino_score:
        print('You win!')
    elif casino_score > your_score:
        print('Casino win !')
    elif casino_score == your_score:
        print('Draw')


def check_casino_hand(hand: list):
    score = calculate_score(hand)
    if score < 17:
        hand.extend(deal_card())
    return hand


def black_jack():
    print(logo)
    your_hand = deal_card(n=2)
    casino_hand = deal_card()
    print(f"Your cards: {your_hand}")
    print(f"Computer's first card: {casino_hand}")

    terminated = False
    while terminated is False:
        loop = input(f"Type 'y' to get another card, type 'n' to pass: ")
        if loop == 'y':
            your_hand.extend(deal_card())
            print(f"Your cards: {your_hand}")
        else:
            casino_hand.extend(deal_card())
            check_casino_hand(casino_hand)
            print_lines()
            your_score = calculate_score(your_hand)
            casino_score = calculate_score(casino_hand)
            print(f"Your final hand: {your_hand} - {your_score}")
            print(f"Casino final hand: {casino_hand} - {casino_score}")
            winner(your_score, casino_score)
            print_lines()

            option = input(f"Do you want to create a new game? Type 'y' or 'n' ")
            if option == 'y':
                black_jack()
            else:
                terminated = True


black_jack()
