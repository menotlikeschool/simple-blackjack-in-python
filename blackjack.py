import random

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

def deal_card():
    """Return a random card."""
    return random.choice(cards)

def calculate_score(hand):
    """Calculate the score of a hand."""
    score = sum(values[card] for card in hand)

    if score > 21 and 'A' in hand:
        aces = hand.count('A')
        while score > 21 and aces:
            score -= 10
            aces -= 1
    return score

def compare(player_score, dealer_score):
    """Determine the winner."""
    if player_score > 21:
        return "You went over. You lose!"
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif player_score > dealer_score:
        return "You win!"
    elif player_score < dealer_score:
        return "You lose!"
    else:
        return "Draw!"

def play_blackjack():
    print("Welcome to Blackjack!")

    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if player_score == 21 or dealer_score == 21 or player_score > 21:
            game_over = True
        else:
            action = input("Type 'hit' to get another card, 'stand' to pass: ").lower()
            if action == 'hit':
                player_hand.append(deal_card())
            else:
                game_over = True

    while dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))

play_blackjack()
