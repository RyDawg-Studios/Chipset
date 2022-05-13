import math
import random

import pygame
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import objectlookatposition, objectlookattarget
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.weapon.bullets.bullet import Bullet
from copy import deepcopy

class Weapon(Actor):
    def __init__(self, man, pde, owner, firerate=10, bullet=Bullet, shotangles=None, shotspread=10, sprite=''):

        #----------< Actor Info >----------#
        self.owner = owner
        self.checkForCollision = False
        self.checkForOverlap = False

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

        super().__init__(man, pde)
        
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=sprite, layer=3)


    def shoot(self, target):
        self.shooting = True
        bs = []
        if self.shottick >= self.firerate:
            self.shottick = 0
            for shot in self.shotangles:
                if self.shotspread != 0:
                    spr = random.randrange(-self.shotspread, self.shotspread)
                else:
                    spr = 0
                
                spr = [spr, spr]
                
                targ = pygame.Vector2(target) + spr

                b = self.man.add_object(obj=self.bullet(man=self.man, pde=self.pde, owner=self, target=targ, position=[self.owner.position[0] + 10, self.owner.position[1] + 10]))
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
