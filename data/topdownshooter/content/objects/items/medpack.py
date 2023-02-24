import random
from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.player.player import ShooterPlayer


class Medpack(Actor):
    def __init__(self, man, pde, position=[0,0], scale=[24, 24], checkForOverlap=True, checkForCollision=False, useCenterForPosition=True, lifetime=-1):
        super().__init__(man, pde, position, scale, checkForOverlap, checkForCollision, useCenterForPosition, lifetime)
        self.sprite = ""


    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=self.sprite, layer=0)



    def overlap(self, obj):
        super().overlap(obj)
        if isinstance(obj, ShooterPlayer):
            obj.hp += 75
            self.deconstruct()