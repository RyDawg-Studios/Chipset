from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.widgets.element.e_button import ButtonElement
from data.engine.widgets.text import TextComponent
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
import pygame




class Dummy(ShooterEntity):
    def __init__(self, man, pde, position=[0, 0], maxhp=100):
        super().__init__(man, pde, position, maxhp)
        self.scale = [32, 48]
        self.canGrantHP = False
        self.bleed = True
        self.damagecount = 0
        self.frames = 0
        self.totaldamage = 0
        self.timestakendamage = 0

    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\objects\dummy\dummy.png',layer=2)
        self.components["Text"] = TextComponent(owner=self, text=str(self.damagecount), font=pygame.font.SysFont('impact.ttf', 72), layer=3)

    def die(self, killer):
        self.hp = 100

    def takedamage(self, obj, dmg):
        self.damagecount += dmg   
        self.totaldamage += dmg   
        self.timestakendamage += 1  
        self.getcomponent("Text").sprite.text = str(round(self.damagecount))
        return super().takedamage(obj, dmg)

    def update(self):
        self.frames += 1
        if self.frames > 60:
            self.frames = 0
            self.damagecount = 0
            self.timestakendamage = 0
        return super().update()
