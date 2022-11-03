import json
import math
from msilib.schema import Upgrade
import random

import pygame
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import getpositionlookatvector, normal_cut, objectlookatposition, objectlookattarget
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.weapon.bullets.bullet import Bullet

class Weapon(Actor):
    def __init__(self, man, pde, owner, position=[0, 0], id=None, bullet=Bullet):
        super().__init__(man, pde)
        #----------< Data Info >----------#
        self.id = id
        if self.id != None:
            weapondata = json.load(open(r"data\topdownshooter\data\weapondata.json"))[self.id]

            self.scale = weapondata["transforminfo"]["scale"]
            self.sprite = weapondata["transforminfo"]["sprite"]

            self.shotangles = weapondata['statinfo']['shotangles']
            self.firerate = weapondata['statinfo']['firerate']
            self.shotspread = weapondata['statinfo']['shotspread']
            self.damagemultiplier = weapondata['statinfo']['damagemultiplier']

            self.name = weapondata['textinfo']['name']
            self.description = weapondata['textinfo']['desc']
            self.flavor = weapondata['textinfo']['flavor']
        else:
            self.scale = [20, 10]
            self.sprite = ''

            self.shotangles = [0]
            self.firerate = 10
            self.shotspread = 4
            self.damagemultiplier = 1.0

            self.name = 'Default Name'
            self.description = 'Default Description'
            self.flavor = 'Devault Flavor'
            

        #----------< Actor Info >----------#
        self.owner = owner
        self.position = position
        self.checkForCollision = False
        self.checkForOverlap = False
        self.useCenterForPosition = True


        #----------< Shot Info >----------#
        self.bullet = bullet
        self.shottick = 500
        self.shottime = 0
        self.shooting = False
        

        #----------< Weapon Info >----------#
        self.upgrades = []



    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=self.sprite, layer=3)
        


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
        return

    def deconstruct(self):
        self.owner = None
        return super().deconstruct()