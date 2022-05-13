from lib2to3.pgen2.token import GREATER
import random
from typing_extensions import Self
from data.engine.fl.world_fl import objectlookatposition
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.camera.shootercam import ShooterCamera
from data.topdownshooter.content.objects.player.shooter_controller import ShooterController
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
from data.topdownshooter.content.objects.weapon.weapons.weapon import Weapon
from data.topdownshooter.content.objects.weapon.weapons.weapons import SMG, AutomaticRifle, DevGun, LaserMachineGun, LaserRifle, Shotgun, SniperRifle, GrenadeLauncher


class ShooterPlayer(ShooterEntity):
    def __init__(self, man, pde, position=None, scale=[32, 32]):
        super().__init__(man, pde, position, scale)
        self.maxhp = 400
        self.hp = 400
        pde.game.player = self
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\me.png', layer=2)
        self.components["PlayerController"] = ShooterController(owner=self)
        w = random.choice([SMG, AutomaticRifle, SniperRifle, LaserMachineGun])

        self.weapon = man.add_object(obj=GrenadeLauncher(man=man, pde=pde, owner=self))
        self.cam = self.man.add_object(ShooterCamera(man=self.man, pde=pde, position=self.position, target=self))

        self.weaponindx = 0

    def update(self):
        if self.weapon != None:
            self.weapon.rotation = objectlookatposition(self, self.pde.input_manager.mouse_position)

        #self.scrollcameratocenterx()
        #self.scrollcameratocentery()

        if self.deadticks >= 100:
            self.pde.game.activate()
        return super().update()

    def die(self, obj):
        self.canMove = False
        self.canShoot = False
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\deadme.png', layer=2)
        self.dropweapon(rotation=self.weapon.rotation)
        self.weapon = None
        return

    def cycleweapon(self):
        return