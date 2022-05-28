from data.engine.level.level import Level
from data.topdownshooter.content.levels.levelloader.levelloader import LevelLoader
from data.topdownshooter.content.objects.hazard.hole.hole import Hole
from data.topdownshooter.content.objects.player.player import ShooterPlayer



class MorphLevel(Level):
    def __init__(self, man, pde):
        super().__init__(man, pde)

        p = self.objectManager.add_object(ShooterPlayer(man=self.objectManager, pde=pde, position=[320, 240]))
        lm = self.objectManager.add_object(LevelLoader(man=self.objectManager, pde=pde, position=[0,0], level="m_room0"))

        h = self.objectManager.add_object(Hole(man=self.objectManager, pde=pde, position=[100, 100]))
