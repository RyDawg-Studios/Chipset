from data.engine.actor.actor import Actor
from data.engine.object.object import Object
from data.engine.sprite.sprite_component import SpriteComponent

class HealthBar(Actor):
    def __init__(self, man, pde, owner=None):
        super().__init__(man, pde)
        self.checkForCollision = False
        self.checkForOverlap = False
        self.owner = owner
        self.scale = [40, 2]

    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\ui\healthbar\bar.png', layer=6)

    def update(self):
        self.rect.centerx= self.owner.position.x
        self.rect.centery = self.owner.position.y - 24
        if self.owner.hp > 0:
            self.rect.width = (self.owner.hp / self.owner.maxhp )* 40
        else:
            self.rect.width = 0
        return super().update()
