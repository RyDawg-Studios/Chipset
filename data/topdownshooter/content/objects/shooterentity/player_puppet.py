import pygame
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
import data.engine.fl.world_fl as wfl



class ShooterPuppet(ShooterEntity):
    def __init__(self, man, pde, position=[0,0], maxhp=100, hp=100):
        super().__init__(man, pde, position, maxhp, hp)

    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\me.png', layer=2)

    def onNetworkUpdate(self, data):
        super().onNetworkUpdate(data)
        net_pos = pygame.Vector2(data['attributes']['position'][0])
        if wfl.getpointdistance(self.rect.centerx, self.rect.centery, net_pos[0], net_pos[1]) != 0:
            self.rect.center = pygame.Vector2(net_pos)


