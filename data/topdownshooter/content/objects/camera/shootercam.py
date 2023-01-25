import pygame
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import *
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent


class ShooterCamera(Actor):
    def __init__(self, man, pde, target, position=[0, 0]):
        super().__init__(man, pde)
        self.position = position
        self.checkForCollision = False
        self.checkForOverlap = False
        self.scale = [32, 32]
        self.speed = [8, 8]
        self.target = target
        
        


    def construct(self):
        super().construct()
        if self.pde.config_manager.config["config"]["debugMode"]:
            self.sprite = self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\camera.png', layer=8)
        else:
            self.sprite = None

        self.components["Projectile"] = ProjectileComponent(owner=self, speed=self.speed)

    def update(self):

        self.scrollcameratocenterx()
        self.scrollcameratocentery()


        self.rect.centerx = round(self.target.position[0] - ((self.target.position[0] - self.pde.mouse_manager.pos[0]) / 5))

        self.rect.centery = round(self.target.position[1] - ((self.target.position[1] - self.pde.mouse_manager.pos[1]) / 4))

        
        return super().update()


    def deconstruct(self):
        self.target = None
        return super().deconstruct()