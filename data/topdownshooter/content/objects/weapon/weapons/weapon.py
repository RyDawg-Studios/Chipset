import math
import random

import pygame
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import getpositionlookatvector, normal_cut, objectlookatposition, objectlookattarget
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.weapon.bullets.bullet import Bullet
from copy import deepcopy

class Weapon(Actor):
    def __init__(self, man, pde, owner, position=[0, 0], firerate=10, bullet=Bullet, shotangles=None, shotspread=4, sprite=''):

        #----------< Actor Info >----------#
        self.owner = owner
        self.position = position
        self.checkForCollision = False
        self.checkForOverlap = False
        self.useCenterForPosition = True

        #----------< Shot Info >----------#
        if shotangles is None:
            shotangles = [0]
        self.shotangles = shotangles
        self.firerate = firerate
        self.bullet = bullet
        self.shotspread = shotspread
        self.shottick = 500
        self.shottime = 0

        #----------< Weapon Info >----------#
        self.shooting = False
        self.upgrades = []

        super().__init__(man, pde)
        
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=sprite, layer=3)


    def shoot(self, target):
        self.shooting = True
        bs = []
        if self.shottick >= self.firerate:
            self.shottick = 0
            for shot in self.shotangles:

                target_pos = pygame.Vector2(target)
                shooter_to_target = target_pos - self.position
                with_spread = shooter_to_target.rotate(normal_cut(0, self.shotspread))
                bullet_target = with_spread.rotate(shot) + self.position
                
                b = self.man.add_object(obj=self.bullet(man=self.man, pde=self.pde, owner=self, target=bullet_target, position=self.rect.center))
                for u in self.upgrades:
                    u.onShot(bullet=b, target=target)

                b.onshot()
                bs.append(b)

        return bs
                
    def update(self):
        self.shottick += 1
        self.components["Sprite"].sprite.rotation = self.rotation
        if self.shooting:
            self.shottime += 1
        else:
            if self.shottime != 0:
                self.shottime = 0
        self.shooting = False
        return super().update()

    def pickup(self):
        pass
