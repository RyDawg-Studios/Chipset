import random
from data.engine.fl.world_fl import objectlookatposition
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.weapon.weapons.weapon import Weapon
from data.topdownshooter.content.objects.weapon.bullets.bullets import DefaultBullet, DevBullet, Grenade, LaserBullet, SniperBullet


class AutomaticRifle(Weapon):
    def __init__(self, man, pde, owner):
        self.scale = [40, 14]
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\debug\debugweapon\cbmk2.png')

        #----------< Weapon Info >----------#

        self.firerate = 12
        self.bullet = DefaultBullet

    def update(self):
        return super().update()

class Shotgun(Weapon):
    def __init__(self, man, pde, owner):
        self.scale = [30, 12]
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\shotgun\boomstick.png')

        #----------< Weapon Info >----------#

        self.firerate = 60
        self.bullet = LaserBullet
        self.shotspread = 0
        self.shotangles = [-10, -5, 0, 5, 10]

class SniperRifle(Weapon):
    def __init__(self, man, pde, owner):
        self.scale = [40, 14]
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\sniper\sniper.png')

        #----------< Weapon Info >----------#

        self.firerate = 75
        self.bullet = SniperBullet

    def update(self):
        return super().update()

class SMG(Weapon):
    def __init__(self, man, pde, owner):
        self.scale = [24, 18]
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\smg\smg.png')

        #----------< Weapon Info >----------#

        self.firerate = 10
        self.shotspread = 8
        self.bullet = DefaultBullet

    def update(self):
        return super().update()

class DevGun(Weapon):
    def __init__(self, man, pde, owner):
        self.scale = [56, 22]
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\devgun\rydawgun.png')

        #----------< Weapon Info >----------#

        self.shotspread = 0
        self.firerate = 6
        self.bullet = DevBullet

    def update(self):
        return super().update()

class LaserRifle(Weapon):
    def __init__(self, man, pde, owner):
        self.scale = [40, 14]
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\devgun\rydawgun.png')
        #----------< Weapon Info >----------#

        self.firerate = 12
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
    def __init__(self, man, pde, owner):
        self.scale = [56, 22]
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\grenadelauncher\grenadelauncher.png')

        #----------< Weapon Info >----------#

        self.shotspread = 5
        self.shotangles = [0]
        self.firerate = 60
        self.bullet = Grenade

    def update(self):
        self.components["Sprite"].sprite.rotation = self.rotation
        return super().update()

class LaserMachineGun(Weapon):
    def __init__(self, man, pde, owner):
        self.scale = [56, 26]
        super().__init__(man, pde, owner, sprite=r'data\topdownshooter\assets\sprites\weapons\lasermachinegun\lasermachinegun.png')

        #----------< Weapon Info >----------#

        self.firerate = 6
        self.shotspread = 5
        self.bullet = LaserBullet

    def update(self):
        return super().update()
