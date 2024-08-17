from data.engine.game.game import Game
from data.engine.object.object_manager import ObjectManager
from data.topdownshooter.content.levels.BossLevel import BossLevel
from data.topdownshooter.content.levels.DevLevel import DevLevel
from data.topdownshooter.content.levels.MainMenu import MainMenu
from data.topdownshooter.content.levels.ShooterLevel import ShooterLevel
from data.topdownshooter.content.levels.StartLevel import StartLevel
from data.topdownshooter.content.levels.morphlevel import MorphLevel
from data.topdownshooter.content.levels.TestLevel import TestLevel
from data.topdownshooter.content.levels.GeneratedLevel import GeneratedLevel
from data.topdownshooter.content.objects.player.player_data_object import PlayerDataObject
from data.topdownshooter.content.objects.weapon.weapons.weapon import WeaponData
from data.topdownshooter.content.objects.widget.leveltext import LevelText
from data.topdownshooter.content.objects.widget.shooterwidget import ShooterWidget
import data.topdownshooter.content.objects.weapon.weapons.weapon_table as wt


class ShooterGame(Game):
    def __init__(self, pde):
        super().__init__(pde)
        self.player = None
        self.currentlevel = MainMenu
        self.currentRoomNumber = 1
        self.playerData = PlayerDataObject()
        self.ui = None


    def activate(self):
        super().activate()
        self.pde.event_manager.net_events["add_puppet_weapon"] = self.add_puppet_weapon
        self.changelevel(MainMenu)

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
    
    def add_puppet_weapon(self, data):
        print(data)
        for spawned in self.pde.level_manager.level.objectManager.objects:
            if spawned.hash == data[1]:
                spawned.addNetWeapon(data)
                return
    
    def update(self):
        super().update()

