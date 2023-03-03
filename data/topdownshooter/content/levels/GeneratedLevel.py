import random
from types import NoneType
from data.engine.level.level import Level
from data.topdownshooter.content.levels.levelloader.levelloader import LevelLoader
from data.topdownshooter.content.levels.levelloader.room import Room
from data.topdownshooter.content.objects.hazard.hole.hole import Hole
from data.topdownshooter.content.objects.levelgenerator.level_generator import LevelGenerator
from data.topdownshooter.content.objects.player.player import ShooterPlayer
from data.topdownshooter.content.objects.turret.turret import Turret
from data.topdownshooter.content.objects.weapon.weapons.weapons import DevGun, Pistol



class GeneratedLevel(Level):
    def __init__(self, man, pde):
        super().__init__(man, pde)
        self.changebackground(r'data\topdownshooter\assets\sprites\backgrounds\bg.png')


        l = self.objectManager.add_object(LevelGenerator(man=self.objectManager, pde=pde, position=[0,0], scale=[10, 10], complexity=self.pde.game.currentRoomNumber))
        pos = random.choice(l.whitespace)
        p = self.objectManager.add_object(ShooterPlayer(man=self.objectManager, pde=pde, position=l.get_spawnpoint(), hp=self.pde.game.playerData.hp))

        x = self.pde.game.playerData.loadout[0]

        if x is not NoneType:
            w = x(man=self.objectManager, pde=self.pde, owner=p, position=[0,0])
            p.weapon = self.objectManager.add_object(obj=w)
        else:
            w = None
            p.weapon = w
        


    def deconstruct(self):
        return super().deconstruct()


