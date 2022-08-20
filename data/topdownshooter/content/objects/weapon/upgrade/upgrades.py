import random
from data.topdownshooter.content.objects.hazard.explosion.explosion import Explosion
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
from data.topdownshooter.content.objects.weapon.upgrade.upgrade import Upgrade
from data.topdownshooter.content.tiles.tile import Tile


class VamprismUpgrade(Upgrade):
    def __init__(self, man, pde, weapon):
        super().__init__(man, pde, weapon, id="Vamprism")

    def onHit(self, bullet, damage, object):
        if isinstance(object, ShooterEntity):
            if self.weapon.owner is not None:
                self.weapon.owner.hp += damage
        return super().onHit(bullet, damage, object)

class SplitStreamUpgrade(Upgrade):
    def __init__(self, man, pde, weapon):
        super().__init__(man, pde, weapon, id="SplitStream")
        weapon.shotangles = [-5, 5]

class DisarmamentUpgrade(Upgrade):
    def __init__(self, man, pde, weapon):
        super().__init__(man, pde, weapon, id="Disarmament")

    def onHit(self, bullet, damage, object):
        if isinstance(object, ShooterEntity):
            if random.randint(0, 100) <= 50:
                object.dropweapon(rotation=bullet.rotation)
        return super().onHit(bullet, damage, object)

class ExplosiveBulletsUpgrade(Upgrade):
    def __init__(self, man, pde, weapon):
        super().__init__(man, pde, weapon, id="ExplosiveBullets")

    def onHit(self, bullet, damage, object):
        if isinstance(object, ShooterEntity) or isinstance(object, Tile):
            self.man.add_object(obj=Explosion(man=self.man, pde=self.pde, owner=bullet, position=bullet.rect.center, scale=[32, 32]))
        return super().onHit(bullet, damage, object)





