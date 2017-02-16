# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console



# initialize global variables used in your code

rangenum = 0
numt = 0
tmpt = -1
import random
import simplegui


# helper function to start and restart the game
def new_game():
    # remove this when you add your code    
    print "New Game starts! Please choose the range"
    global numt, rangenum
    numt = 0
    rangenum = 1


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    
    # remove this when you add your code    
    print "The range is from 0 to 100"
    global  number_random, rangenum, tmpt
    number_random = random.randrange(0, 100)
    rangenum=100
    tmpt=7

def range1000():
    # button that changes range to range [0,1000) and restarts
    
    # remove this when you add your code    
    print "The range is from 0 to 1000"
    global  number_random , rangenum 
    pnumber_random = random.randrange(0, 1000)
    rangenum=1000
    tmpt=10
    
def input_guess(guess):
    # main game logic goes here	
    
    # remove this when you add your code 
    
    guess1 = int(guess)
    global numt
    
    if rangenum == 0:
        print "Please click the new game button "
    elif rangenum == 1:
        print "Please choose the range"
    if numt == tmpt :
        print "Sorry. You already tried", tmpt, "times. Please try another round "
        print "Please click the new game button"
    elif guess1>rangenum :
        print "Your input is",guess
        print "Your input is beyond the range please enter agian"
    elif guess1 < 0:
        print "Your input is",guess
        print "Your input should larger than 0"
    elif guess1 > number_random :
        numt +=1
        print "Your input is",guess
        print "The number should be smaller, please enter again"
    elif guess1 < number_random :
        numt +=1
        print "Your input is",guess
        print "The number should be bigger, please enter again"
    elif guess1 == number_random :
        numt +=1
        print "Your input is",guess
        print "Good Job! you win"
    else:
        print "Unknown Error"

        

    
# create frame
f = simplegui.create_frame("Guess Game",300,300)


# register event handlers for control elements
f.add_button("New Game",new_game, 100)
f.add_button("Range 0-100", range100, 100)
f.add_button("Range 0-1000",range1000, 100)

f.add_input("Input Guess", input_guess, 100)


# call new_game and start frame

f.start()

# always remember to check your completed program against the grading rubric
