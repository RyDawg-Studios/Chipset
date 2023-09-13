import pygame
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.player.net_shooter_player import NetShooterPlayer
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
import data.engine.fl.world_fl as wfl



class ShooterPuppet(NetShooterPlayer):
    def __init__(self, man, pde, position=[0,0], hp=100):
        super().__init__(man, pde, position, hp)
        self.controller = None

    def settargetposition(self):
        return 



