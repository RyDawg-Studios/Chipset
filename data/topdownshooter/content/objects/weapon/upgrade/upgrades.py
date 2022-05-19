import random
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
from data.topdownshooter.content.objects.weapon.upgrade.upgrade import Upgrade


class VamprismUpgrade(Upgrade):
    def __init__(self, man, pde, weapon):
        super().__init__(man, pde, weapon)

    def onHit(self, bullet, damage, object):
        if isinstance(object, ShooterEntity):
            self.weapon.owner.hp += damage
        return super().onHit(bullet, damage, object)

class SplitStreamUpgrade(Upgrade):
    def __init__(self, man, pde, weapon):
        super().__init__(man, pde, weapon)
        weapon.shotangles = [-5, 5]

class DisarmamentUpgrade(Upgrade):
    def __init__(self, man, pde, weapon):
        super().__init__(man, pde, weapon)

    def onHit(self, bullet, damage, object):
        if isinstance(object, ShooterEntity):
            if random.randint(0, 100) <= 50:
                object.dropweapon(rotation=bullet.rotation)
        return super().onHit(bullet, damage, object)



