import json

import pygame
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import getpositionlookatvector, normal_cut, objectlookatposition, objectlookattarget
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.weapon.bullets.bullet import Bullet


class WeaponData():
    def __init__(self, weaponClass=None, upgrades=[]) -> None:
        self.weaponClass = weaponClass
        self.weaponUpgrades = upgrades

    def createWeaponData(self, weapon):
        self.weaponClass = weapon.__class__
        self.weaponUpgrades = weapon.upgrades
        return self


class Weapon(Actor):
    def __init__(self, man, pde, owner=None, position=[0, 0], id=None, bullet=Bullet, lifetime = -1):
        super().__init__(man, pde)
        #----------< Data Info >----------#
        self.id = id

            

        #----------< Actor Info >----------#
        self.owner = owner
        self.position = position
        self.checkForCollision = False
        self.checkForOverlap = False
        self.useCenterForPosition = True
        self.lifetime = lifetime
        self.moveable = False


        #----------< Shot Info >----------#
        self.bullet = bullet
        self.shottick = 500
        self.shottime = 0
        self.shooting = False
        

        #----------< Weapon Info >----------#
        self.upgrades = []
        self.uiOverride = None
        self.addToInventory = True
        self.ai_state = "wander"

        #----------< Replication Info >----------#
        self.replicate = True
        self.replication_package = 'tds'
        self.replication_id = 'weapon'
        self.replicable_attributes = {
            "id": str,
            "owner": str
        }



    def construct(self):
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
            self.flavor = 'Default Flavor'

        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=self.sprite, layer=3)        


    def shoot(self, target, bullet):
        self.shooting = True
        bs = []
        if self.shottick >= self.firerate:
            self.shottick = 0
            for shot in self.shotangles:

                target_pos = pygame.Vector2(target)
                shooter_to_target = target_pos - self.position
                with_spread = shooter_to_target.rotate(normal_cut(0, self.shotspread))
                bullet_target = with_spread.rotate(shot) + self.position
                
                b = self.man.add_object(obj=bullet(man=self.man, pde=self.pde, owner=self, target=bullet_target, position=self.rect.center))
                b.on_update_dispatcher.call(self.on_bullet_update)
                b.on_hit_dispatcher.call(self.on_bullet_hit)
                self.components["Sprite"].sprite.rotation = b.rotation
                for u in self.upgrades:
                    u.onShot(bullet=b, target=target)

                b.onshot()
                bs.append(b)

        return bs

    def altShot(self, target):
        for u in self.upgrades:
            u.onAltShot(target)
                
    def update(self):
        if not self.shooting:
            if "Sprite" in self.components.keys():
                self.components["Sprite"].sprite.rotation = self.rotation
        if self.shooting:
            self.shottime += 1
        else:
            if self.shottime != 0:
                self.shottime = 0
        self.shooting = False
        for u in self.upgrades:
            u.update()
        super().update()

    def pickup(self):
        return
    
    def on_bullet_update(self, bullet):
        for upg in self.upgrades:
            upg.onBulletUpdate(bullet=bullet)
    
    def on_bullet_hit(self, bullet):
        for upg in self.upgrades:
            upg.onBulletHit(bullet=bullet)

    def deconstruct(self):
        self.owner = None
        return super().deconstruct()