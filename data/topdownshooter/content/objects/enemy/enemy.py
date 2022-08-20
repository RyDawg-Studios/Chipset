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
        self.position = position
        self.scale = [256, 256]
        self.useCenterForPosition = True
        self.checkForCollision = False
        super().__init__(man, pde)

        if self.pde.config_manager.config["config"]["debugMode"]:
            self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\mariohitbox.png', layer=2)



class ShooterEnemy(ShooterEntity):
    def __init__(self, man, pde, position=None, velocity=4, weapon=None):
        super().__init__(man, pde, position)
        self.maxVelocity = velocity
        self.velocity = self.maxVelocity
        self.player = pde.game.player
        self.defaultspeed = [8, 8]
        self.speed = self.defaultspeed
        self.rotation = 0
        self.ticksSinceWeapon = 0
        #self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\badme.png', layer=2)
        self.ai = self.components["AI"] = AIComponent(owner=self)
        self.ai.addstate(name="wander", state=WanderAI)
        self.ai.addstate(name="weaponless", state=WeaponlessAI)
        self.ai.state = "wander"

        self.area = self.man.add_object(obj=EnemyPickupArea(man=self.man, pde=self.pde, position=self.rect.center))


        if weapon != None:
            self.weapon = man.add_object(obj=weapon(man=man, pde=pde, owner=self, position=[self.rect.centerx + 10, self.rect.centery + 10]))

    def update(self):
        self.player = self.pde.game.player
        self.area.rect.center = self.rect.center


        if self.weapon != None and self.player != None and self.player.dead == False:
            print("Sees Player")
            self.weapon.shoot(target=self.player.position)
            self.weapon.rotation = objectlookattarget(self.weapon, self.player)

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

    def overlap(self, obj):
        if isinstance(obj, PickupWeapon) and self.weapon is None:
            if self.ticksSinceWeapon >= 120:
                self.interact()
        return super().overlap(obj)

    def die(self, killer):
        super().die(killer)
        self.deconstruct()
        return