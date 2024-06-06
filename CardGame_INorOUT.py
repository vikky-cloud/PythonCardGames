import random
import string

# Function to create and shuffle a deck of cards
def create_deck():
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# Function to distribute cards to players
def distribute_cards(deck, num_players):
    hands = [[] for _ in range(num_players)]
    for _ in range(2):  # Distribute 2 cards to each player
        for i in range(num_players):
            card = deck.pop()
            hands[i].append(card)
    return hands

# Function to check if the third card value is between the first two cards
def check_third_card(card1, card2, third_card):
    values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    value1 = values[card1['rank']]
    value2 = values[card2['rank']]
    value3 = values[third_card['rank']]
    return value1 < value3 < value2 or value2 < value3 < value1

# Function to play the game
def play_game():
    while True:
        try:
            num_players = int(input("Enter the number of players: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if num_players < 2:
            print("Minimum 2 players required.")
            continue
        else:
            break

    player_names = []
    for i in range(num_players):
        while True:
            name = input(f"Enter the name of player {i+1}: ").strip()
            if all(char.isalpha() or char.isspace() for char in name):
                player_names.append(name)
                break
            else:
                print("Please enter valid name with alphabets only.")

    deck = create_deck()
    hands = distribute_cards(deck, num_players)
    results = []

    for i in range(num_players):
        print(f"\n{player_names[i]}, here are your cards:")
        for card in hands[i]:
            print(f"{card['rank']} of {card['suit']}")

        third_card = deck.pop()
        while True:
            choice = input("Third card: In or Out? ").strip().lower()
            if choice in ['in', 'out']:
                break
            else:
                print("Please enter 'In' or 'Out'.")

        if (choice == 'in' and check_third_card(hands[i][0], hands[i][1], third_card)) or (choice == 'out' and not check_third_card(hands[i][0], hands[i][1], third_card)):
            results.append(f"{player_names[i]} won! Third card was {third_card['rank']} of {third_card['suit']}")
        else:
            results.append(f"{player_names[i]} lost. Third card was {third_card['rank']} of {third_card['suit']}")

    print("\nResults:")
    for result in results:
        print(result)

    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thanks for playing!")

# Play the game
play_game()
