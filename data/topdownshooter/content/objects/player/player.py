from data.engine.fl.world_fl import objectlookatposition
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.camera.shootercam import ShooterCamera
from data.topdownshooter.content.objects.player.shooter_controller import ShooterController
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
from data.topdownshooter.fl.game_fl import chooseRandomWeapon


class ShooterPlayer(ShooterEntity):
    def __init__(self, man, pde, position=None):
        super().__init__(man, pde, position)
        self.maxhp = 400
        self.hp = 400
        pde.game.player = self
        self.maxVelocity = 1
        self.velocity = self.maxVelocity
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\me.png', layer=2)
        self.components["PlayerController"] = ShooterController(owner=self)
        w = chooseRandomWeapon()

        self.weapon = man.add_object(obj=w(man=man, pde=pde, owner=self, position=[self.rect.centerx + 10, self.rect.centery + 10]))
        self.cam = self.man.add_object(ShooterCamera(man=self.man, pde=pde, position=self.position, target=self))
        #self.fo = self.man.add_object(FadeOut(man=self.man, pde=self.pde))
        self.weaponindx = 0

    def update(self):
        if self.weapon != None:
            self.weapon.rotation = objectlookatposition(self.weapon, self.pde.input_manager.mouse_position)

        if self.deadticks >= 100:
            self.pde.game.restart()

        #self.fo.rect.center = self.cam.rect.center
        self.components["Sprite"].scale = self.scale
        return super().update()

    def die(self, killer):
        self.canMove = False
        self.canShoot = False
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\deadme.png', layer=2)
        if self.weapon is not None:
            self.dropweapon(rotation=self.weapon.rotation)
        self.weapon = None
        return super().die(killer)
