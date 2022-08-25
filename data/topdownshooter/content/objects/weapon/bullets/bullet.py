from data.engine.actor.actor import Actor
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.weapon.hitmarker.hitmarker import Hitmarker
from data.topdownshooter.content.tiles.tile import Tile
from data.engine.fl.world_fl import getobjectlookatvector, getpositionlookatvector, objectlookatposition, objectlookattarget

class Bullet(Actor):
    def __init__(self, man, pde, owner, position=[0,0], target=[0, 0], scale=[20, 4], sprite=r'data\topdownshooter\assets\sprites\weapons\assaultrifle\assaultriflebullet.png'):
        self.checkForCollision = False
        self.scale = scale
        self.position = position
        self.speed = 24
        self.damage = 4
        self.owner = owner
        self.kb = 2
        self.destroyOnCollide = True
        self.ignoreCollides = []
        self.destroyOnOOB = True
        self.useCenterForPosition = True
        super().__init__(man, pde)
        self.target = getpositionlookatvector(self, target)
        self.rotation = objectlookatposition(self, self.position + self.target)
        self.movement = self.target * self.speed
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=sprite, layer=1)




    def update(self):
        for upg in self.owner.upgrades:
            upg.onBulletUpdate(bullet=self)

        self.movement = self.target * self.speed
        self.components["Sprite"].sprite.rotation = self.rotation

        if self.destroyOnOOB:
            if self.position[0] < -80 or self.position[1] < -80:
                self.deconstruct()
            elif self.position[0] > 720 or self.position[1] > 560:
                self.deconstruct()

        return super().update()


    def onshot(self):
        pass

    def overlap(self, obj):
        print(f"Overlapped with {obj.__class__.__name__}")
        if self.ticks >= 2:
            if obj != self.owner and obj != self.owner.owner:
                for upg in self.owner.upgrades:
                    upg.onHit(bullet=self, damage=self.damage, object=obj)
                if hasattr(obj, 'hp'):
                    obj.takedamage(self, self.damage * self.owner.damagemultiplier)
                    self.man.add_object(obj=Hitmarker(man=self.man, pde=self.pde, position=self.position))
                    self.hit(obj)
                    if self.destroyOnCollide:
                        self.man.remove_object(self)
                        self.deconstruct()
                elif isinstance(obj, Tile):
                    self.hit(obj)
                    if self.destroyOnCollide:
                        self.deconstruct()
                        
        return super().overlap(obj)

    def hit(self, obj):
        return

    def deconstruct(self):
        for upg in self.owner.upgrades:
            upg.onBulletDestruction(bullet=self)
        return super().deconstruct()