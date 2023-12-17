import random
from  art import logo2
############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def add(n1, n2):
    return n1 + n2


def player():

    global dealer_hand, hand_shown, your_hand

    your_hand = []
    dealer_hand = []
    hand_shown = []

    for r in range(2):
        your_hand.append(random.choice(cards))
        dealer_hand.append(random.choice(cards))

    go = True
    total = add(your_hand[0], your_hand[1])
    for c in range(len(dealer_hand) - 1):
        hand_shown.append(dealer_hand[c])
    hand_shown.append("?")
    print(f"  Your hand: {your_hand}, Score: {total}.")
    print(f"  Dealer hand: {hand_shown}")

    if total == 21:
        return 0

    else:
        while go:
            if total < 21:
                hit = input("Type 'y' to draw another card or 'n' to pass ")
                if hit == "y":
                    your_hand.append(random.choice(cards))
                    new_total = sum(your_hand)
                    total = new_total

                    if total > 21:
                        for n in your_hand:
                            if n == 11:
                                your_hand[your_hand.index(n)] = 1
                                total = sum(your_hand)

                    if total < 21:
                        print(f"  Your hand is {your_hand}, score: {total}.")
                        print(f"  Dealer hand is {hand_shown}")

                elif hit == "n":
                    return total

            elif total == 21:
                return total

            else:
                return total


def dealer():
    total = add(dealer_hand[0], dealer_hand[1])
    if total == 21:
        return 0

    while total < 17:
        dealer_hand.append(random.choice(cards))
        new_total = sum(dealer_hand)
        total = new_total
        if total > 21:
            if 11 in dealer_hand:
                dealer_hand.remove(11)
                dealer_hand.append(1)
                total = sum(dealer_hand)
    return total


def blackjack():
    print(logo2)
    play = input("Do you want to play Blackjack: 'y' or 'n'?\n")
    if play == 'y':
        gambler = player()
        table = dealer()
        if gambler == 0:
            print(f"  Your final hand is {your_hand}, final score: {gambler}.")
            print("BLACKJACK!\nYou win")
            blackjack()
        elif gambler > 21:
            print(f"  Your final hand: {your_hand}, final score: {gambler}.")
            print("You lose")
            blackjack()
        elif table == 0:
            print(f"  Your final hand: {your_hand}, final score: {gambler}.")
            print(f"  Dealer final hand: {dealer_hand}, final score: {table}")
            print("Dealer BLACKJACK!\nYou lose")
            blackjack()
        elif gambler == table:
            print(f"  Your final hand: {your_hand}, final score: {gambler}.")
            print(f"  Dealer final hand: {dealer_hand}, final score: {table}")
            print("It is a draw")
            blackjack()
        elif table > 21:
            print(f"  Your final hand: {your_hand}, final score: {gambler}.")
            print(f"  Dealer final hand: {dealer_hand}, final score: {table}")
            print("you win")
            blackjack()
        elif gambler > table:
            print(f"  Your final hand: {your_hand}, final score: {gambler}.")
            print(f"  Dealer final hand: {dealer_hand}, final score: {table}")
            print("you win")
            blackjack()
        else:
            print(f"  Your final hand: {your_hand}, final score: {gambler}.")
            print(f"  Dealer final hand: {dealer_hand}, final score: {table}")
            print("you lose")
            blackjack()
    else:
        print('Maybe next time')


blackjack()

