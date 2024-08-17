import random
from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
from data.topdownshooter.content.objects.weapon.pickup.pickupweapon import PickupWeapon
from data.topdownshooter.content.objects.weapon.weapons.weapon import WeaponData


class Chest(ShooterEntity):
    def __init__(self, man, pde, position=[0,0], items=None):
        super().__init__(man, pde, position=position)
        if items == None:
            items = []
        self.position = position
        self.scale = [32, 32]
        self.items = items

    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\objects\chests\chest.png',layer=2)

    def die(self, killer):
        super().die(killer)
        for item in self.items:
            rotation = random.randint(0, 360)
            self.man.add_object(obj=PickupWeapon(man=self.man, pde=self.pde, position=list(self.rect.center), rotation=rotation, weaponData=WeaponData(weaponClass=item, upgrades=[]), speed=[random.randint(4, 7), random.randint(4, 7)]))
        self.deconstruct()

            

    