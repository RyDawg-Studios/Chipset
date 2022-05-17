from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.hazard.explosion.explosion import Explosion


class Mine(Actor):
    def __init__(self, man, pde, position=[0,0], rotation=0):
        self.position = position
        self.scale = [6, 6]
        self.rotation = rotation
        self.checkForCollision = False
        super().__init__(man, pde)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\objects\mine\mine.png', layer=1)
        self.explosion = Explosion

    def update(self):
        return



    def explode(self):
        e = self.man.add_object(obj=self.explosion(man=self.man, pde=self.pde, owner=self, position = self.rect.center, scale = [32, 32]))
        self.deconstruct()