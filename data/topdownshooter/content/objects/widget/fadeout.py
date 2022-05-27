from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent



class FadeOut(Actor):
    def __init__(self, man, pde):
        self.position = [0, 0]
        self.scale = [640, 480]
        self.checkForCollision = False
        self.checkForOverlap = False
        super().__init__(man, pde)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\backgrounds\black.png', layer=99)

    def update(self):
        self.components["Sprite"].sprite.opacity -= 3
        if self.components["Sprite"].sprite.opacity <= 0:
            self.deconstruct()
        return super().update()
