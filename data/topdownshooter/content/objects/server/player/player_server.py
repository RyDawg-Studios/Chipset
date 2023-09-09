import pygame
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import objectlookatposition
from data.engine.particle.particle_emitter import ParticleEmitter
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.camera.shootercam import ShooterCamera
from data.topdownshooter.content.objects.hazard.magnet.magnet import Magnet
from data.topdownshooter.content.objects.player.net_shooter_controller import NetShooterController
from data.topdownshooter.content.objects.player.player import ShooterPlayer
from data.topdownshooter.content.objects.server.player.client_linked_shooter_controller import ClientLinked_ShooterController
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
from data.topdownshooter.content.objects.widget.fadeout import FadeOut
from data.topdownshooter.content.objects.widget.shooterwidget import ShooterWidget
import data.topdownshooter.content.objects.weapon.upgrade.upgrades as u

class Crosshair(Actor):
    def __init__(self, man, pde, position) -> None:
        super().__init__(man=man, pde=pde, position=position, scale=[32, 32], useCenterForPosition=True)

    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\ui\hud\reticle.png', layer=5)

class ShooterPlayerServer(ShooterPlayer):
    def __init__(self, man, pde, client=(0,0), position=[0,0], hp=400):
        super().__init__(man, pde, position, hp)
        self.client = client

        self.controller = ClientLinked_ShooterController(owner=self, client=self.client)