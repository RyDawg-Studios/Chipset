from data.engine.game.game import Game
from data.engine.game.game_server import GameServer
from data.engine.object.object_manager import ObjectManager
from data.topdownshooter.content.levels.BossLevel import BossLevel
from data.topdownshooter.content.levels.DevLevel import DevLevel
from data.topdownshooter.content.levels.ServerLevels.ServerLevel import ServerLevel

from data.topdownshooter.content.levels.MainMenu import MainMenu
from data.topdownshooter.content.levels.ShooterLevel import ShooterLevel
from data.topdownshooter.content.levels.StartLevel import StartLevel
from data.topdownshooter.content.levels.morphlevel import MorphLevel
from data.topdownshooter.content.levels.TestLevel import TestLevel
from data.topdownshooter.content.levels.GeneratedLevel import GeneratedLevel
from data.topdownshooter.content.objects.player.player import ShooterPlayer
from data.topdownshooter.content.objects.player.player_data_object import PlayerDataObject
from data.topdownshooter.content.objects.server.player.player_server import ShooterPlayerServer
from data.topdownshooter.content.objects.widget.leveltext import LevelText
from data.topdownshooter.content.objects.widget.shooterwidget import ShooterWidget

class ShooterGameServer(GameServer):
    def __init__(self, pde):
        super().__init__(pde)
        self.player = None
        self.currentlevel = ServerLevel
        self.currentRoomNumber = 10
        self.playerData = None
        self.ui = None

    def activate(self):
        super().activate()
        self.changelevel(ServerLevel)
        self.playerData = PlayerDataObject()
        
    def game_over(self):
        self.playerData = PlayerDataObject()
        self.currentRoomNumber = 1
        self.restart()

    def next_room(self):
        print(self.currentRoomNumber)
        self.currentRoomNumber += 1
        self.restart()

    def allEnemiesKilled(self):
        self.next_room()

    def changelevel(self, level):
        self.pde.level_manager.clearlevel()
        self.currentlevel = level
        l = self.pde.level_manager.addlevel(level=level(man=self.pde.level_manager, pde=self.pde), name="Main", active=True)
        return l

    def restart(self):
        self.pde.player_manager.clear()
        self.changelevel(self.currentlevel)
        return
    
    def add_player(self, data):
        super().add_player(data)
        p = self.pde.level_manager.level.objectManager.add_object(ShooterPlayerServer(man=self.pde.level_manager.level.objectManager, pde=self.pde, position=[0,0], client=data[1]))
        p.removeweapon()
