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

        dist = abs(math.hypot(self.rect.centerx - self.target.rect.centerx, self.rect.centery-self.target.rect.centery))
        if dist < 50:
            self.speed = [dist/10, dist/10]
        
        if dist > 150:
            if self.speed[0] < 8:
                self.speed[0] += 0.1
                self.speed[1] += 0.1
        else:
            if self.speed[0] > 4:
                self.speed[0] -= 0.1
                self.speed[1] -= 0.1



        self.rotation = objectlookattarget(self, self.target)
        self.components["Projectile"].speed = self.speed
        if self.sprite is not None:
            self.components["Sprite"].sprite.rotation = self.rotation
        
        return super().update()


    def deconstruct(self):
        self.target = None
        return super().deconstruct()