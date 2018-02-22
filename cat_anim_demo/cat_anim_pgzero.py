# Write your code here :-)
import time
import pygame

# The artwork for this demo was downloaded from
# https://opengameart.org/content/cat-dog-free-sprites
# I had to rename the files for pgzero to work correctly.
# It wants all lower case file names and I replaced the 
# space with an underscore and removed the parenthesis
# I also copied the files and flipped them horizontally 
# to create the left moving/facing sprites. 

WIDTH = 800
HEIGHT = 500
FPS = 30

cat_idx = 0
jump_idx = 0

facing_right = True
moving = False
jumping = False
cat = None
cat_left = 0

def fps_tick():
    global cat_idx, jump_idx, jumping
    if jumping:
        jump_idx += 1 
        if jump_idx >= 16:
            jumping = False
            jump_idx = 0
        

    cat_idx = (cat_idx + 1) % 10
    


def update():
    global cat, facing_right, cat_left, jump_idx, jumping, moving
    
	# controls how many pixels the cat moves with each update
    speed = 3 
    
	# space starts a jump
    if keyboard[keys.SPACE]:
        if not jumping:
            jumping = True
       
    if jumping:
        idx = jump_idx
		# it looks better with the jump animation moves slower
        if idx > 0: 
            idx = min(int(idx / 2), 7)
            
        if facing_right:
            cat = cat_sprite['jump'][idx]
            if moving: 
                cat_left += speed
        else:
            cat = cat_sprite['jump_left'][idx]
            if moving: 
                cat_left -= speed
        
        
    elif keyboard[keys.RIGHT]:
        cat = cat_sprite['right'][cat_idx]
        facing_right = True
        moving = True
        cat_left += speed

    elif keyboard[keys.LEFT]:
        cat = cat_sprite['left'][cat_idx]
        facing_right = False
        moving = True
        cat_left -= speed

    else:
        moving = False
        if facing_right:
            cat = cat_sprite['idle'][cat_idx]
        else:
            cat = cat_sprite['idle_left'][cat_idx]
    
    cat.left = cat_left
    if cat.left >= WIDTH:
        cat.right = 0 
        cat_left = cat.left
    elif cat.right < 0:
        cat.left = WIDTH
        cat_left = cat.left


def draw():
    screen.fill((0,25,50))
    if cat:
        cat.draw()
    
# create a cat sprite to hold the different animations
cat_sprite = { 
    'right' : [],
    'left' : [],
    'idle' : [],
    'idle_left' : [],
    'jump' : [],
    'jump_left' : []
    }

# create all the pgzero Actors for each animation state
for i in range(10):
    cat_sprite['right'].append(Actor('cat_walk_{}'.format(i + 1)))
    cat_sprite['left'].append(Actor('cat_walk_{}b'.format(i + 1)))
    cat_sprite['idle'].append(Actor('cat_idle_{}'.format(i + 1)))
    cat_sprite['idle_left'].append(Actor('cat_idle_{}b'.format(i + 1)))
    if i < 8:
        cat_sprite['jump'].append(Actor('cat_jump_{}'.format(i + 1)))
        cat_sprite['jump_left'].append(Actor('cat_jump_{}b'.format(i + 1)))
    
    
    
clock.schedule_interval(fps_tick, .05)