#Blackjack game
import random
from art import logo
#from replit import clear
import os

#deals a random card from a list of cards
def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = random.choice(cards)
    return card


#Caluculates the score of the given list of cards
def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


#Compares the scores of both players and checks if there is a winner
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over 21. You lose. :-("

    if user_score == computer_score:
        return "It's a draw. -_-"
    elif computer_score == 0:
        return "The computer has Blackjack! You lose. :-("
    elif user_score == 0:
        return "You have Blackjack! You win! :-D"
    elif user_score > 21:
        return "You went over 21. You lose. :-("
    elif computer_score > 21:
        return "The computer went over 21! You win! :-D"
    elif user_score > computer_score:
        return "You win! :-D"
    else:
        return "You lose. :-("


#Plays the game
def play_game():
    print(logo)

    #Create lists for user and computer cards
    user_cards = []
    computer_cards = []
    is_game_over = False

    #Deals two random cards to each player
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #plays user's turn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal.lower() == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

        #makes computer take another card if score is below 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    #compares final scores
    print(f"  Your final hand: {user_cards}, your final score: {user_score}")
    print(
        f"  Computer's final hand: {computer_cards}, final score: {computer_score}"
    )
    print(compare(user_score, computer_score))


#Asks if the player would like to start a new game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower(
) == 'y':
   # clear()
    os.system('cls')
    play_game()