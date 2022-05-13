from turtle import pos
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import getobjectlookatvector, getpositionlookatvector, objectlookattarget
from data.topdownshooter.content.objects.weapon.bullets.bullet import Bullet
from data.topdownshooter.content.objects.weapon.hitmarker.hitmarker import Hitmarker
from data.topdownshooter.content.objects.weapon.pickup.pickupweapon import PickupWeapon
from data.topdownshooter.content.objects.widget.shooterwidget import HealthBar


class ShooterEntity(Actor):
    def __init__(self, man, pde, position=None, scale=[32, 32], maxhp=100):

        #----------< Transform Info >----------#
        if position is None: position = [0,0]
        self.position = position
        self.scale = scale
        self.useCenterForPosition = True

        #----------< Weapon Info >----------#
        
        self.weapon = None
        self.item = None

        #----------< Stat Info >----------#

        self.maxhp = maxhp
        self.hp = self.maxhp
        self.dead = False
        self.damagable = True

        #----------< Dodge Info >----------#

        self.dodgeframe = 0
        self.dodgetime = 10
        self.dodging = False
        self.dodgecooldown = 200
        self.dodgecooldowntime = 50

        #----------< Tag Info >----------#
        
        self.homable = True
        self.canPickupWeapons = True
        self.canCollectExp = True
        self.canShoot = True

        #----------< Timer Info >----------#

        self.deadticks = 0


        super().__init__(man, pde)

        self.healthbar = man.add_object(obj=HealthBar(man=man, pde=pde, owner=self))


    def shootweapon(self, target):
        if self.weapon != None and self.canShoot:
            shot = self.weapon.shoot(target)
            return shot

    def update(self):
        if self.dead:
            self.deadticks += 1
        self.dodgebuffer()
        self.weaponoffset()
        return super().update()

    def collide(self, obj, side):
        return super().collide(obj, side)

    def takedamage(self, obj):
        if self.damagable:
            self.hp -= obj.damage
            if self.hp <= 0:
                if not self.dead:
                    self.dead = True
                    self.die(obj)
            return True
        else:
            return False

    def dodgeroll(self):
        self.damagable = False
        if self.movement[0] != 0 and abs(self.movement[0]) == abs(self.movement[1]):
            self.rect.centerx += (self.movement[0] * 3) * 0.6
            self.rect.centery += (self.movement[1] * 3) * 0.6
        else:
            self.rect.centerx += (self.movement[0] * 3)
            self.rect.centery += (self.movement[1] * 3)

    def dodgebuffer(self):
        self.dodgecooldown += 1
        if self.dodgecooldown >= self.dodgecooldowntime:
            if self.dodging:
                self.dodgeframe += 1
                self.dodgeroll()
                if self.dodgeframe >= self.dodgetime:
                    self.dodging = False
                    self.dodgeframe = 0
                    self.dodgecooldown = 0
                    self.damagable = True
        else:
            self.dodging = False


    def die(self, killer):
        rot = killer.rotation
        self.dropweapon(rot)
        if self.weapon != None:
            self.weapon.deconstruct()
        self.deconstruct()

    def weaponoffset(self):
        if self.weapon != None:
            self.weapon.rect.centerx = self.rect.centerx + 10
            self.weapon.rect.centery = self.rect.centery + 10

    def dropweapon(self, rotation=0):
        if self.weapon != None:
            self.man.add_object(obj=PickupWeapon(man=self.man, pde=self.pde, position=list(self.rect.center), rotation=rotation, weapon=self.weapon, speed=[4, 4]))
            self.removeweapon()

    def interact(self):
        for o in self.overlapInfo["Objects"]:
            if o.__class__ == PickupWeapon:
                if self.canPickupWeapons:
                    self.dropweapon(rotation=objectlookattarget(self, o))
                    self.changeweapon(o.weapon.__class__)
                    o.deconstruct()
                    return
            

    def changeweapon(self, cls):
        self.weapon = self.man.add_object(obj=cls(man=self.man, pde=self.pde, owner=self))

    def removeweapon(self):
        if self.weapon != None:
            self.weapon.deconstruct()
            self.weapon = None

    def useitem(self, item):
        item.use()

    def checkXcollision(self, movement):
        if self.canMove:
            self.rect.x += self.movement.x * self.velocity
            hits = self.getoverlaps()  
            for object in hits:
                if hasattr(object, 'checkForCollision') and object.checkForCollision and self.checkForCollision:
                    if not isinstance(object, Bullet):
                        if object not in self.collideInfo["Objects"]:
                            self.collideInfo["Objects"].append(object)
                        if movement[0] > 0:
                            self.rect.right = object.rect.left
                            self.collideInfo["Right"] = True
                            object.collide(self, "Left")
                        elif movement[0] < 0:
                            self.rect.left = object.rect.right
                            self.collideInfo["Left"] = True
                            object.collide(self, "Right")

    def checkYcollision(self, movement):
        if self.canMove:
            self.rect.y += self.movement.y * self.velocity
            hits = self.getoverlaps()  
            for object in hits:
                if hasattr(object, 'checkForCollision') and object.checkForCollision and self.checkForCollision:
                    if not isinstance(object, Bullet):
                        if object not in self.collideInfo["Objects"]:
                            self.collideInfo["Objects"].append(object)
                        if movement[1] > 0:
                            self.rect.bottom = object.rect.top
                            self.collideInfo["Bottom"] = True
                            object.collide(self, "Top")
                        elif movement[1] < 0:
                            self.rect.top = object.rect.bottom
                            self.collideInfo["Top"] = True
                            object.collide(self, "Bottom")

    def deconstruct(self):
        self.healthbar.deconstruct()
        return super().deconstruct()