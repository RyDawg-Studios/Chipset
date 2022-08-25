import random
from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
from data.topdownshooter.content.objects.weapon.pickup.pickupweapon import PickupWeapon


class Chest(ShooterEntity):
    def __init__(self, man, pde, position=[0,0], items=[]):
        self.position = position
        self.scale = [32, 32]
        self.items = items
        super().__init__(man, pde, position=self.position)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\objects\chests\chest.png',layer=2)

    def die(self, killer):
        for item in self.items:
            rotation = random.randint(0, 360)
            spawnable = item(man=self.man, pde=self.pde, owner=self, position=self.position)
            self.man.add_object(obj=PickupWeapon(man=self.man, pde=self.pde, position=list(self.rect.center), rotation=rotation, weapon=spawnable, speed=[random.randint(4, 7), random.randint(4, 7)]))
            spawnable.deconstruct()
            spawnable = None

        self.deconstruct()

            
        return super().die(killer)

    