import random
import pygame
from data.engine.actor.actor import Actor
from data.engine.anim.anim_manager import AnimManager
from data.engine.sprite.sprite_component import SpriteComponent


class Splat(Actor):
    def __init__(self, man, pde, owner, position=[0, 0], scale=[64, 64], lifetime=260, color='blue'):
        super().__init__(man, pde)
        self.color = color
        self.position = position
        self.scale = scale
        self.lifetime = lifetime
        self.owner = owner
        self.useCenterForPosition = True
        self.checkForCollision = False
        self.checkForOverlap = False
        self.objects = []
        self.rotation = random.randint(0, 360)
    
    def construct(self):
        super().construct()
        if self.color == 'blue':
            self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\weapons\splatgun\splatblue.png', layer=0)
        elif self.color == 'orange':
            self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\weapons\splatgun\splatorange.png', layer=0)

    def update(self):

        if self.ticks >= 200:
            self.components["Sprite"].sprite.opacity -= 5
        return super().update()



