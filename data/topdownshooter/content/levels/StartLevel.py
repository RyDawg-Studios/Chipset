from data.engine.level.level import Level
from data.topdownshooter.content.levels.levelloader.levelloader import LevelLoader
from data.topdownshooter.content.objects.hazard.hole.hole import Hole
from data.topdownshooter.content.objects.player.player import ShooterPlayer
from data.topdownshooter.content.objects.widget.startwidget import StartButton



class StartLevel(Level):
    def __init__(self, man, pde):
        super().__init__(man, pde)
        b = self.objectManager.add_object(StartButton(man=self.objectManager, pde=self.pde, position=[0,0]))
