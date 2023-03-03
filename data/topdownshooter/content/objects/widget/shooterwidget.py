from data.engine.actor.actor import Actor
from data.engine.object.object import Object
from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.widgets.text import TextComponent
import pygame

class HealthBar(Actor):
    def __init__(self, man, pde, owner=None):
        super().__init__(man, pde)
        self.checkForCollision = False
        self.checkForOverlap = False
        self.owner = owner
        self.scale = [40, 2]

    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\ui\healthbar\bar.png', layer=6)

    def update(self):
        self.rect.centerx= self.owner.position.x
        self.rect.centery = self.owner.position.y - 24
        if self.owner.hp > 0:
            self.rect.width = (self.owner.hp / self.owner.maxhp )* 40
        else:
            self.rect.width = 0
        return super().update()
    
class LevelText(Actor):
    def __init__(self, man, pde):
        super().__init__(man, pde)
        self.checkForCollision = False
        self.checkForOverlap = False
        self.scale = [48, 48]

    def construct(self):
        super().construct()
        self.components["Text"] = TextComponent(owner=self, text=f"Level: {self.pde.game.currentRoomNumber}", font=pygame.font.SysFont('impact.ttf', 48), layer=5)
        self.rect.topright=[640-48,0]

    def updateText(self):
        self.components["Text"].sprite.text = f"Level: {self.pde.game.currentRoomNumber}"

    def update(self):
        return super().update()

    def deconstruct(self, outer=None):
        return super().deconstruct(outer)
    
class ShooterWidget(Actor):
    def __init__(self, man, pde, position=[0,0], scale=[0,0], checkForOverlap=False, checkForCollision=False, useCenterForPosition=False, lifetime=-1):
        super().__init__(man, pde, position, scale, checkForOverlap, checkForCollision, useCenterForPosition, lifetime)

    def construct(self):
        super().construct()
        self.levelText = self.man.add_object(obj=LevelText(man=self.man, pde=self.pde))


