import math
import random
import pygame
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import getpositionlookatvector, objectlookatposition, objectlookattarget
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.hazard.explosion.explosion import Explosion
from data.topdownshooter.content.objects.weapon.bullets.bullet import Bullet




class HomingActor(Actor):
    def __init__(self, man, pde, position=[0, 0], owner=None):
        self.position = position
        self.scale = [400, 400]
        self.owner = owner
        self.target = None
        self.foundtarget = False
        self.checkForCollision = False
        super().__init__(man, pde)

    def overlap(self, obj):
        if self.foundtarget == False:
            self.target = obj
            if hasattr(obj, 'homable'):
                if obj.homable and obj != self.owner.owner.owner:
                    self.owner.target = getpositionlookatvector(self, obj.position)
                    self.owner.rotation = objectlookattarget(self, obj)
        return super().overlap(obj)

    def update(self):
        self.rect.center = self.owner.rect.center
        return super().update()

class DefaultBullet(Bullet):
    def __init__(self, man, pde, owner, position=[0, 0], target=[0, 0]):
        super().__init__(man, pde, owner, position, target)

class DevBullet(Bullet):
    def __init__(self, man, pde, owner, target=[0,0], position=[0, 0]):
        self.scale=[12, 12]
        super().__init__(man, pde, owner, position=position, target=target)
        self.damage = 5
        self.homing = False
        self.hometicks = 0
        self.starthometime = 6
        self.area = None
        self.speed=24

    def update(self):
        self.hometicks += 1
        if self.hometicks >= self.starthometime:
            if not self.homing:
                self.area = self.man.add_object(obj=HomingActor(man=self.man, pde=self.pde, position=list(self.rect.center), owner=self))
                self.homing = True

        return super().update()

    def deconstruct(self):
        if self.area != None:
            self.area.deconstruct()
        return super().deconstruct()

class Grenade(Bullet):
    def __init__(self, man, pde, owner, target=[0,0], position=[0, 0]):
        self.scale = [20, 14]
        self.owner = owner
        self.lifetime = 120
        super().__init__(man, pde, owner, position=position, scale=self.scale, target=target, sprite=r'data\topdownshooter\assets\sprites\weapons\grenadelauncher\grenade.png')
        self.destroyOnCollide = False
        self.checkForCollision = True
        self.speed = 12
        self.damage = 3
        self.fuse=60
        self.fusetime = 0
        self.explosion = Explosion
        

    def update(self):
        self.fusetime += 1
        if self.fusetime >= self.fuse:
            self.explode()
            self.deconstruct()

        if self.speed > 0.3:
            self.speed -= 0.3
        return super().update()

    def collide(self, obj, side):
        if side == "Left":
            self.target = pygame.Vector2(self.target.reflect((-1,0)))
        if side == "Right":
             self.target = pygame.Vector2(self.target.reflect((1,0)))
        if side == "Top":
             self.target = pygame.Vector2(self.target.reflect((0, -1)))
        if side == "Bottom":
            self.target = pygame.Vector2(self.target.reflect((0, 1)))
        return super().collide(obj, side)

    def checkXcollision(self, movement):
        if self.canMove:
            self.rect.x += self.movement.x * self.velocity
            hits = self.getoverlaps()  
            for object in hits:
                if hasattr(object, 'checkForCollision') and object.checkForCollision and self.checkForCollision:
                    if object != self.owner and object != self.owner.owner and not isinstance(self, object.__class__):
                        if object not in self.collideInfo["Objects"]:
                            self.collideInfo["Objects"].append(object)
                        if movement[0] > 0:
                            self.rect.right = object.rect.left
                            self.collideInfo["Right"] = True
                            self.collide(self, "Right")
                        elif movement[0] < 0:
                            self.rect.left = object.rect.right
                            self.collideInfo["Left"] = True
                            self.collide(self, "Left")

    def checkYcollision(self, movement):
        if self.canMove:
            self.rect.y += self.movement.y * self.velocity
            hits = self.getoverlaps()  
            for object in hits:
                if hasattr(object, 'checkForCollision') and object.checkForCollision and self.checkForCollision:
                    if object != self.owner and object != self.owner.owner and not isinstance(self, object.__class__):
                        if object not in self.collideInfo["Objects"]:
                            self.collideInfo["Objects"].append(object)
                        if movement[1] > 0:
                            self.rect.bottom = object.rect.top
                            self.collideInfo["Bottom"] = True
                            self.collide(self, "Bottom")
                        elif movement[1] < 0:
                            self.rect.top = object.rect.bottom
                            self.collideInfo["Top"] = True
                            self.collide(self, "Top")

    def explode(self):
        e = self.man.add_object(obj=self.explosion(man=self.man, pde=self.pde, owner=self, position = self.position, scale = [128, 128]))

class LaserBullet(Bullet):
    def __init__(self, man, pde, owner, position=[0, 0], target=[0, 0]):
        super().__init__(man, pde, owner, position, target, scale=[20, 4], sprite=r'data\topdownshooter\assets\sprites\weapons\lasermachinegun\laserbullet.png')
        self.speed = 26
        self.damage = 5

class SniperBullet(Bullet):
    def __init__(self, man, pde, owner, position=[0, 0], target=[0, 0]):
        super().__init__(man, pde, owner, position, target)
        self.speed = 48
        self.damage = random.randint(80, 120)





