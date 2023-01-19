import random
from data.engine.actor.actor import Actor
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.widgets.button import Button
from data.topdownshooter.content.objects.widget.infobox import InfoBox

class PickupWeapon(Actor):
    def __init__(self, man, pde, position=[0, 0], speed=[4, 4], rotation=0, weapon=None):
        super().__init__(man, pde)
        self.weapon = weapon
        self.position = position
        self.scale = self.weapon.scale
        self.checkForCollision = False
        self.checkForOverlap = True
        self.useCenterForPosition = True
        self.speed = speed
        self.rotation = rotation
        self.rotdir = random.choice([-0.35, 0.35])
        self.rotticks = 0
        self.rottime = 100
        self.hoverframes = 0

        self.infobox = None

    def construct(self):
        super().construct()

        self.components['Sprite'] = SpriteComponent(owner=self, sprite=self.weapon.components["Sprite"].path, layer=1)
        self.components["Projectile"] = ProjectileComponent(owner=self, rotation=self.rotation, speed=self.speed)
        self.components["Button"] = Button(owner=self)
        self.components["Button"].whilehovered = self.whilehovered
        self.components["Button"].whilenothovered = self.whilenothovered

    def update(self):
        self.rotticks += 1
        if self.rotticks >= self.rottime:
            self.components["Projectile"].rotation += self.rotdir
        self.components["Projectile"].speed[0] -= 0.2
        self.components["Projectile"].speed[1] -= 0.2

        if self.components["Projectile"].speed[0] < 0:
            self.components["Projectile"].speed[0] = 0
        if self.components["Projectile"].speed[1] < 0:
            self.components["Projectile"].speed[1] = 0

    def whilehovered(self):
        self.hoverframes += 1
        if self.infobox is None and self.hoverframes >= 30:
            self.infobox = self.man.add_object(obj=InfoBox(man=self.man, pde=self.pde, weapon=self.weapon))
        return

    def whilenothovered(self):
        if self.infobox is not None:
            self.infobox.deconstruct()
            self.infobox = None
        self.hoverframes = 0
        return

    def deconstruct(self):
        if self.infobox is not None:
            self.infobox.deconstruct()
        return super().deconstruct() 