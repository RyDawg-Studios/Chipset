import json
import pygame
from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.widgets.text import TextComponent

class NameText(Actor):
    def __init__(self, man, pde, position=[0,0], box=None):
        super().__init__(man, pde)
        self.position = position
        self.scale = [100, 20]
        self.box = box
        self.checkForCollision = False
        self.checkForOverlap = False
        self.useCenterForPosition = True


    def construct(self):
        super().construct()
        self.components["nametext"] = TextComponent(owner=self, text=self.box.weapon.name, font=pygame.font.SysFont('impact.ttf', 16), layer=3)

    def update(self):
        self.rect.topleft = [self.box.rect.topleft[0] + 5, self.box.rect.topleft[1] + 5]
        return super().update()

class FireRateText(Actor):
    def __init__(self, man, pde, position=[0,0], box=None):
        super().__init__(man, pde)
        self.position = position
        self.scale = [70, 12]
        self.box = box
        self.checkForCollision = False
        self.checkForOverlap = False
        self.useCenterForPosition = False

    def construct(self):
        super().construct()
        self.components["frtext"] = TextComponent(owner=self, text=f"Shot Delay: {self.box.weapon.firerate}", font=pygame.font.SysFont('impact.ttf', 12), layer=3)
        self.rect.topleft = [self.box.rect.topleft[0]+ 5, self.box.rect.topleft[1] + 27]

    def update(self):
        super().update()
        self.rect.topleft = [self.box.rect.topleft[0]+ 5, self.box.rect.topleft[1] + 27]

class DamageMultText(Actor):
    def __init__(self, man, pde, position=[0,0], box=None):
        super().__init__(man, pde)
        self.position = position
        self.scale = [80, 12]
        self.box = box
        self.checkForCollision = False
        self.checkForOverlap = False
        self.useCenterForPosition = False

    def construct(self):
        super().construct()
        self.components["multtext"] = TextComponent(owner=self, text=f"Damage Multiplier: x{self.box.weapon.damagemultiplier}", font=pygame.font.SysFont('impact.ttf', 12), layer=3)
        self.rect.topleft = [self.box.rect.topleft[0]+5, self.box.rect.topleft[1] + 37]

    def update(self):
        super().update()
        self.rect.topleft = [self.box.rect.topleft[0]+5, self.box.rect.topleft[1] + 37]

class AccuracyText(Actor):
    def __init__(self, man, pde, position=[0,0], box=None):
        super().__init__(man, pde)
        self.position = position
        self.scale = [50, 12]
        self.box = box
        self.checkForCollision = False
        self.checkForOverlap = False
        self.useCenterForPosition = False

    def construct(self):
        super().construct()
        self.components["acctext"] = TextComponent(owner=self, text=f"Spread: {self.box.weapon.shotspread}", font=pygame.font.SysFont('impact.ttf', 12), layer=3)
        self.rect.topleft = [self.box.rect.topleft[0]+5, self.box.rect.topleft[1] + 47]


    def update(self):
        self.rect.topleft = [self.box.rect.topleft[0]+5, self.box.rect.topleft[1] + 47]
        return super().update()

class UpgradeIcon(Actor):
    def __init__(self, man, pde, id="Empty", num=0, box=None):
        super().__init__(man, pde)
        self.offsets = [[30, -50], [75, -50], [120, -50]]
        self.position = [box.rect.bottomleft[0]+self.offsets[num][0], box.rect.bottomleft[1]+self.offsets[num][1]]
        self.scale = [35,35]
        self.id = id
        self.num = num
        self.box = box
        self.useCenterForPosition = True
        self.checkForCollision = False
        self.useCenterForPosition = True
        self.upgradedata = json.load(open(r"data\topdownshooter\data\upgradedata.json"))

    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=self.upgradedata[self.id]["spriteinfo"]["sprite"], layer=3)
        return


    def update(self):
        self.rect.center = [self.box.rect.bottomleft[0]+self.offsets[self.num][0], self.box.rect.bottomleft[1]+self.offsets[self.num][1]]
        return super().update()


class UpgradeContainer(Actor):
    def __init__(self, man, pde, weapon, box):
        super().__init__(man, pde)
        self.weapon = weapon
        self.upgrades = ["Empty", "Empty", "Empty"]
        self.box = box
        for inx, upgrade in enumerate(self.weapon.upgrades):
            self.upgrades[inx] = upgrade.id 
        self.icons = []
        for inx, u in enumerate(self.upgrades):
            i = self.man.add_object(UpgradeIcon(man=self.man, pde=self.pde, box=self.box, id=u, num=inx))
            self.icons.append(i)

    def deconstruct(self):
        for i in self.icons:
            i.deconstruct()
        return super().deconstruct()




class InfoBox(Actor):
    def __init__(self, man, pde, weapon=None):
        super().__init__(man, pde)
        self.scale = [150, 200]
        self.position = [pde.input_manager.mouse_position[0], pde.input_manager.mouse_position[1] - self.scale[1]]
        self.weapon = weapon
        self.checkForCollision = False
        self.checkForOverlap = False
        self.useCenterForPosition = True

    
    def construct(self):
        super().construct()
        self.sprite = self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\ui\infobox\infobox.png', layer=3)
        self.sprite.sprite.opacity = 150
        self.nametext = self.man.add_object(NameText(man=self.man, pde=self.pde, position=self.rect.topleft, box=self))
        self.fireratetext = self.man.add_object(FireRateText(man=self.man, pde=self.pde, position=self.rect.topleft, box=self))
        self.damagemulttext = self.man.add_object(DamageMultText(man=self.man, pde=self.pde, position=self.rect.topleft, box=self))
        self.accuracytext = self.man.add_object(AccuracyText(man=self.man, pde=self.pde, position=self.rect.topleft, box=self))
        self.upgradeicons = self.man.add_object(UpgradeContainer(man=self.man, pde=self.pde, box=self, weapon=self.weapon))
        if self.rect.topright[0] >= 640:
            self.allignment = "left"
        else:
            self.allignment = "right"
        self.rect.bottomleft = self.pde.input_manager.mouse_position



    def update(self):
        if self.allignment == "left":
            self.rect.bottomright = self.pde.input_manager.mouse_position
        else:
            self.rect.bottomleft = self.pde.input_manager.mouse_position
        return super().update()

    def deconstruct(self):
        self.nametext.deconstruct()
        self.fireratetext.deconstruct()
        self.damagemulttext.deconstruct()
        self.accuracytext.deconstruct()
        self.upgradeicons.deconstruct()
        return super().deconstruct()
