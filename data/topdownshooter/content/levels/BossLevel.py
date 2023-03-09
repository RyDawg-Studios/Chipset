import random
from types import NoneType
from data.engine.level.level import Level
from data.topdownshooter.content.levels.levelloader.levelloader import LevelLoader
from data.topdownshooter.content.levels.levelloader.room import Room
from data.topdownshooter.content.objects.enemy.boss_enemy import BossEnemy
from data.topdownshooter.content.objects.hazard.hole.hole import Hole
from data.topdownshooter.content.objects.levelgenerator.level_generator import LevelGenerator
from data.topdownshooter.content.objects.player.player import ShooterPlayer
from data.topdownshooter.content.objects.turret.turret import Turret
from data.topdownshooter.content.objects.weapon.weapons.weapons import DevGun, Pistol



class BossLevel(Level):
    def __init__(self, man, pde):
        super().__init__(man, pde)
        self.changebackground(r'data\topdownshooter\assets\sprites\backgrounds\bg.png')

        lm = self.objectManager.add_object(LevelLoader(man=self.objectManager, pde=pde, position=[-240, -240],level="default"))


        b = self.objectManager.add_object(BossEnemy(man=self.objectManager, pde=pde, position=lm.objects['b'][0]))

        b.onDeathEvent.bind(self.on_boss_killed)

        p = self.objectManager.add_object(ShooterPlayer(man=self.objectManager, pde=pde, position=lm.objects['p'][0], hp=self.pde.game.playerData.hp))

        x = self.pde.game.playerData.loadout[0]

        if x is not NoneType:
            w = x(man=self.objectManager, pde=self.pde, owner=p, position=[0,0])
            p.weapon = self.objectManager.add_object(obj=w)
        else:
            w = None
            p.weapon = w
        

    def on_boss_killed(self, enemy, killer):
        print("Boss Down!")


    def deconstruct(self):
        return super().deconstruct()


