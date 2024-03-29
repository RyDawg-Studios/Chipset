import random
from data.topdownshooter.content.objects.hazard.explosion.explosion import Explosion
import data.topdownshooter.content.objects.shooterentity.shooterentity as se
from data.topdownshooter.content.objects.weapon.bullets.bullets import Grenade
from data.topdownshooter.content.objects.weapon.upgrade.upgrade import Upgrade
from data.topdownshooter.content.tiles.tile import Tile


class VamprismUpgrade(Upgrade):
    def __init__(self, man, pde, weapon):
        super().__init__(man, pde, weapon, id="Vamprism")
        self.rate = 0.5

    def onHit(self, bullet, damage, object):
        if isinstance(object, se.ShooterEntity):
            if self.weapon.owner is not None and object.canGrantHP:
                self.weapon.owner.hp += (damage * self.rate)
        return super().onHit(bullet, damage, object)

class SplitStreamUpgrade(Upgrade):
    def __init__(self, man, pde, weapon):
        super().__init__(man, pde, weapon, id="SplitStream")
        weapon.shotangles = [-5, 5]

class DisarmamentUpgrade(Upgrade):
    def __init__(self, man, pde, weapon):
        super().__init__(man, pde, weapon, id="Disarmament")

    def onHit(self, bullet, damage, object):
        if isinstance(object, se.ShooterEntity):
            if random.randint(0, 100) <= 50:
                object.dropweapon(rotation=bullet.rotation)
        return super().onHit(bullet, damage, object)

class ExplosiveBulletsUpgrade(Upgrade):
    def __init__(self, man, pde, weapon):
        super().__init__(man, pde, weapon, id="ExplosiveBullets")

    def onHit(self, bullet, damage, object):
        if isinstance(object, se.ShooterEntity) or isinstance(object, Tile):
            self.man.add_object(obj=Explosion(man=self.man, pde=self.pde, owner=bullet, position=bullet.rect.center, scale=[32, 32]))
        return super().onHit(bullet, damage, object)

class SecondWindUpgrade(Upgrade):
    def __init__(self, man, pde, weapon):
        super().__init__(man, pde, weapon, id="SecondWind")

    def onShot(self, bullet, target):
        super().onShot(bullet, target)
        self.weapon.owner.dodgecooldown = 200
        self.weapon.owner.can

class GrenadeLauncherUpgrade(Upgrade):
    def __init__(self, man, pde, weapon):
        super().__init__(man, pde, weapon, id="GrenadeUpgrade")
        self.shotTicks = 0

    def update(self):
        super().update()
        self.shotTicks += 1

    def onAltShot(self, target):
        super().onAltShot(target)
        if self.shotTicks >= 120:
            self.weapon.shoot(target=target, bullet=Grenade)
            self.shotTicks = 0

upgrades = [VamprismUpgrade, SplitStreamUpgrade, DisarmamentUpgrade, ExplosiveBulletsUpgrade, SecondWindUpgrade, GrenadeLauncherUpgrade]





