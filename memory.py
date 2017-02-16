# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global num1, exposed ,card_list, click, card_list1, swich
    num1 = range(8)
    num2 = range(8)
    num1.extend(num2)
    random.shuffle(num1)
    exposed = range(16)
    click = 0
    label.set_text("Turns = " + str(click))
    swich = 0

    exposed = []
    for i in range(16):
        exposed.append (False)
    global state
    state = 0

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed ,card_list, click, card_list1,loc1, loc2,num1,swich
    pos2 = pos[0] / 50


    
    global state
    
    if state == 0:
        state = 1
        for i in range(16):
            if pos2 == i:
                if exposed[i] == False :
                   exposed[i] = True
                   loc1 = i
                   click += 1
                   label.set_text("Turns = " + str(click)) 

    elif state == 1:
        state = 2
        for i in range(16):
            if pos2 == i:
               if exposed[i] == True :
                    state = 1
               if exposed[i] == False :
                   exposed[i] =  True
                   loc2 = i 
                   click += 1
                   label.set_text("Turns = " + str(click)) 
                   if num1[loc2] != num1[loc1]:
                        swich = 1

                 
    else:
        state = 1

        for i in range(16):
            if pos2 == i:
                if exposed[i] == True :
                    state = 2
                if exposed[i] == False :
                   if swich == 1:
                      exposed[loc1] = False
                      exposed[loc2] = False
                   swich = 0
                   exposed[i] = True
                   loc1 = i
                   click += 1
                   label.set_text("Turns = " + str(click))
 

        
    
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

    
                                                            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global num1 , card_list, exposed
    for i in range(16):
       canvas.draw_text(str(num1[i]), (10 + i * 50, 70), 80, 'Red')
    
    for i in range(16):
        if exposed[i] == False:
            canvas.draw_polygon([[50*i, 0], [50*i, 100], [50*(i+1), 100], [50*(i+1), 0]], 6, 'black','green')       
        if exposed[i] == True:
            canvas.draw_text(str(num1[i]), (10 + i * 50, 70), 80, 'Red')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns =  0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric