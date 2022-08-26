import random
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import getobjectdistance, getpositionlookatvector, objectlookattarget
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.hazard.explosion.explosion import Explosion
from data.topdownshooter.content.objects.weapon.bullets.bullet import Bullet


class MagnetArea(Actor):
    def __init__(self, man, pde, owner, position=[0,0]):
        self.position = position
        self.scale = [128, 128]
        self.checkForCollision = False
        self.owner = owner
        super().__init__(man, pde)

        if self.pde.config_manager.config["config"]["debugMode"]:
            self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\mariohitbox.png', layer=2)
    
    def overlap(self, obj):
        if isinstance(obj, Bullet):
            obj.rotation = objectlookattarget(obj, self)
            obj.target = getpositionlookatvector(self, obj.position) *-1
            if obj not in self.owner.attached:
                self.owner.attached.append(obj)
                obj.destroyOnOOB = False
        return super().overlap(obj)

    def deconstruct(self):
        self.owner = None
        return super().deconstruct()


class Magnet(Actor):
    def __init__(self, man, pde, position=[0,0], rotation=0):
        self.position = position
        self.scale = [3,24]
        self.rotation = rotation
        self.checkForCollision = False
        self.attached = []
        self.lifetime = 400
        super().__init__(man, pde)
        self.area = self.man.add_object(MagnetArea(man=self.man, pde=pde, owner=self, position=self.position))
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\objects\magnet\magnet.png', layer=1)
        self.explosion = Explosion


    def update(self):
        if len(self.attached) > 20:
            self.attached[0].deconstruct(outer=self)
            self.attached.remove(self.attached[0])
        self.area.rect.center = self.rect.center
        return super().update()

    def explode(self):
        e = self.man.add_object(obj=self.explosion(man=self.man, pde=self.pde, owner=self, position = self.rect.center, scale = [32, 32]))
        self.deconstruct()

    def deconstruct(self):
        for b in self.attached:
            b.destroyOnOOB = True
        self.area.deconstruct()
        return super().deconstruct()