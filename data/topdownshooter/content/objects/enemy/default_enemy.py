import random
from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.ai.ai_component import AIComponent
from data.topdownshooter.content.ai.ai_close_quarters import ShortAI
from data.topdownshooter.content.ai.ai_wander import WanderAI
from data.topdownshooter.content.ai.ai_weaponless import WeaponlessAI
from data.topdownshooter.content.objects.enemy.enemy import ShooterEnemy
from data.topdownshooter.content.objects.weapon.pickup.pickupweapon import PickupWeapon
from data.topdownshooter.content.objects.weapon.weapons.weapons import Medpack


class DefaultEnemy(ShooterEnemy):
    def __init__(self, man, pde, position=None, velocity=4, weapon=None, hp=100):
        super().__init__(man, pde, position, velocity, weapon)
        self.hp = hp
        self.ignoreEntities = [DefaultEnemy]

    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\me.png', layer=2)
        self.components["AI"] = AIComponent(owner=self)
        self.components["AI"].addstate(name="wander", state=WanderAI)
        self.components["AI"].addstate(name="weaponless", state=WeaponlessAI)
        self.components["AI"].addstate(name="short", state=ShortAI)

        self.components["AI"].state = "wander"

    def update(self):
        super().update()

        if self.weapon is None:
            if self.components["AI"].state != "weaponless":
                self.components["AI"].state = "weaponless"
        else:
            self.components["AI"].state = self.weapon.ai_state


    def die(self, killer):
        if random.randint(1,1) == 1:
            med = self.man.add_object(Medpack(man=self.man, pde=self.pde, position=self.position, owner=self, lifetime=1))
            self.man.add_object(obj=PickupWeapon(man=self.man, pde=self.pde, position=list(self.rect.center), rotation=random.randint(0,360), weapon=med, speed=[4, 4]))
        super().die(killer)