from data.engine.server.engine.PyDawgEngine_Server import PyDawgEngineServer
import pygame

pygame.init()
pygame.font.init()
pygame.joystick.init()

if __name__ == '__main__':
    server = PyDawgEngineServer()