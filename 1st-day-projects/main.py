import random as rd
from art import logo

def deal_card():
    """"Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = rd.choice(cards)
    return card

def calculate_score(ls):
    """ This is going to take a list of cards return the score calculated from the cards"""
    if len(ls) == 2 and sum(ls) == 21:
        return 0
    if sum(ls) > 21 and 11 in ls:
        ls.remove(11)
        ls.append(1)
    return sum(ls)

def compare(u_socre, c_score):
    if u_socre == c_score:
        return "Draw "
    elif c_score == 0:
        return "Lose, opponent has Blackjack "
    elif c_score == 0:
        return "Win with a Blackjack!:)"
    elif u_socre > 21:
        return "You went over. You lose ):"
    elif c_score > 21:
        return "Opponent went over. You win:)"
    elif u_socre > c_score:
        return "User Win:)"
    else:
        return "You lose"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score {user_score}")
        print(f"Computer's first cards: {computer_cards}")

        if user_score ==0 or computer_score == 0 or user_score>21:
            is_game_over = True

        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
    print("\n"*20)
    play_game()