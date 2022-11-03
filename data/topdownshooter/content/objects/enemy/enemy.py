import gc
import random
from data.engine.actor.actor import Actor
from data.engine.ai.ai_component import AIComponent
from data.engine.debug.debugAI import debugAI
from data.engine.debug.debugController import DebugController
from data.engine.fl.world_fl import objectlookatposition, objectlookattarget
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.ai.ai_wander import WanderAI
from data.topdownshooter.content.ai.ai_weaponless import WeaponlessAI
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
from data.topdownshooter.content.objects.weapon.pickup.pickupweapon import PickupWeapon

class EnemyPickupArea(Actor):
    def __init__(self, man, pde, position):
        super().__init__(man, pde)
        self.position = position
        self.scale = [256, 256]
        self.useCenterForPosition = True
        self.checkForCollision = False

    def construct(self):
        super().construct()
        
        if self.pde.config_manager.config["config"]["debugMode"]:
            self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\mariohitbox.png', layer=2)



class ShooterEnemy(ShooterEntity):
    def __init__(self, man, pde, position=None, velocity=4, weapon=None):
        super().__init__(man, pde, position)
        self.weapon = weapon
        self.maxVelocity = velocity
        self.velocity = self.maxVelocity
        self.defaultspeed = [8, 8]
        self.speed = self.defaultspeed
        self.rotation = 0
        self.ticksSinceWeapon = 0

    def construct(self):
        super().construct()

        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\badme.png', layer=2)
        self.ai = self.components["AI"] = AIComponent(owner=self)
        self.ai.addstate(name="wander", state=WanderAI)
        self.ai.addstate(name="weaponless", state=WeaponlessAI)
        self.ai.state = "wander"

        self.area = self.man.add_object(obj=EnemyPickupArea(man=self.man, pde=self.pde, position=self.rect.center))

        if self.weapon != None:
            self.weapon = self.man.add_object(obj=self.weapon(man=self.man, pde=self.pde, owner=self, position=[self.rect.centerx + 10, self.rect.centery + 10]))



    def update(self):
        self.area.rect.center = self.rect.center


        if self.weapon != None and self.pde.game.player != None and self.pde.game.player.dead == False and self.decompose == False:
            self.weapon.shoot(target=self.pde.game.player.position)
            self.weapon.rotation = objectlookattarget(self.weapon, self.pde.game.player)

        if self.weapon is None:
            self.ticksSinceWeapon += 1
            if self.ai.state != 'weaponless':
                self.ai.state = 'weaponless'
        elif self.weapon is not None:
            if self.ai.state != 'wander':
                self.ai.state = 'wander'
            else:
                self.ticksSinceWeapon = 0
            

        return super().update()

    def deconstruct(self):
        self.area.deconstruct()
        
        return super().deconstruct()

    def takedamage(self, obj, dmg):
        return super().takedamage(obj, dmg)

    def overlap(self, obj):
        if isinstance(obj, PickupWeapon):
            self.interact()
        return super().overlap(obj)

    def die(self, killer):
        super().die(killer)
        self.queuedeconstruction()
        return

    def printDebugInfo(self):
        print(f"Referrers: {gc.get_referrers(self)}")
        return super().printDebugInfo()