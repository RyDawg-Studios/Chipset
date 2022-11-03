from data.engine.game.game import Game
from data.topdownshooter.content.levels.DevLevel import DevLevel
from data.topdownshooter.content.levels.ShooterLevel import ShooterLevel
from data.topdownshooter.content.levels.StartLevel import StartLevel
from data.topdownshooter.content.levels.morphlevel import MorphLevel
from data.topdownshooter.content.levels.TestLevel import TestLevel

class ShooterGame(Game):
    def __init__(self, pde):
        self.player = None
        self.currentlevel = None
        super().__init__(pde)

    
    def changelevel(self, level):
        self.clearObjectManager()
        self.currentlevel = level
        l = self.pde.level_manager.addlevel(level=level(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)
        return l

    def activate(self):
        self.changelevel(DevLevel)
        return super().activate()

    def restart(self):
        self.pde.player_manager.clear()
        self.changelevel(self.currentlevel)
        return
