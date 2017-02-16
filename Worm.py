# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_pos2 = [WIDTH / 2, HEIGHT / 2] 

ball_vel = [1,3]
score1 = 0
score2 = 0
D = "right"

paddle1_pos = ( HEIGHT - PAD_HEIGHT )/ 2
paddle2_pos = ( HEIGHT - PAD_HEIGHT )/ 2

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel , ball_pos2 # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [1,3]
    
    if direction == "right" :
        ball_vel = [-random.randrange(5,7),random.randrange(-7,7)]
        ball_pos2[0] = ball_pos[0] - 4 * ball_vel[0]
        ball_pos2[1] = ball_pos[1] - 4 * ball_vel[1]

    elif direction == "left" :
        ball_vel = [random.randrange(5,7),random.randrange(-7,7)]
        ball_pos2[0] = ball_pos[0] - 4 * ball_vel[0]
        ball_pos2[1] = ball_pos[1] - 4 * ball_vel[1]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel ,Gstart  # these are numbers
    global score1, score2  # these are ints
    
    spawn_ball( D )
    Gstart = 1

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,Gstart, D
    

        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "0099CC")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "0099CC")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "0099CC")
    canvas.draw_circle([ball_pos[0] - 5 * ball_vel[0] , ball_pos[1] - 5 * ball_vel[1] ] , 12, 1, "black", "Green")
    canvas.draw_circle([ball_pos[0] - 4 *ball_vel[0] , ball_pos[1] - 4 * ball_vel[1] ] , 14, 1, "black", "#FFCC00")
    canvas.draw_circle([ball_pos[0] - 3 * ball_vel[0] , ball_pos[1] - 3 * ball_vel[1] ] , 15, 1, "black", "Green")
    canvas.draw_circle([ball_pos[0] - 2 * ball_vel[0] , ball_pos[1] - 2 * ball_vel[1] ] , 17, 1, "black", "#FFCC00")
    canvas.draw_circle([ball_pos[0] - ball_vel[0] , ball_pos[1] - ball_vel[1] ] , 18, 1, "black", "Green")
    canvas.draw_circle(ball_pos, 18, 1, "black", "#FFCC00")   
     
    
    # update ball
    
    if Gstart == 0:
        new_game()
    
    elif Gstart == 1:
        
        if ball_pos[1] <= HEIGHT - BALL_RADIUS and ball_pos[1] >= 0 + BALL_RADIUS:
            ball_pos[0] = ball_pos[0] + ball_vel[0]
            ball_pos[1] = ball_pos[1] + ball_vel[1]

        if ball_pos[1] > HEIGHT - BALL_RADIUS :
            ball_pos[0] = ball_pos[0] + ball_vel[0]
            ball_vel[1] = -  ball_vel[1]
            ball_pos[1] = ball_pos[1] + ball_vel[1]

        if ball_pos[1] < 0 + BALL_RADIUS :
            ball_pos[0] = ball_pos[0] + ball_vel[0]
            ball_vel[1] = -  ball_vel[1]
            ball_pos[1] = ball_pos[1] + ball_vel[1]

         
        if ball_pos[0] >= WIDTH - BALL_RADIUS:
            Gstart = 0 
            D = "right"
            score1 +=1
        if ball_pos[0] <= 0 + BALL_RADIUS:
            Gstart = 0 
            score2 +=1 
            D = "left"
        
    
    print ball_pos
    
    canvas.draw_circle(ball_pos, 15, 4, "black", "Green")
    canvas.draw_circle([ball_pos[0] + 5 , ball_pos[1] +5 ], 2, 1, "white", "white")
    canvas.draw_circle([ball_pos[0] - 5 , ball_pos[1] -5 ], 2, 1, "white", "white")

        
    # draw ball

    
    # update paddle's vertical position, keep paddle on the screen
    
    
    
    # draw paddles
    canvas.draw_polygon([(0, paddle1_pos), (PAD_WIDTH, paddle1_pos), (PAD_WIDTH, PAD_HEIGHT + paddle1_pos), (0, PAD_HEIGHT + paddle1_pos)], 12, '0099CC')
    canvas.draw_polygon([(WIDTH - PAD_WIDTH, paddle2_pos), (WIDTH, paddle1_pos), (WIDTH, PAD_HEIGHT + paddle1_pos), (WIDTH - PAD_WIDTH, PAD_HEIGHT + paddle1_pos)], 12, '0099CC')
    
    # draw scores
    canvas.draw_text(str(score1), [150, 50], 32, "0099CC")
    canvas.draw_text(str(score2), [450, 50], 32, "0099CC")


    
def keydown(key):
    global paddle1_vel, paddle2_vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_canvas_background('White')

# start frame
new_game()
frame.start()
