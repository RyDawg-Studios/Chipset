import pygame
from data.engine.actor.actor import Actor
from data.engine.anim.anim_manager import AnimManager
from data.engine.sprite.sprite_component import SpriteComponent


class Explosion(Actor):
    def __init__(self, man, pde, owner, position=[0, 0], scale=[64, 64], lifetime=16, damage=60):
        super().__init__(man, pde)
        self.position = position
        self.scale = scale
        self.lifetime = lifetime
        self.owner = owner
        self.useCenterForPosition = True
        self.checkForCollision = False
        self.checkForOverlap = True
        self.moveable = True
        self.damage = damage


    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\anims\explosion\tile000.png', layer=2)
        
        self.components["Anim"] = AnimManager(owner=self, sprite=self.components["Sprite"])

        self.components["Anim"].addAnimation(name='runright', anim=r'data\topdownshooter\assets\anims\explosion', speed=1, set=True, stopFrame=-1)


        
    def update(self):
        if self.ticks == 1:
            for object in self.overlapInfo["Objects"]:
                if hasattr(object, 'hp'):
                    object.takedamage(self, self.damage)
        return super().update()

