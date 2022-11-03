from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent


class LevelGate(Actor):
    def __init__(self, man, pde, position=[0, 0]):
        super().__init__(man, pde)
        self.checkForCollision = False
        self.useCenterForPosition = True
        self.position = position
        self.scale =[32, 32]
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\mariohitbox.png', layer=8)


    def overlap(self, obj):
        return super().overlap(obj)