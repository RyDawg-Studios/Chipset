from data.engine.level.level import Level
from data.topdownshooter.content.levels.levelloader.levelloader import LevelLoader
from data.topdownshooter.content.levels.levelloader.room import Room
from data.topdownshooter.content.objects.hazard.hole.hole import Hole
from data.topdownshooter.content.objects.player.player import ShooterPlayer



class GeneratedLevel(Level):
    def __init__(self, man, pde):
        super().__init__(man, pde)
        self.changebackground(r'data\topdownshooter\assets\sprites\backgrounds\bg.png')

        p = self.objectManager.add_object(ShooterPlayer(man=self.objectManager, pde=pde, position=[320, 240]))

        lm = self.objectManager.add_object(Room(man=self.objectManager, pde=pde, position=[0,0], level="room1"))

