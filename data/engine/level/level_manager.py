import pygame


class LevelManager:
    def __init__(self, pde) -> None:
        self.active = False
        self.pde = pde
        self.level = None

    def addlevel(self, level, name, active):
        level.active = active
        self.level= level

    def changelevel(self, level, name, active):
        self.level = None
        level.active = active
        self.level = level

    def removelevel(self, level):
        for obj in list(self.level.objectManager.objects.values()):
            obj.deconstruct()
        self.levels.pop(level)

    def update(self):
        self.level.update()


    def activate(self):
        pass