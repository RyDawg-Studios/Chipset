import gc
import random
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import objectlookatposition, objectlookattarget
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
from data.topdownshooter.content.objects.weapon.pickup.pickupweapon import PickupWeapon



class ShooterEnemy(ShooterEntity):
    def __init__(self, man, pde, position=None, velocity=4, weapon=None):
        super().__init__(man, pde, position)
        self.weapon = weapon
        self.maxVelocity = velocity
        self.velocity = self.maxVelocity
        self.speed = 3
        self.rotation = 0
        self.ticksSinceWeapon = 0
        self.bleed = True
        self.handeling = random.randint(85, 100) / 100

    def construct(self):
        super().construct()


        if self.weapon != None:
            self.weapon = self.man.add_object(obj=self.weapon(man=self.man, pde=self.pde, owner=self, position=[self.rect.centerx + 10, self.rect.centery + 10]))



    def update(self):
        super().update()

        if self.weapon != None and self.pde.game.player != None and self.pde.game.player.dead == False and self.decompose == False:
            self.weapon.shoot(target=self.pde.game.player.position, bullet=self.weapon.bullet)
            self.weapon.rotation = objectlookattarget(self.weapon, self.pde.game.player)


    def deconstruct(self):
        
        return super().deconstruct()

    def takedamage(self, obj, dmg):
        return super().takedamage(obj, dmg)

    def overlap(self, obj):
        if isinstance(obj, PickupWeapon):
            self.interact()
        return super().overlap(obj)

    def die(self, killer):
        super().die(killer)
        self.deconstruct()
        return

    def printDebugInfo(self):
        print(f"Referrers: {gc.get_referrers(self)}")
        return super().printDebugInfo()