import pygame
from data.engine.actor.actor import Actor
from data.engine.anim.anim_manager import AnimManager
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity


class Splat(Actor):
    def __init__(self, man, pde, owner, position=[0, 0], scale=[64, 64], lifetime=360, color='blue'):
        self.position = position
        self.scale = scale
        self.lifetime = lifetime
        self.owner = owner
        self.useCenterForPosition = True
        self.checkForCollision = False
        self.objects = []
        super().__init__(man, pde)
        if color == 'blue':
            self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\weapons\splatgun\splatblue.png', layer=0)
        elif color == 'orange':
            self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\weapons\splatgun\splatorange.png', layer=0)

    def update(self):
        for object in self.overlapInfo["Objects"]:
            if isinstance(object, ShooterEntity):
                self.objects.append(object)

        for object in self.objects:
            if object not in self.overlapInfo["Objects"]:
                object.velocity = object.maxVelocity
            else:
                if object.velocity != object.maxVelocity / 2 and object != self.owner.owner.owner:
                    object.velocity = object.maxVelocity / 2

        return super().update()



