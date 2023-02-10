import random
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import getobjectlookatvector, getpositionlookatvector, objectlookattarget
from data.engine.particle.particle_emitter import ParticleEmitter
from data.topdownshooter.content.objects.particles.blood import Blood
from data.topdownshooter.content.objects.weapon.bullets.bullet import Bullet
from data.topdownshooter.content.objects.weapon.pickup.pickupweapon import PickupWeapon
from data.topdownshooter.content.objects.widget.shooterwidget import HealthBar


class ShooterEntity(Actor):
    def __init__(self, man, pde, position=[0, 0], scale=[32, 32], maxhp=100):
        super().__init__(man, pde, useCenterForPosition=True)
        #----------< Transform Info >----------#

        self.position = position
        self.scale = scale
        self.maxVelocity = 0


        #----------< Weapon Info >----------#
        
        self.weapon = None
        self.weaponoffset = 10
        self.item = None

        #----------< Stat Info >----------#

        self.maxhp = maxhp
        self.hp = self.maxhp
        self.dead = False
        self.damagable = True
        self.falling = False
        self.canGrantHP = True
        self.speed = 3

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
        
        #----------< Visual Info >----------#

        self.bleed = False

        #----------< Timer Info >----------#

        self.deadticks = 0

    def construct(self):
        super().construct()

        self.components["Particle"] = ParticleEmitter(owner=self)

        self.healthbar = self.man.add_object(obj=HealthBar(man=self.man, pde=self.pde, owner=self))
        return

    def shootweapon(self, target):
        if self.weapon != None and self.canShoot:
            shot = self.weapon.shoot(target, self.weapon.bullet)
            return shot

    def altShot(self, target):
        if self.weapon != None:
            self.weapon.altShot(target)


    def update(self):
        
        if self.dead:
            self.deadticks += 1

        self.dodgebuffer()
        self.offsetweapon(weapon=self.weapon, offset=self.weaponoffset)

        if self.falling:
            self.fall()
        if self.speed > 3:
            self.speed -= 0.4
        return super().update()

    def takedamage(self, obj, dmg):
        if self.bleed:
            bleed = random.choice([True, False])
            if bleed:
                #self.components["Particle"].particles.append(self.components["Particle"].templates["blood"])
                pass
        if self.damagable:
            self.hp -= dmg
            if self.hp <= 0 and self.hp != -1:
                if not self.dead:
                    self.die(obj)
            return True
        else:
            return False

    def dodgeroll(self):
        self.speed = 10
        return

    def dodgebuffer(self):
        self.dodgecooldown += 1
        if self.dodgecooldown >= self.dodgecooldowntime:
            if self.dodging:
                self.dodgeroll()
                self.dodgecooldown = 0
                self.dodging = False
        else:
            self.dodging = False
        return

    def die(self, killer):
        self.dead = True
        if killer is not None:
            rot = killer.rotation
            self.dropweapon(rot)
        else:
            self.removeweapon()
        if self.weapon != None:
            self.weapon.queuedeconstruction()


    def offsetweapon(self, weapon, offset=10):
        if weapon != None:
            weapon.rect.centerx = self.rect.centerx + offset
            weapon.rect.centery = self.rect.centery + offset

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
        self.removeweapon()
        self.weapon = self.man.add_object(obj=cls(man=self.man, pde=self.pde, owner=self, position=[self.rect.centerx + 10, self.rect.centery + 10]))
        return

    def removeweapon(self):
        if self.weapon is not None:
            self.weapon.queuedeconstruction()
            self.weapon = None

    def useitem(self, item):
        item.use()
        return

    def checkXcollision(self, movement):
        if self.canMove:
            self.rect.x += self.movement.x * round(self.speed)
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
        return

    def checkYcollision(self, movement):
        if self.canMove:
            self.rect.y += self.movement.y * round(self.speed)
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
        return

    def fall(self):
        self.canMove = False
        self.takedamage(obj=None, dmg=10)
        self.removeweapon()
        if self.rect.height > 0 and self.rect.width > 0:
            self.rect.height -= 1
            self.rect.width -= 1
        else:
            self.die(killer=None)

    def deconstruct(self):
        self.healthbar.deconstruct()
        self.healthbar = None
        return super().deconstruct()