import pygame 
from data.engine.PyDawgEngine import PyDawgEngine

#Initialize Important Pygame Lis
pygame.init()
pygame.font.init()
pygame.joystick.init()

#Create Engine Object
if __name__ == '__main__':
    engine = PyDawgEngine()
