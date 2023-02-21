import random
from data.engine.level.level import Level
from data.topdownshooter.content.levels.levelloader.levelloader import LevelLoader
from data.topdownshooter.content.levels.levelloader.room import Room
from data.topdownshooter.content.objects.hazard.hole.hole import Hole
from data.topdownshooter.content.objects.levelgenerator.level_generator import LevelGenerator
from data.topdownshooter.content.objects.player.player import ShooterPlayer



class GeneratedLevel(Level):
    def __init__(self, man, pde):
        super().__init__(man, pde)
        self.changebackground(r'data\topdownshooter\assets\sprites\backgrounds\bg.png')


        l = self.objectManager.add_object(LevelGenerator(man=self.objectManager, pde=pde, position=[0,0], scale=[16, 16]))
        pos = random.choice(l.whitespace)
        p = self.objectManager.add_object(ShooterPlayer(man=self.objectManager, pde=pde, position=[pos[0]*16, pos[1]*16]))

    def deconstruct(self):
        return super().deconstruct()


