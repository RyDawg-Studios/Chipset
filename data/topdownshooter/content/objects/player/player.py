import pygame
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import objectlookatposition
from data.engine.particle.particle_emitter import ParticleEmitter
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.camera.shootercam import ShooterCamera
from data.topdownshooter.content.objects.hazard.magnet.magnet import Magnet
from data.topdownshooter.content.objects.player.shooter_controller import ShooterController
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


class ShooterPlayer(ShooterEntity):
    def __init__(self, man, pde, position=None, hp=400):
        super().__init__(man, pde, position=position)
        self.maxhp = 400
        self.hp = hp
        self.maxVelocity = 1
        self.velocity = self.maxVelocity
        self.pausable = False
        self.bleed = True
        self.crosshair = None
        
        self.weaponindx = 0

        self.stock = [u.SplitStreamUpgrade, u.DisarmamentUpgrade, u.VamprismUpgrade]

        self.ignoreEntities =[ShooterPlayer]

    def construct(self):
        super().construct()
        self.components["PlayerController"] = ShooterController(owner=self)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\me.png', layer=2)

        self.crosshair = self.man.pde.display_manager.userInterface.add_object(obj=Crosshair(man=self.man.pde.display_manager.userInterface, pde=self.pde, position=[0,0]))
        
        self.cam = self.man.add_object(ShooterCamera(man=self.man, pde=self.pde, position=self.position, target=self))

    def cycleweapon(self):
        index = self.currentweapon + 1
        if index > 6:
            index = 1
        self.switchweapon(index)


    def spawnmagnet(self):
        self.man.add_object(Magnet(man=self.man, pde=self.pde, position=self.pde.input_manager.mouse_position))

    def managereticle(self):
        if self.weapon is not None:
            self.crosshair.rect.center = self.target
            self.crosshair.components["Sprite"].sprite.opacity = 255
        else:
            self.crosshair.components["Sprite"].sprite.opacity = 0

    def settargetposition(self):
        if len(self.pde.input_manager.joysticks) > 0:
            if self.weapon is not None:
                self.target = pygame.Vector2(self.weapon.rect.center) + (pygame.Vector2(round(self.components["PlayerController"].axis[2], 2), round(self.components["PlayerController"].axis[3], 2)) * 50)
                self.cam.rect.center = self.target
            else:
                self.target = self.position
        else:
            self.target = self.pde.input_manager.mouse_position

    def openUpgradeSelectionUI(self):
        self.pde.game.ui.openUpgradeSelection()

    def update(self):
        super().update()
        self.pde.game.player = self

        self.pde.game.playerData.hp = self.hp
        self.pde.game.playerData.loadout = self.weapons.copy()
        self.pde.game.playerData.currentWeapon = self.currentweapon
        


        self.components["Sprite"].scale = self.scale


        self.settargetposition()
        self.managereticle()
        
        if self.weapon != None:
            self.weapon.rotation = objectlookatposition(self.weapon, self.target)

        if self.deadticks >= 100:
            self.pde.game.game_over()
            self.pde.game.restart()
            return

        #self.fo.rect.center = self.cam.rect.center

    def die(self, killer):
        super().die(killer)
        self.pde.game.player = None
        self.canMove = False
        self.canShoot = False
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\deadme.png', layer=2)
        self.dropweapon()

    def deconstruct(self):
        super().deconstruct()

    def onKill(self, enemy):
        super().onKill(enemy)
        self.pde.game.playerData.kills += 1
