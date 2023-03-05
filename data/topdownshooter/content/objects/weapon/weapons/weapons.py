import random
from data.engine.fl.world_fl import objectlookatposition
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.hazard.jumpscare.jumpscare import Jumpscare
from data.topdownshooter.content.objects.weapon.weapons.weapon import Weapon
from data.topdownshooter.content.objects.weapon.bullets.bullets import AntiMatterBullet, Coin, DartBullet, DefaultBullet, DevBullet, Electrosphere, FireBall, Flame, Grenade, LaserBullet, LaserBullet2, PistolBullet, RevolverBullet, Rocket, SMGBullet, ShotgunBullet, SniperBullet, SplatBullet, StarmadaBullet, TurretBullet, PistolBullet
from data.topdownshooter.content.objects.weapon.upgrade.upgrades import DisarmamentUpgrade, ExplosiveBulletsUpgrade, GrenadeLauncherUpgrade, SecondWindUpgrade, SplitStreamUpgrade, VamprismUpgrade




class AutomaticRifle(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="AutomaticRifle", position=position)
        self.bullet = DefaultBullet

class Shotgun(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="Shotgun", position=position)
        self.bullet = ShotgunBullet
        self.ai_state = "short"

class SniperRifle(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="SniperRifle", position=position)
        self.bullet = SniperBullet

    def update(self):
        if self.owner.movement[0] != 0 or self.owner.movement[1] != 0:
            self.shotspread = 20
        else:
            self.shotspread = 1
        return super().update()

class SMG(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="SMG", position=position)
        self.bullet = SMGBullet

class DevGun(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="Devgun", position=position)
        self.upgrades = [GrenadeLauncherUpgrade(man=self.man, pde=self.pde, weapon=self), DisarmamentUpgrade(man=self.man, pde=self.pde, weapon=self), SplitStreamUpgrade(man=self.man, pde=self.pde, weapon=self)]
        self.bullet = DevBullet

class LaserRifle(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="LaserRifle", position=position)
        self.bullet = None

    def update(self):
        self.components["Sprite"].sprite.rotation = self.rotation
        bs = []
        if self.shottime > 20 and not self.shooting:
            for shot in self.shotangles:
                b = self.man.add_object(obj=self.bullet(man=self.man, pde=self.pde, owner=self, scale = [self.shottime, 16], rotation=objectlookatposition(self, self.pde.input_manager.mouse_position) + shot + random.randint(-self.shotspread, self.shotspread)))
  
        return super().update()

    def shoot(self, target, bullet):
        self.shooting = True
        return []

class GrenadeLauncher(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="GrenadeLauncher", position=position)
        self.bullet = Grenade

class LaserMachineGun(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="LaserMachineGun", position=position)
        self.bullet = LaserBullet

class ElectroLauncher(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="ElectroLauncher", position=position)
        self.bullet = Electrosphere

class SpawnerWeapon(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, position=position, id="DebugGun")
        self.scale = [46, 22]
        self.firerate = 60
        self.item = 0
        self.items = []
        self.shot = False

    def shoot(self, target, bullet):
        self.shooting = True
        if not self.shot:

            if self.item >= 0 and self.item < len(self.items):
                self.man.add_object(self.items[self.item](man=self.man, pde=self.pde, position=target, weapon=LaserMachineGun))
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
        super().__init__(man, pde, owner, position=position)

    def shoot(self, target, bullet):
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
        super().__init__(man, pde, owner, id="SplatGun", position=position)

        #----------< Weapon Info >----------#

        self.firerate = 12
        self.shotspread = 5
        self.bullet = SplatBullet


class RocketLauncher(Weapon):
    def __init__(self, man, pde, owner, position):
        self.scale = [52, 22]
        
        super().__init__(man, pde, owner, id="RocketLauncher", position=position)

        #----------< Weapon Info >----------#

        self.shotspread = 0
        self.firerate = 75
        self.bullet = Rocket

    def update(self):
        self.components["Sprite"].sprite.rotation = self.rotation
        return super().update()

class Revolver(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="Revolver", position=position)
        self.bullet = RevolverBullet

class ChainRifle(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="ChainRifle", position=position)
        self.bullet = LaserBullet2

class TurretHead(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="TurretHead", position=position)
        self.bullet = TurretBullet

class LaserPistol(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="LaserPistol", position=position)
        self.bullet = TurretBullet

class Pistol(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="Pistol", position=position)
        self.bullet = PistolBullet

class RiskGun(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="RiskGun", position=position)
        self.shot = False
        self.bullet = Rocket

    def shoot(self, target, bullet):
        risk = random.randint(0, 100)
        if risk == 69:
            self.jumpscare()

        self.shooting = True
        if not self.shot:
            super().shoot(target, bullet)
            self.shot = True
            return

    def update(self):
        if self.shot == True and self.shooting == False:
            self.shot = False
        if not self.shooting:
            self.shooting = False
        return super().update()

    def jumpscare(self):
        self.pde.display_manager.userInterface.add_object(obj=Jumpscare(man=self.pde.display_manager.userInterface, pde=self.pde))

class Medpack(Weapon):
    def __init__(self, man, pde, owner, position, lifetime = -1):
        super().__init__(man, pde, owner, id="Medpack", position=position, lifetime=lifetime)
        self.bullet = None

    def shoot(self, target, bullet):
        self.owner.hp += 75
        for component in self.components.values():
            component.update()
        self.owner.weapon = None
        self.deconstruct()

    def update(self):
        super().update()

class FlamePistol(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="FlamePistol", position=position)
        self.bullet = FireBall

class LooseChange(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="LooseChange", position=position)
        self.bullet = Coin

class Musket(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="Musket", position=position)
        self.bullet = SniperBullet

    def update(self):
        if self.owner.movement[0] != 0 or self.owner.movement[1] != 0:
            self.shotspread = 10
        else:
            self.shotspread = 2
        return super().update()
    
class AutoShotgun(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="AutoShotgun", position=position)
        self.bullet = ShotgunBullet
        self.ai_state = "short"


class Flamethrower(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="Flamethrower", position=position)
        self.bullet = Flame
        self.ai_state = "short"


class DartRifle(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="DartRifle", position=position)
        self.bullet = DartBullet

class Starmada(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="Starmada", position=position)
        self.bullet = StarmadaBullet

class AntiMatterRifle(Weapon):
    def __init__(self, man, pde, owner, position):
        super().__init__(man, pde, owner, id="AntiMatterRifle", position=position)
        self.bullet = AntiMatterBullet



