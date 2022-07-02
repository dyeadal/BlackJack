import random

def createDeck():
    deck = []
    for x in range(6):
        deck += ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    return deck

def pickCard(array):
    chosenNum = random.randint(0, len(array))
    card = "ZZZ"
    while array[chosenNum] != "X":
        card = array[chosenNum]
        array[chosenNum] = "X"
    return card

def countHand():
    hand = 0
    return hand

def createHand():
    emptyArray = []
    return emptyArray

def newHands(deck):
    hand = createHand()
    hand.append(pickCard(deck))
    hand.append(pickCard(deck))

    return hand

def calculateHand(hand):
    x = 0
    point = [0, 0]
    while x < len(hand):
        if hand[x] == int(hand[x]):
            print("Card is Int: " + str(hand[x]))
            point[0] += hand[x]
            x += 1
        elif str(hand[x]) == "A":
            # 1 or 10
            point[1] += 1
            x += 1
        elif str(hand[x]) == "J" or "Q" or "K":
            point[0] += 10
            x += 1
        else:
            print("ERROR")
            break

    return point

def startGame():
    point = 0
    gameDeck = createDeck()

    player = newHands(gameDeck)
    dealer = newHands(gameDeck)
    print("Player's Hand:", player, calculateHand(player))
    print("Dealer's Hand:", dealer, calculateHand(dealer))
    print(gameDeck)

    return point

startGame()



