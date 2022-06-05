from data.engine.game.game import Game
from data.topdownshooter.content.levels.DevLevel import DevLevel
from data.topdownshooter.content.levels.ShooterLevel import ShooterLevel
from data.topdownshooter.content.levels.StartLevel import StartLevel
from data.topdownshooter.content.levels.morphlevel import MorphLevel

class ShooterGame(Game):
    def __init__(self, pde):
        self.player = None
        super().__init__(pde)


    def activate(self):
        super().activate()
        self.pde.level_manager.levels = {}
        self.pde.level_manager.addlevel(level=DevLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)


    def loadMorphLevel(self):
        super().activate()
        self.pde.level_manager.level = None
        self.pde.level_manager.addlevel(level=MorphLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)