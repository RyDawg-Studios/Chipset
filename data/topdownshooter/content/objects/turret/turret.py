from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.enemy.enemy import ShooterEnemy
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
from data.topdownshooter.content.objects.weapon.weapons.weapons import TurretHead


class Turret(ShooterEnemy):
    def __init__(self, man, pde, position=None, velocity=4, weapon=None):
        super().__init__(man, pde, position, velocity, weapon)
        self.weapon = TurretHead
        self.weaponoffset = 0

    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\objects\turret\turret_base.png',layer=2)
