from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.hazard.explosion.explosion import Explosion
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity


class Hole(Actor):
    def __init__(self, man, pde, position=[0, 0], sprite=r'data\topdownshooter\assets\sprites\objects\hole\hole.png'):
        super().__init__(man, pde)
        self.sprite = sprite
        self.position = position
        self.scale =[32, 32]
        self.useCenterForPosition = True
        self.checkForCollision = False

    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=self.sprite, layer=0)
        self.man.add_object(Explosion(man=self.man, pde=self.pde, owner=self, position=self.position, scale=[128, 128], damage=0))

    def overlap(self, obj):
        super().overlap(obj)
        if isinstance(obj, ShooterEntity):
            if self.rect.collidepoint(obj.rect.center):
                self.pde.game.next_room()


