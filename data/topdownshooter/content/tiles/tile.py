from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent


class Tile(Actor):
    def __init__(self, man, pde, position=[0, 0], sprite=r'data\assets\sprites\undef.png'):
        super().__init__(man, pde)
        self.spritePath = sprite
        self.position = position
        self.scale =[32, 32]
        self.useCenterForPosition = False

    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=self.spritePath, layer=4)

    def update(self):
        return