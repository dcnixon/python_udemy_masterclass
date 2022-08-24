card_names = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]


card_values = {}


# create dictionary of the card values dictionary with A as 11 and 1 as 1
for card_name in card_names:
    card_name = str(card_name)
    if card_name == "A":
        card_values[card_name] = 11
    elif card_name.isnumeric():
        card_values[card_name] = int(card_name)
    else:
        card_values[card_name] = 10


# simple sum of the cards in the hand

# find the best total for a list of cards
# changes A==11 to '1'==1 if over 21 and recalculate
#
def blackjack_hand_total(hand: list):
    """Calculate the blackjack value for a list of cards"""

    for i in range(len(hand) + 1):
        hand_total = sum([card_values[card] for card in hand])
        if hand_total <= 21 or "A" not in hand:
            return hand_total

        if hand[i] == "A":
            hand[i] = "1"


# Compare the two hands
def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.

    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21

    Hands are represented as a list of cards. Each card is represented by a string.

    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.

    When determining a hand's total, you should try to count aces in the way that
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.

    Examples:
    blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    blackjack_hand_greater_than(['K'], ['10'])
    False
    blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    hand_1_total = blackjack_hand_total(hand_1)
    hand_2_total = blackjack_hand_total(hand_2)
    if hand_1_total > 21:
        return False
    elif hand_2_total > 21 or hand_2_total < hand_1_total:
        return True
    else:
        return False


print(blackjack_hand_greater_than(['K'], ['3', '4']))
print(blackjack_hand_greater_than(['K'], ['10']))
print(blackjack_hand_greater_than(['K', 'K', '2'], ['3']))