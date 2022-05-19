import random
from data.engine.fl.world_fl import objectlookatposition
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.camera.shootercam import ShooterCamera
from data.topdownshooter.content.objects.player.shooter_controller import ShooterController
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
from data.topdownshooter.content.objects.weapon.weapons.weapon import Weapon
from data.topdownshooter.content.objects.weapon.weapons.weapons import SMG, AutomaticRifle, DevGun, LaserMachineGun, LaserRifle, Shotgun, SniperRifle, GrenadeLauncher
from data.topdownshooter.fl.game_fl import chooseRandomWeapon


class ShooterPlayer(ShooterEntity):
    def __init__(self, man, pde, position=None, scale=[32, 32]):
        super().__init__(man, pde, position, scale)
        self.maxhp = 400
        self.hp = 400
        pde.game.player = self
        self.maxVelocity = 1
        self.velocity = self.maxVelocity
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\me.png', layer=2)
        self.components["PlayerController"] = ShooterController(owner=self)
        w = chooseRandomWeapon()

        self.weapon = man.add_object(obj=w(man=man, pde=pde, owner=self))
        self.cam = self.man.add_object(ShooterCamera(man=self.man, pde=pde, position=self.position, target=self))


        self.weaponindx = 0

    def update(self):
        if self.weapon != None:
            self.weapon.rotation = objectlookatposition(self.weapon, self.pde.input_manager.mouse_position)

        if self.deadticks >= 100:
            self.pde.game.activate()
        return super().update()

    def die(self, obj):
        self.canMove = False
        self.canShoot = False
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\deadme.png', layer=2)
        if self.weapon is not None:
            self.dropweapon(rotation=self.weapon.rotation)
        self.weapon = None
        return

    def cycleweapon(self):
        return