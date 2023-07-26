import random

card_value = {
         '2':2,
         '3':3,
         '4':4,
         '5':5,
         '6':6,
         '7':7,
         '8':8,
         '9':9,
         '10':10,
         'J':10,
         'Q':10,
         'K':10,
         'A':11}
         
#create a deck of cards
def create_deck():
    deck = []
    for suit in  ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
        for value in card_value:
            deck.append(value + ' of ' + suit)
    random.shuffle(deck)
    return deck

#deal the inital hand two cards
def initial_hand(deck):
    hand = [deck.pop(), deck.pop()]
    return hand

#def a function to calculate value of hand
def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        card_rank = card.split()[0]  # Get the rank of the card
        value += card_value[card_rank]
        if card_rank == 'A':
            num_aces += 1
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    return value


#define players turn
def player_turn(deck, player_hand):
     while True:
          print(f"Player`s hand: {', '.join(player_hand)} and the value is: {calculate_hand_value(player_hand)}")
          choice = input("Do you want to hit or stand?(h/s): ")
          if choice.lower() == 'h':
               player_hand.append(deck.pop())
               if calculate_hand_value(player_hand)>21:
                    print(f"Player busts! Dealer wins! Your value is {calculate_hand_value(player_hand)}")
                    return False
          elif choice.lower() == 's':
               return True
          else:
               print("Invalid input. Please enter 'h' or 's'.")

#define dealer turn
def dealer_turn(deck, dealer_hand):
     while calculate_hand_value(dealer_hand) < 17:
          dealer_hand.append(deck.pop())
     print(f"Dealer`s hand: {','.join(dealer_hand)}")
     print(f"Dealer`s hand value:{calculate_hand_value(dealer_hand)}")
     if calculate_hand_value(dealer_hand) > 21:
          print("Dealer busts! Player wins!")
          return False
     return True

#define starting ammount
def starting_ammount():
    ammount= int(input("Place starting ammount: "))
    print(f"You have: {ammount}")
    return ammount

    
    
                              

#define placing a bet
def place_bet(balance):
     while True:
        try:
            bet_amount = int(input("Place your bet: $"))
            if bet_amount <= 0:
                print("Invalid bet amount. Amount must be greater than zero.")
            elif bet_amount > balance:
                 print("Insufficient funds")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid bet amount.")

     return bet_amount

    

    

#define game
def play_game(balance, bet_amount):
    deck = create_deck()
    player_hand = initial_hand(deck)
    dealer_hand = initial_hand(deck)

    first_card = dealer_hand[0]
    print(f"Dealer shows their first card: {first_card} (Value: {card_value[first_card.split()[0]]})")

    if calculate_hand_value(player_hand) == 21:
        print("Player has blackjack!")
        return False, bet_amount

    if player_turn(deck, player_hand):
        if dealer_turn(deck, dealer_hand):
            player_value = calculate_hand_value(player_hand)
            dealer_value = calculate_hand_value(dealer_hand)
            if player_value > dealer_value:
                print("Player wins!")
                balance += bet_amount
            elif player_value < dealer_value:
                print("Dealer wins!")
                balance -= bet_amount
            else:
                print("It's a tie!")

    print(f"Current balance: ${balance}")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == 'y':
        return True, balance
    else:
        print("Thank you for playing!")
        return False, balance

# Main function
def main():
    print("Welcome to Blackjack!")
    balance = starting_ammount()  # Get the starting balance
    while balance > 0:
        print(f"Current balance: ${balance}")
        bet_amount = place_bet(balance)
        balance -= bet_amount
        play_again, balance = play_game(balance, bet_amount)
        if not play_again:
            break
    else:
        print("Insufficient balance. Game over.")

# Run the program
if __name__ == "__main__":
    main()
