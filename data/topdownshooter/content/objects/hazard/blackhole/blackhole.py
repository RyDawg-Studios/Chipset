import random
import pygame
from data.engine.actor.actor import Actor
from data.engine.anim.anim_manager import AnimManager
from data.engine.fl.world_fl import getpositionlookatvector
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity


class BlackHole(Actor):
    def __init__(self, man, pde, owner, position=[0, 0], scale=[64, 64], lifetime=360, color='blue'):
        super().__init__(man, pde)
        self.position = position
        self.scale = scale
        self.lifetime = lifetime
        self.owner = owner
        self.useCenterForPosition = True
        self.checkForCollision = False
        self.checkForOverlap = False
        self.objects = []
        self.rotation = random.randint(0, 360)
        print("AH")
    
    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\objects\blackhole\blackhole.png', layer=0)

    def update(self):
        if self.ticks >= 300:
            self.components["Sprite"].sprite.opacity -= 5

        if self.pde.game.player is not None:
             self.pde.game.player.movement += getpositionlookatvector( self.pde.game.player, self.position) * 0.75
        super().update()




