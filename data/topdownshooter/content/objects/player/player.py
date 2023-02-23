import random
from data.engine.fl.world_fl import objectlookatposition
from data.engine.particle.particle_emitter import ParticleEmitter
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.camera.shootercam import ShooterCamera
from data.topdownshooter.content.objects.hazard.magnet.magnet import Magnet
from data.topdownshooter.content.objects.player.shooter_controller import ShooterController
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
from data.topdownshooter.content.objects.widget.fadeout import FadeOut


class ShooterPlayer(ShooterEntity):
    def __init__(self, man, pde, position=None, hp=400):
        super().__init__(man, pde, position=position)
        self.maxhp = 400
        self.hp = hp
        self.maxVelocity = 1
        self.velocity = self.maxVelocity
        self.pausable = False
        self.bleed = True
        
        self.weaponindx = 0

    def construct(self):
        super().construct()
        self.components["PlayerController"] = ShooterController(owner=self)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\me.png', layer=2)
        
        self.cam = self.man.add_object(ShooterCamera(man=self.man, pde=self.pde, position=self.position, target=self))

        

    def spawnmagnet(self):
        self.man.add_object(Magnet(man=self.man, pde=self.pde, position=self.pde.input_manager.mouse_position))

    def update(self):
        self.pde.game.player = self
        self.components["Sprite"].scale = self.scale



        if self.weapon != None:
            self.weapon.rotation = objectlookatposition(self.weapon, self.pde.input_manager.mouse_position)

        if self.deadticks >= 100:
            self.pde.game.restart()
            return

        #self.fo.rect.center = self.cam.rect.center
        return super().update()

    def die(self, killer):
        super().die(killer)
        self.pde.game.player = None
        self.canMove = False
        self.canShoot = False
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\deadme.png', layer=2)
        self.dropweapon()
        self.pde.game.game_over()
