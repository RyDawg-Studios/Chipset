from data.engine.actor.actor import Actor
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.weapon.hitmarker.hitmarker import Hitmarker
from data.topdownshooter.content.tiles.tile import Tile
from data.engine.fl.world_fl import getobjectlookatvector, getpositionlookatvector, objectlookatposition, objectlookattarget

class Bullet(Actor):
    def __init__(self, man, pde, owner, position=[0,0], target=[0, 0], scale=[14, 7], sprite=r'data\topdownshooter\assets\sprites\debug\debugweapon\rocket.png'):
        self.checkForCollision = False
        self.useCenterForPosition = True
        self.scale = scale
        self.position = position
        self.speed = 12
        self.damage = 1
        self.owner = owner
        self.kb = 2
        self.destroyOnCollide = True
        self.ignoreCollides = []
        
        super().__init__(man, pde)

        self.target = getpositionlookatvector(self, target)
        self.rotation = objectlookatposition(self, self.position + self.target)

        self.movement = self.target * self.speed
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=sprite, layer=2)


    def update(self):
        self.movement = self.target * self.speed
        self.components["Sprite"].sprite.rotation = self.rotation

        if self.position[0] < -80 or self.position[1] < -80:
            self.deconstruct()
        elif self.position[0] > 720 or self.position[1] > 560:
            self.deconstruct()
        return super().update()


    def onshot(self):
        pass

    def overlap(self, obj):
        if self.ticks >= 2:
            if obj != self.owner and obj != self.owner.owner:
                if hasattr(obj, 'hp'):
                    obj.takedamage(self)
                    self.man.add_object(obj=Hitmarker(man=self.man, pde=self.pde, position=self.position))
                    if self.destroyOnCollide:
                        self.deconstruct()
                elif isinstance(obj, Tile):
                    if self.destroyOnCollide:
                        self.deconstruct()
                        
        return super().overlap(obj)