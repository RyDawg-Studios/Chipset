from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity


class Hole(Actor):
    def __init__(self, man, pde, position=[0, 0], sprite=r'data\topdownshooter\assets\sprites\objects\hole\hole.png'):
        super().__init__(man, pde)
        self.position = position
        self.scale =[32, 32]
        self.useCenterForPosition = True
        self.checkForCollision = False
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=sprite, layer=0)

    def overlap(self, obj):
        if isinstance(obj, ShooterEntity):
            if self.rect.collidepoint(obj.rect.center):
                obj.falling = True



        return super().overlap(obj)