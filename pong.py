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
ball_vel = [1,3]
score1 = 0
score2 = 0
D = "right"
paddle1_pos = 200
paddle1_vel = 0
paddle2_pos = 200
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [1,3]
    
    if direction == "right" :
        ball_vel = [-random.randrange(5,7),random.randrange(-7,7)]
    elif direction == "left" :
        ball_vel = [random.randrange(5,7),random.randrange(-7,7)]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel ,Gstart  # these are numbers
    global score1, score2  # these are ints
    
    spawn_ball( D )
    Gstart = 1

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,Gstart, D, speed , paddle1_vel , paddle2_vel 
    
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "0099CC")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "0099CC")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "0099CC")
       
    # update ball
    
    if Gstart == 0:
        new_game()
    
    elif Gstart == 1:
           
        #if ball_pos[1] <= HEIGHT - BALL_RADIUS and ball_pos[1] >= 0 + BALL_RADIUS:
            
        ball_pos[0] = ball_pos[0] + ball_vel[0] 
        ball_pos[1] = ball_pos[1] + ball_vel[1] 
            
        if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS :
             if ball_pos[1] >= paddle1_pos - BALL_RADIUS and ball_pos[1] <= paddle1_pos + PAD_HEIGHT + BALL_RADIUS:
                ball_pos[1] = ball_pos[1] + ball_vel[1] 
                ball_vel[0] = -  ball_vel[0]*1.1
                ball_pos[0] = ball_pos[0] + ball_vel[0] 

                
        if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH :
             if ball_pos[1] >= paddle2_pos - BALL_RADIUS and ball_pos[1] <= paddle2_pos + PAD_HEIGHT + BALL_RADIUS:
                ball_pos[1] = ball_pos[1] + ball_vel[1] 
                ball_vel[0] = -  ball_vel[0]*1.1
                ball_pos[0] = ball_pos[0] + ball_vel[0]    
                
        if ball_pos[1] > HEIGHT - BALL_RADIUS :
            ball_pos[0] = ball_pos[0] + ball_vel[0] 
            ball_vel[1] = -  ball_vel[1]
            ball_pos[1] = ball_pos[1] + ball_vel[1] 
            
        if ball_pos[1] < 0 + BALL_RADIUS :
            ball_pos[0] = ball_pos[0] + ball_vel[0] 
            ball_vel[1] = -  ball_vel[1]
            ball_pos[1] = ball_pos[1] + ball_vel[1] 
         

                
        
        
        if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
            Gstart = 0 
            D = "right"
            score1 +=1
            ball_pos[0] = WIDTH - BALL_RADIUS - PAD_WIDTH
            
        if ball_pos[0] <= 0 + BALL_RADIUS + PAD_WIDTH:
            Gstart = 0 
            score2 +=1 
            D = "left"
            ball_pos[0] = 0 + BALL_RADIUS + PAD_WIDTH
        
    
    print ball_pos
        
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 4, "#FFCC00", "White") 
    
    # update paddle's vertical position, keep paddle on the screen
    
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    if PAD_HEIGHT + paddle1_pos >= HEIGHT:
        paddle1_pos = HEIGHT - PAD_HEIGHT
    elif paddle1_pos <= 0 :
        paddle1_pos = 0
        
    if PAD_HEIGHT + paddle2_pos >= HEIGHT:
        paddle2_pos = HEIGHT - PAD_HEIGHT
    elif paddle2_pos <= 0 :
        paddle2_pos = 0
        
    # draw paddles
    canvas.draw_polygon([(0, paddle1_pos), (PAD_WIDTH/2, paddle1_pos), (PAD_WIDTH/2, PAD_HEIGHT + paddle1_pos), (0, PAD_HEIGHT + paddle1_pos)], 12, '0099CC')
    canvas.draw_polygon([(WIDTH - PAD_WIDTH/2, paddle2_pos), (WIDTH, paddle2_pos), (WIDTH, PAD_HEIGHT + paddle2_pos), (WIDTH - PAD_WIDTH/2, PAD_HEIGHT + paddle2_pos)], 12, '0099CC')
    
    # draw scores
    canvas.draw_text(str(score1), [150, 50], 32, "0099CC")
    canvas.draw_text(str(score2), [450, 50], 32, "0099CC")


    
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos

    
    if key == simplegui.KEY_MAP["s"]:
       paddle1_vel = 5
    if key == simplegui.KEY_MAP["down"]:
       paddle2_vel = 5  
        
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -5
    if key == simplegui.KEY_MAP["up"]:
       paddle2_vel = -5
   
def keyup(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos

    
    if key == simplegui.KEY_MAP["s"]:
         paddle1_vel = 0  
    if key == simplegui.KEY_MAP["down"]:
         paddle2_vel = 0    
        
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"]:
         paddle2_vel = 0

  
def reset_game():
    global swich , score1, score2

    score1 = 0
    score2 = 0
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_canvas_background('White')

frame.add_button("Reset",reset_game, 100)


# start frame
new_game()
frame.start()
