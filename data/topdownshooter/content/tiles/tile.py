from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent


class Tile(Actor):
    def __init__(self, man, pde, position=[0, 0], owner=None, sprite=r'data\assets\sprites\undef.png'):
        super().__init__(man, pde)
        self.owner = owner
        self.spritePath = sprite
        self.position = position
        self.scale = [24, 24]
        self.useCenterForPosition = True
        self.canMove = False

    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=self.spritePath, layer=4)

    def update(self):
        super().update()

class OverlapTile(Actor):
    def __init__(self, man, pde, position=[0, 0], owner=None, sprite=r'data\assets\sprites\undef.png'):
        super().__init__(man, pde)
        self.owner = owner
        self.spritePath = sprite
        self.position = position
        self.scale =[32, 32]
        self.useCenterForPosition = True

    def construct(self):
        super().construct()

    def overlap(self, obj):
        print("Yippee!")
        return super().overlap(obj)

    def update(self):
        return