'''
Blackjack
'''
import random
import time

DECK = {
    "A": 1, # Count all Aces as 1, if the current hand
            # total is 11 and there is an ace, ad 10 and quit
    "K": 10,
    "Q": 10,
    "J": 10,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10
}

def draw_random():
    """ Draw a random card from the deck and return it in a tuple
        in the form (face, value)"""
    face = random.choice(list(DECK.keys()))
    value = DECK[face]
    return (face, value) # return tuple representing the card

def total_hand(cards):
    """ Return the sum of all cards in a list """
    return sum(card[1] for card in cards)

def determine_aces(cards):
    """ Determine the final value of ACE (A) cards
        You only want an ACE to be valued at 11 if the current
        value of your hand is <= 11 with that ACE valued at 1
    """
    c_total = total_hand(cards)
    if 'A' in [c[0] for c in cards] and c_total <= 11:  # is there an ACE and are we <= 11
        for i in range(0, len(cards)):  # find the ACE, change its value from 1 to 11                  
            face = cards[i][0]
            if face is 'A':
                cards[i] = (face, 11) # change the ace value to 11
                break
        return cards # returned modified cards
    else:
        return cards # return unmodified cards (no aces found)
    
def run():
    # start game
    dealer = []
    player = []
    dealer.append(draw_random()) # dealer card 1
    dealer.append(draw_random()) # dealer card 2
    player.append(draw_random()) # player card 1
    player.append(draw_random()) # player card 2
    print('The dealer drew two cards, HIDDEN and ' + dealer[0][0]) # print dealer first card
    print('The dealer delt you two cards, ' + player[0][0] + ' and ' + player[1][0]) # print dealer first card

    # player plays
    player_total = total_hand(player)
    while player_total <= 21: # allow player to keep drawing
        hit = True if input('Hit? (Y/N): ') is 'Y' else False
        if hit:
            face, value = draw_random()
            print('You drew: ' + face)
            player.append((face, value)) # put the card in a tuple and append
            player_total = total_hand(player) # new total
            print('Your cards are {}'.format(str([card[0] for card in player])))
        else:
            break # chose not to hit

    # determine player final hand
    player = determine_aces(player)
    player_total = total_hand(player)
    print('Your final cards are {} for a total of {}'.format(str([card[0] for card in player]), str(player_total)))

    # dealer Plays
    dealer_total = total_hand(dealer)
    print('Dealer cards are {}'.format(str([card[0] for card in dealer])))
    while dealer_total < 21: # dealer stops at 21
        time.sleep(1) # pause for a little suspense
        if dealer_total == 16 or (dealer_total < player_total and player_total <= 21):
            print('Dealer hit!')
            time.sleep(2) # pause for a little suspense
            face, value = draw_random()
            print('Dealer drew: ' + face)
            dealer.append((face, value))
            dealer = determine_aces(dealer)
            dealer_total = total_hand(dealer)
            print('Dealer cards are {}'.format(str([card[0] for card in dealer])))
        elif dealer_total == 17:
            print('Dealer has to stay')
            break # has to stay
        else:
            print('Dealer has chosen to stay')
            break # chose to stay

    # show dealer final hand
    print('Dealer final cards are {} for a total of {}'.format(str([card[0] for card in dealer]), str(dealer_total)))

    # End game, determine winner
    print('END OF GAME')
    if (player_total > dealer_total and player_total <= 21) or dealer_total > 21:
        print('You WON!')
    elif (player_total < dealer_total and dealer_total <= 21) or player_total > 21:
        print('House WON!')
    else:
        print('Tie! Push!')        


# Main Game Loop
play = True
while play:
    run()
    play = True if input('Play again? (Y/N): ') is 'Y' else False
        
