import pygame
from data.engine.actor.actor import Actor
from data.engine.anim.anim_manager import AnimManager
from data.engine.sprite.sprite_component import SpriteComponent


class Jumpscare(Actor):
    def __init__(self, man, pde, position=[0, 0], scale=[640, 480], lifetime=160):
        super().__init__(man, pde)
        self.position = position
        self.scale = scale
        self.lifetime = lifetime
        self.useCenterForPosition = False
        self.checkForCollision = False
        self.checkForOverlap = False


    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\ui\hud\risky.png', layer=5)
        
    def update(self):
        if self.ticks >= 30:
            self.components["Sprite"].sprite.opacity -= 5
        super().update()


