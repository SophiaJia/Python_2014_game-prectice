# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':100, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
# Student should insert code for Hand class here
class Hand:
    def __init__(self):
        self.hand = []	# create Hand object

    def __str__(self):
        # return a string representation of a hand
        self.ans = ""
        for i in range(len(self.hand)):
            self.ans += str(self.hand[i])+" "
        return self.ans
    
    def add_card(self, card):
        self.hand.append (card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        self.hand_value = 0 # compute the value of the hand, see Blackjack video
        for card in self.hand:
            self.hand_value += VALUES[card.get_rank()] 
        if self.hand_value < 100 :
            return self.hand_value
        else :
            if self.hand_value + 10 - (self.hand_value // 100) * 99 <= 21 :
                return self.hand_value + 10 - (self.hand_value // 100) * 99
            else :
                return self.hand_value - (self.hand_value // 100) * 99
              
                             
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        
        for c in self.hand:
            c.draw(canvas,pos)
            pos[0] += CARD_SIZE[0]
                                            
# define deck class 
class Deck:
    def __init__(self):
        self.deck = [] # create a Deck object
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append (Card(suit, rank))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
        self.card = self.deck [-1]# deal a card object from the deck
        self.deck.remove (self.card)
        return self.card
        
    def __str__(self):
            # return a string representing the deck
        self.ans = "Deck contains : "
        for i in range(len(self.deck)):
            self.ans += str(self.deck[i])+" "
        return self.ans
        
#define event handlers for buttons
def deal():
    global outcome, in_play, New_deck, p_hand , d_hand , outcome, p_value, d_value,showcard, hint, score

    # your code goes here
    New_deck = Deck()
    New_deck.shuffle()
    
    p_hand = Hand() # player 
    d_hand = Hand() # dealer
    p_hand.add_card(New_deck.deal_card())
    d_hand.add_card(New_deck.deal_card())
    p_hand.add_card(New_deck.deal_card())
    d_hand.add_card(New_deck.deal_card())
    p_value = p_hand.get_value()
    d_value = d_hand.get_value()
    
    if in_play == True :
        score -= 1
    

    outcome = " "
    showcard = False
    hint = "Hit or Stand ?"
    in_play = True

def hit():
    # replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
    global outcome, in_play, New_deck, p_hand , d_hand ,score, p_value, d_value,showcard, hint
    
    if in_play == True:
        p_hand.add_card(New_deck.deal_card())
        p_value = p_hand.get_value()
        hint = "Hit or Stand ?"
        if p_hand.get_value() > 21 :
            outcome = " You are BUSTED "
            hint = "New deal ?  "
            in_play = False
            score -= 1
            showcard = True

       
def stand():
    # replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
    global outcome, in_play, New_deck, p_hand , d_hand ,score , p_value, d_value ,showcard, hint
    if in_play == True:
        while d_hand.get_value() < 17 :
            d_hand.add_card(New_deck.deal_card())
            d_value = d_hand.get_value()
        if d_hand.get_value() > 21 :
            outcome = "Dealer Bust, You Win "
            hint = "New deal ? "
            showcard = True
            in_play = False
            score += 1
        else:
            if d_hand.get_value() >= p_hand.get_value():
                outcome = "You Lose"
                hint = "New deal ?  "
                showcard = True
                in_play = False
                score -= 1
            else: 
                outcome = "You Win"
                hint = "New deal ?  "
                showcard = True
                in_play = False
                score += 1   

               

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    p_hand.draw(canvas, [100, 370])
    d_hand.draw(canvas, [100, 120])
    if showcard == False :
        canvas.draw_polygon([[100, 120], [100 + CARD_SIZE[0], 120], [100 + CARD_SIZE[0], 120 + CARD_SIZE[1]], [100, 120 + CARD_SIZE[1]]], 1, 'Red', 'white')
    
    canvas.draw_text(outcome, [150,550], 30, "White")
    canvas.draw_text(str(hint), [300,350], 30, "White")
    canvas.draw_text("Blackjack", [50,50], 30, "White")
    canvas.draw_text("Score : " + str(score), [450,50], 30, "White")
    
    #canvas.draw_text(str(p_value), [200,350], 30, "White")
    #canvas.draw_text(str(d_value), [200,100], 30, "White")
    
    canvas.draw_text("Dealer", [100,100], 30, "White")
    canvas.draw_text("Player", [100,350], 30, "White")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric