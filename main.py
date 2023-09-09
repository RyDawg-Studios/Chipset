import pygame 
from data.engine.PyDawgEngine import PyDawgEngine


#Initialize Important Pygame Libs
pygame.init()
pygame.font.init()  
pygame.joystick.init()

#Create Engine Object 
if __name__ == '__main__':           
    engine = PyDawgEngine()

#-------< TODO >-------#
#  Optimize Tiles because they mad laggy! #
#  Make more guns  #
#  Basically, because spawning a player on the server spawns one on the client, a new PlayerController gets created aswell, replicating all input events for both spawned characters (I think)