# "Stopwatch: The Game"

# define global variables
import random
import simplegui
import time
sys_text = "New Game starts!"
sys_time = 0
swich = 1 
tmp = 0 
win = 0 

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
      d = t % 10
      c = ((t % 600) / 10) % 10
      b = ((t % 600) / 10) / 10  
      a = int(t) / 600 
      time_m = str(a) + ":" + str(b) + str(c) + ":" + str(d)
      return time_m

       
# define event handlers for buttons; "Start", "Stop", "Reset"
## helper function to start and restart the game
def new_game():    
   # print "New Game starts!"
    global sys_text,  sys_time, swich
    sys_text = "New Game starts!"
    sys_time = 0
    swich = 0 


## helper function to stop the game 
def stop_game():
    #print "New Game Stops!"
    global sys_text, sys_time, swich , tmp , win 
    sys_text = "     Game Stops!  "
    sys_time = sys_time
    swich = 1 
    tmp = tmp + 1
    
    if format(sys_time)[5] == "0":
        win = win + 1
    
    
## helper fucntion to reset the game 
def reset_game():
    #print "New Game Resets!"
    global sys_text, sys_time, swich, tmp, win
    sys_text = "         Resets!     "
    sys_time = 0 
    swich = 1 
    tmp = 0
    win = 0

    
# define event handler for timer with 0.1 sec interval
def timer_handler():
  global sys_time 
  if swich == 0 :
        sys_time = sys_time + 1
  elif swich == 1:
        sys_time = sys_time
       

# define draw handler
def draw(canvas):
    canvas.draw_text(format(sys_time), [80, 130], 60, '#FFCC00')
    canvas.draw_text(str(tmp), [210, 250], 32, "0099CC")
    canvas.draw_text("/", [245, 250], 32, "0099CC")
    canvas.draw_text(str(win), [270, 250], 32, "0099CC")
    
# create frame
f = simplegui.create_frame("Timer",300,300)

# register event handlers
f.set_canvas_background('White')
f.add_button("Start",new_game, 100)
f.add_button("Stop", stop_game, 100)
f.add_button("Reset",reset_game, 100)
f.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)

# start frame
f.start()
timer.start()
# Please remember to review the grading rubric