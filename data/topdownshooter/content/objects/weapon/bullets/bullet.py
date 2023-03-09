from data.engine.actor.actor import Actor
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.weapon.hitmarker.hitmarker import Hitmarker
from data.topdownshooter.content.tiles.tile import Tile
from data.engine.fl.world_fl import getobjectlookatvector, getpositionlookatvector, objectlookatposition, objectlookattarget

class Bullet(Actor):
    def __init__(self, man, pde, owner, position=[0,0], target=[0, 0], scale=[20, 4], sprite=r'data\topdownshooter\assets\sprites\weapons\assaultrifle\assaultriflebullet.png'):
        super().__init__(man, pde)
        self.target = target
        self.spritePath = sprite
        self.checkForCollision = False
        self.scale = scale
        self.position = position
        self.speed = 24
        self.damage = 2
        self.owner = owner
        self.kb = 2
        self.destroyOnCollide = True
        self.ignoreCollides = []
        self.destroyOnOOB = True
        self.useCenterForPosition = True
        self.piercing = False


    def construct(self):
        super().construct()
        self.target = getpositionlookatvector(self, self.target)
        self.rotation = objectlookatposition(self, self.position + self.target)
        self.movement = self.target * self.speed
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=self.spritePath, layer=1)

    def update(self):
        super().update()
        if not self.paused:
            self.components["Sprite"].sprite.rotation = self.rotation

            for upg in self.owner.upgrades:
                upg.onBulletUpdate(bullet=self)

            self.movement = self.target * self.speed

            if self.destroyOnOOB:
                if self.rect.centerx not in range(0, self.pde.config_manager.config["config"]["dimensions"][0]) and self.rect.centery not in range(0, self.pde.config_manager.config["config"]["dimensions"][1]):
                    self.deconstruct()

    def onshot(self):
        pass

    def overlap(self, obj):
        super().overlap(obj)
        if obj != self.owner and obj != self.owner.owner:
            for upg in self.owner.upgrades:
                upg.onHit(bullet=self, damage=self.damage, object=obj)
            if hasattr(obj, 'hp'):
                obj.takedamage(self, self.damage * self.owner.damagemultiplier)
                if len(self.pde.display_manager.userInterface.objects) < 16:
                    self.pde.display_manager.userInterface.add_object(obj=Hitmarker(man=self.pde.display_manager.userInterface, pde=self.pde, position=self.position))
                self.hit(obj)
                if self.destroyOnCollide and not self.piercing:
                    self.deconstruct()
                    return True
            elif isinstance(obj, Tile):
                self.hit(obj)
                if self.destroyOnCollide:
                        self.deconstruct()
                        return True
                        

    def hit(self, obj):
        return

    def deconstruct(self, outer=None):
        super().deconstruct(outer)
        for upg in self.owner.upgrades:
            upg.onBulletDestruction(bullet=self)