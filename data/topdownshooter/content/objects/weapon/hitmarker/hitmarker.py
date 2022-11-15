from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent


class Hitmarker(Actor):
    def __init__(self, man, pde, position=[0, 0]):
        super().__init__(man, pde)
        self.position = position
        self.scale = [16, 16]
        self.lifetime = 10
        self.useCenterForPosition = True
        self.checkForCollision = False
        self.checkForOverlap = False

    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\weapons\hitmarker\hm.png', layer=4)

    def update(self):
        self.ticks += 1    
        self.checklifetime()