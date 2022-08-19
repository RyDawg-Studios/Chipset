import math
import random
from numpy import isin
import pygame
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import getpositionlookatpositionvector, getpositionlookatvector, objectlookatposition, objectlookattarget, positionlookatposition
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.hazard.explosion.explosion import Explosion
from data.topdownshooter.content.objects.hazard.mine.mine import Mine
from data.topdownshooter.content.objects.hazard.splat.splat import Splat
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
from data.topdownshooter.content.objects.weapon.bullets.bullet import Bullet
from data.topdownshooter.content.tiles.tile import Tile




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
                if isinstance(obj, ShooterEntity) and obj != self.owner.owner.owner:
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
        super().__init__(man, pde, owner, position=position, target=target, sprite=r'data\topdownshooter\assets\sprites\weapons\devgun\devbullet.png')
        self.damage = 5
        self.homing = False
        self.hometicks = 0
        self.starthometime = 1
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
        else:
            self.speed = 0

        
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
        super().__init__(man, pde, owner, position, target, scale=[24, 3], sprite=r'data\topdownshooter\assets\sprites\weapons\sniper\sniperbullet.png')
        self.speed = 48
        self.damage = random.randint(80, 120)

class RevolverBullet(Bullet):
    def __init__(self, man, pde, owner, position=[0, 0], target=[0, 0]):
        super().__init__(man, pde, owner, position, target, scale=[24, 3], sprite=r'data\topdownshooter\assets\sprites\weapons\sniper\sniperbullet.png')
        self.speed = 48
        self.damage = 20

class ShotgunBullet(Bullet):
    def __init__(self, man, pde, owner, position=[0, 0], target=[0, 0]):
        super().__init__(man, pde, owner, position, target, sprite=r'data\topdownshooter\assets\sprites\weapons\shotgun\shotgunbullet.png')
        self.damage = 5


class SMGBullet(Bullet):
    def __init__(self, man, pde, owner, position=[0, 0], target=[0, 0]):
        super().__init__(man, pde, owner, position, target)
        self.speed = 20
        self.damage = 2

class Electrosphere(Bullet):
    def __init__(self, man, pde, owner, position=[0, 0], target=[0, 0]):
        super().__init__(man, pde, owner, position, target, scale=[16, 16], sprite=r'data\topdownshooter\assets\sprites\weapons\electrospherelauncher\electroball.png')
        self.lifetime = 300
        self.speed = 8
        self.destroyOnCollide = False
        self.checkForCollision = True
        self.mines = []
        self.trailticks = 0
        self.destroyOnOOB = False

        self.explosion = Explosion
        self.lastoverlap = None

    def update(self):
        self.trailticks += 1
        if self.trailticks >= 6:
            self.trailticks = 0
            self.mines.append(self.man.add_object(obj=Mine(man=self.man, pde=self.pde, position=self.position, rotation=self.rotation)))
            
        if self.ticks >= self.lifetime - 1:
            self.explode()
            
        return super().update()

    def collide(self, obj, side):
        if side != self.lastoverlap:
            r = random.randint(0, 100)
            if r <= 5:
                self.explode()


        if side == "Left":
            self.target = pygame.Vector2(self.target.reflect((-1,0)))
        if side == "Right":
             self.target = pygame.Vector2(self.target.reflect((1,0)))
        if side == "Top":
             self.target = pygame.Vector2(self.target.reflect((0, -1)))
        if side == "Bottom":
            self.target = pygame.Vector2(self.target.reflect((0, 1)))

        self.lastoverlap = side
        
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
        for mine in self.mines:
            mine.explode()
        e = self.man.add_object(obj=self.explosion(man=self.man, pde=self.pde, owner=self, position = self.position, scale = [128, 128]))
        self.deconstruct()

    def deconstruct(self):
        return super().deconstruct()


class SplatBullet(Bullet):
    def __init__(self, man, pde, owner, position=[0, 0], target=[0, 0]):
        self.color = random.choice(['blue', 'orange'])
        if self.color == 'orange':
            s = r'data\topdownshooter\assets\sprites\weapons\splatgun\splatorange.png'
        elif self.color == 'blue':
            s = r'data\topdownshooter\assets\sprites\weapons\splatgun\splatblue.png'
        super().__init__(man, pde, owner, position, target, sprite=s)
        self.speed = 15
        self.damage = 5
        self.splatticks = 0
        self.splattime = random.randint(10, 20)
        
    def hit(self, obj):
        self.splat()
        return super().hit(obj)

    def update(self):
        self.splatticks += 1
        if self.splatticks >= self.splattime:
            self.splat()
            self.deconstruct()
        return super().update()

    def splat(self):
        self.man.add_object(obj=Splat(man=self.man, pde=self.pde, position=list(self.rect.center), owner=self, color=self.color))

class Rocket(Bullet):
    def __init__(self, man, pde, owner, position=[0, 0], target=[0, 0]):
        super().__init__(man, pde, owner, position, target, scale = [30, 20], sprite=r'data\topdownshooter\assets\sprites\weapons\rocketlauncher\rocket.png')
        self.speed = 10
        self.damage = 15
        self.reachedTarget = False

    def update(self):
        return super().update()

    def hit(self, object):
        if isinstance(object, ShooterEntity) or isinstance(object, Tile):
            self.man.add_object(obj=Explosion(man=self.man, pde=self.pde, owner=self, position=self.rect.center, scale=[64, 64]))
        return super().hit(object)
