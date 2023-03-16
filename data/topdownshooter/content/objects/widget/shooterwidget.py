import math
from data.engine.actor.actor import Actor
from data.engine.object.object import Object
from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.widgets.element.e_sprite import SpriteElement
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
        self.rect.topright=[1280-48,0]

    def updateText(self):
        self.components["Text"].sprite.text = f"Level: {self.pde.game.currentRoomNumber}"

    def update(self):
        return super().update()

    def deconstruct(self, outer=None):
        return super().deconstruct(outer)
    
class WeaponSelectorChamber(Actor):
    def __init__(self, man, pde, position=[0.0], scale=[128, 128], checkForOverlap=True, checkForCollision=True, useCenterForPosition=False, lifetime=-1, owner=None):
        super().__init__(man, pde, position, scale, checkForOverlap, checkForCollision, useCenterForPosition, lifetime)
        self.scale = [128, 127]
        self.owner = owner
        self.owner.onSwitchWeaponEvent.bind(self.onWeaponSwitch)
        self.sprites = [r'data\topdownshooter\assets\sprites\ui\inventory\chamber_0.png', r'data\topdownshooter\assets\sprites\ui\inventory\chamber_1.png', 
                        r'data\topdownshooter\assets\sprites\ui\inventory\chamber_2.png', r'data\topdownshooter\assets\sprites\ui\inventory\chamber_3.png',
                        r'data\topdownshooter\assets\sprites\ui\inventory\chamber_4.png', r'data\topdownshooter\assets\sprites\ui\inventory\chamber_5.png',
                        r'data\topdownshooter\assets\sprites\ui\inventory\chamber_6.png']
        self.rotations = [0, 60, 120, 180, 240, 300]

        self.targetRotation = 0

    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\ui\inventory\chamber_0.png', layer=5)

    def onWeaponSwitch(self, current, index):
        self.components["Sprite"].deconstruct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=self.sprites[len(self.owner.weapons)], layer=5)
        self.components["Sprite"].sprite.rotation = self.rotations[current-1]

        if self.rotations[index-1] != self.targetRotation:
            self.targetRotation = self.rotations[index-1]

    def update(self):
        super().update()

        if self.components["Sprite"].sprite.rotation < self.targetRotation:
            self.components["Sprite"].sprite.rotation += round(abs(self.components["Sprite"].sprite.rotation-self.targetRotation) / 10, 2)
        elif self.components["Sprite"].sprite.rotation > self.targetRotation:
            self.components["Sprite"].sprite.rotation -= round(abs(self.components["Sprite"].sprite.rotation-self.targetRotation) / 10, 2)
        else:
            return
    
class WeaponSelector(Actor):
    def __init__(self, man, pde, position=[0,0], scale=[0,0], checkForOverlap=True, checkForCollision=True, useCenterForPosition=False, lifetime=-1, owner=None):
        super().__init__(man, pde, position, scale, checkForOverlap, checkForCollision, useCenterForPosition, lifetime)
        self.owner = owner
        
    def construct(self):
        super().construct()
        self.chamber = self.man.add_object(obj=WeaponSelectorChamber(man=self.man, pde=self.pde, position=[0,0], scale=[64, 64], owner=self.owner))
        

    def update(self):
        super().update()




        
    
class ShooterWidget(Actor):
    def __init__(self, man, pde, position=[0,0], scale=[0,0], checkForOverlap=False, checkForCollision=False, useCenterForPosition=False, lifetime=-1, owner=None):
        super().__init__(man, pde, position, scale, checkForOverlap, checkForCollision, useCenterForPosition, lifetime)
        self.owner = owner

    def construct(self):
        super().construct()
        self.levelText = self.man.add_object(obj=LevelText(man=self.man, pde=self.pde))
        self.inventory = self.man.add_object(obj=WeaponSelector(man=self.man, pde=self.pde, owner=self.owner))


