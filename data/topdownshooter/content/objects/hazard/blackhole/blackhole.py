import random
import pygame
from data.engine.actor.actor import Actor
from data.engine.anim.anim_manager import AnimManager
from data.engine.fl.world_fl import getpositionlookatvector
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
import data.topdownshooter.content.objects.weapon.bullets.bullets as b


class BlackHole(Actor):
    def __init__(self, man, pde, owner, position=[0, 0], scale=[64, 64], lifetime=260, color='blue'):
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
    
    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\objects\blackhole\blackhole.png', layer=0)

    def update(self):
        if self.ticks >= 90:
            self.components["Sprite"].sprite.opacity -= 5

        if self.pde.game.player is not None:
             self.pde.game.player.movement += getpositionlookatvector( self.pde.game.player, self.position) * (pygame.Vector2.distance_to(self.position, self.pde.game.player.position)/250)

        for object in self.getNeighboringObjects():
            if isinstance(object, b.Grenade):
                object.movement += getpositionlookatvector( self.pde.game.player, self.position) * (pygame.Vector2.distance_to(self.position, self.pde.game.player.position)/50)
        super().update()



        




