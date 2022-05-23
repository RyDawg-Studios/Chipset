import random
from data.engine.fl.world_fl import objectlookatposition
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.enemy.enemy import ShooterEnemy
from data.topdownshooter.content.objects.weapon.weapons.weapon import Weapon
from data.topdownshooter.content.objects.weapon.bullets.bullets import DefaultBullet, DevBullet, Electrosphere, Grenade, LaserBullet, RevolverBullet, Rocket, SMGBullet, ShotgunBullet, SniperBullet, SplatBullet
from data.topdownshooter.content.objects.weapon.upgrade.upgrades import DisarmamentUpgrade, ExplosiveBulletsUpgrade, SplitStreamUpgrade, VamprismUpgrade




class AutomaticRifle(Weapon):
    def __init__(self, man, pde, owner, position):
        self.scale = [40, 14]
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\debug\debugweapon\cbmk2.png', position=position)


        #----------< Weapon Info >----------#

        self.firerate = 12
        self.bullet = DefaultBullet

    def update(self):
        return super().update()

class Shotgun(Weapon):
    def __init__(self, man, pde, owner, position):
        self.scale = [30, 12]
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\shotgun\boomstick.png', position=position)


        #----------< Weapon Info >----------#

        self.firerate = 52
        self.bullet = ShotgunBullet
        self.shotspread = 1
        self.shotangles = [-10, -5, 0, 5, 10]

class SniperRifle(Weapon):
    def __init__(self, man, pde, owner, position):
        self.scale = [40, 14]
        self.shotspread = 1
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\sniper\sniper.png', position=position)

        #----------< Weapon Info >----------#

        self.firerate = 75
        self.bullet = SniperBullet

    def update(self):
        if self.owner.movement[0] != 0 or self.owner.movement[1] != 0:
            self.shotspread = 20
        else:
            self.shotspread = 1
        return super().update()

class SMG(Weapon):
    def __init__(self, man, pde, owner, position):
        self.scale = [24, 18]
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\smg\smg.png', position=position)

        #----------< Weapon Info >----------#

        self.firerate = 4
        self.shotspread = 12
        self.bullet = SMGBullet

    def update(self):
        return super().update()

class DevGun(Weapon):
    def __init__(self, man, pde, owner, position):
        self.scale = [56, 22]
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\devgun\rydawgun.png', position=position)
        self.upgrades = [VamprismUpgrade(man=self.man, pde=self.pde, weapon=self), DisarmamentUpgrade(man=self.man, pde=self.pde, weapon=self), SplitStreamUpgrade(man=self.man, pde=self.pde, weapon=self)]

        #----------< Weapon Info >----------#

        self.shotspread = 0
        self.firerate = 3
        self.bullet = DevBullet

    def update(self):
        return super().update()

class LaserRifle(Weapon):
    def __init__(self, man, pde, owner, position):
        self.scale = [40, 14]
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\devgun\rydawgun.png', position=position)
        #----------< Weapon Info >----------#

        self.firerate = 16
        self.bullet = None

    def update(self):
        self.components["Sprite"].sprite.rotation = self.rotation
        bs = []
        if self.shottime > 20 and not self.shooting:
            for shot in self.shotangles:
                b = self.man.add_object(obj=self.bullet(man=self.man, pde=self.pde, owner=self, scale = [self.shottime, 16], rotation=objectlookatposition(self, self.pde.input_manager.mouse_position) + shot + random.randint(-self.shotspread, self.shotspread)))
  
        return super().update()

    def shoot(self, angle):
        self.shooting = True
        return []

class GrenadeLauncher(Weapon):
    def __init__(self, man, pde, owner, position):
        self.scale = [56, 22]
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\grenadelauncher\grenadelauncher.png', position=position)

        #----------< Weapon Info >----------#

        self.shotspread = 5
        self.firerate = 75
        self.bullet = Grenade

    def update(self):
        self.components["Sprite"].sprite.rotation = self.rotation
        return super().update()

class LaserMachineGun(Weapon):
    def __init__(self, man, pde, owner, position):
        self.scale = [56, 26]
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\lasermachinegun\lasermachinegun.png', position=position)

        #----------< Weapon Info >----------#

        self.firerate = 6
        self.shotspread = 5
        self.bullet = LaserBullet

    def update(self):
        return super().update()

class ElectroLauncher(Weapon):
    def __init__(self, man, pde, owner, position):
        self.scale = [37, 16]
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\electrospherelauncher\electrospherelauncher.png', position=position)

        #----------< Weapon Info >----------#

        self.firerate = 60
        self.shotspread = 2
        self.bullet = Electrosphere

class LingerTest(Weapon):
    def __init__(self, man, pde, owner, position):
        self.scale = [37, 16]
        self.firerate = 1000
        super().__init__(man, pde, owner, sprite='')

    def shoot(self, target):
        self.pde.game.activate()
        return super().shoot(target)

class SpawnerWeapon(Weapon):
    def __init__(self, man, pde, owner, position):
        self.scale = [46, 22]
        self.firerate = 60
        self.item = 0
        self.items = [ShooterEnemy]
        self.shot = False
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\zapinator\zapinator.png', position=position)

    def shoot(self, target):
        self.shooting = True
        if not self.shot:

            if self.item >= 0 and self.item < len(self.items):
                self.man.add_object(self.items[self.item](man=self.man, pde=self.pde, position=target, weapon=SMG))
            else:
                self.item = 0

            self.shot = True
            return


    def update(self):
        if self.shot == True and self.shooting == False:
            self.shot = False
        if not self.shooting:
            self.shooting = False
        return super().update()

class Enderpearl(Weapon):
    def __init__(self, man, pde, owner, position):
        self.scale = [16, 16]
        self.firerate = 60
        self.shot = False
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\enderpearl\enderpearl.png', position=position)

    def shoot(self, target):
        self.shooting = True
        if not self.shot:

            self.owner.rect.center = target

            self.shot = True
            return


    def update(self):
        if self.shot == True and self.shooting == False:
            self.shot = False
        if not self.shooting:
            self.shooting = False
        return super().update()

class SplatGun(Weapon):
    def __init__(self, man, pde, owner, position):
        self.scale = [70, 20]
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\splatgun\splatgun.png', position=position)
        self.upgrades = [SplitStreamUpgrade(pde=pde, man=man, weapon=self)]

        #----------< Weapon Info >----------#

        self.firerate = 12
        self.shotspread = 5
        self.bullet = SplatBullet

    def update(self):
        return super().update()

class RocketLauncher(Weapon):
    def __init__(self, man, pde, owner, position):
        self.scale = [52, 22]
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\rocketlauncher\rocketlauncher.png', position=position)

        #----------< Weapon Info >----------#

        self.shotspread = 5
        self.firerate = 75
        self.bullet = Rocket

    def update(self):
        self.components["Sprite"].sprite.rotation = self.rotation
        return super().update()

class Revolver(Weapon):
    def __init__(self, man, pde, owner, position):
        self.scale = [52, 20]
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\revolver\revolver.png', position=position)
        self.firerate = 25
        self.shot = False
        self.shotspread = 3
        self.bullet = RevolverBullet

    def shoot(self, target):
        self.shooting = True
        if not self.shot:
            super().shoot(target)
            self.shot = True
            return


    def update(self):
        if self.shot == True and self.shooting == False:
            self.shot = False
        if not self.shooting:
            self.shooting = False
        return super().update()