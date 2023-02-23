import pygame
from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.widgets.text import TextComponent


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

