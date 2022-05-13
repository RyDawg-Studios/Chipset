import random
from data.engine.ai.ai_component import AIComponent
from data.engine.debug.debugAI import debugAI
from data.engine.debug.debugController import DebugController
from data.engine.fl.world_fl import objectlookatposition, objectlookattarget
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.ai.ai_wander import WanderAI
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
from data.topdownshooter.content.objects.weapon.weapons.weapon import Weapon
from data.topdownshooter.content.objects.weapon.weapons.weapons import SMG, AutomaticRifle, DevGun, GrenadeLauncher, Shotgun, SniperRifle


class ShooterEnemy(ShooterEntity):
    def __init__(self, man, pde, position=None, scale=[32, 32], player=None, velocity=4, weapon=None):
        super().__init__(man, pde, position, scale, maxhp=100)
        self.velocity = velocity
        self.player = pde.game.player
        self.defaultspeed = [8, 8]
        self.speed = self.defaultspeed
        self.rotation = 0
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\badme.png', layer=2)
        ai = self.components["AI"] = AIComponent(owner=self)
        ai.addstate(name="default", state=WanderAI)
        w = random.choice([SMG, AutomaticRifle, SniperRifle])
        self.weapon = man.add_object(obj=weapon(man=man, pde=pde, owner=self))

    def update(self):
        self.player = self.pde.game.player

        if self.weapon != None and self.player != None and self.player.dead == False:
            self.weapon.shoot(target=self.player.position)
            self.weapon.rotation = objectlookattarget(self, self.player)
        else:
            return

        return super().update()
