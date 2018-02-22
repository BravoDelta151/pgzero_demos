# Write your code here :-)
import time
import pygame

# The artwork for this demo was downloaded from
# https://opengameart.org/content/adventurer-girl-free-sprite
# I had to rename the files for pgzero to work correctly.
# It wants all lower case file names and I replaced the 
# space with an underscore and removed the parenthesis
# I also copied the files and flipped them horizontally 
# to create the left moving/facing sprites. 

WIDTH = 800
HEIGHT = 600
FPS = 30

avatar_idx = 0
jump_idx = 0

facing_right = True
moving = False
jumping = False
avatar = None
avatar_left = 0

def fps_tick():
    global avatar_idx, jump_idx, jumping
    if jumping:
        jump_idx += 1 
        if jump_idx >= 20:
            jumping = False
            jump_idx = 0
        

    avatar_idx = (avatar_idx + 1) % 10
    


def update():
    global avatar, facing_right, avatar_left, jump_idx, jumping, moving
    
	# controls how many pixels the avatar moves with each update
    speed = 5 
    
	# space starts a jump
    if keyboard[keys.SPACE]:
        if not jumping:
            jumping = True
       
    if jumping:
        idx = jump_idx
		# it looks better with the jump animation moves slower
        if idx > 0: 
            idx = min(int(idx / 2), 9)
            
        if facing_right:
            avatar = sprite['jump'][idx]
            if moving: 
                avatar_left += speed
        else:
            avatar = sprite['jump_left'][idx]
            if moving: 
                avatar_left -= speed
        
        
    elif keyboard[keys.RIGHT]:
        avatar = sprite['right'][avatar_idx % 8]
        facing_right = True
        moving = True
        avatar_left += speed

    elif keyboard[keys.LEFT]:
        avatar = sprite['left'][avatar_idx % 8]
        facing_right = False
        moving = True
        avatar_left -= speed

    else:
        moving = False
        if facing_right:
            avatar = sprite['idle'][avatar_idx]
        else:
            avatar = sprite['idle_left'][avatar_idx]
    
    avatar.left = avatar_left
    if avatar.left >= WIDTH:
        avatar.right = 0 
        avatar_left = avatar.left
    elif avatar.right < 0:
        avatar.left = WIDTH
        avatar_left = avatar.left


def draw():
    screen.fill((0,25,50))
    if avatar:
        avatar.draw()
    
# create a sprite to hold the different animations
sprite = { 
    'right' : [],
    'left' : [],
    'idle' : [],
    'idle_left' : [],
    'jump' : [],
    'jump_left' : []
    }

prefix = 'ag'

# create all the pgzero Actors for each animation state
for i in range(10):
    # sprite['right'].append(Actor('{}_walk_{}'.format(prefix, i + 1)))
    # sprite['left'].append(Actor('{}_walk_{}l'.format(prefix, i + 1)))
    sprite['idle'].append(Actor('{}_idle_{}'.format(prefix, i + 1)))
    sprite['idle_left'].append(Actor('{}_idle_{}l'.format(prefix, i + 1)))
    sprite['jump'].append(Actor('{}_jump_{}'.format(prefix, i + 1)))
    sprite['jump_left'].append(Actor('{}_jump_{}l'.format(prefix, i + 1)))
	
    if i < 8: # only 8 frames in the run animation 
        sprite['right'].append(Actor('{}_run_{}'.format(prefix, i + 1)))
        sprite['left'].append(Actor('{}_run_{}l'.format(prefix, i + 1)))
    
    
clock.schedule_interval(fps_tick, .05)