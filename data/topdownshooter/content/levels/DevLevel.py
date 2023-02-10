from data.engine.debug.debugObject import SpinProjectile, TestActor, TestPlayer
from data.engine.level.level import Level
from data.engine.util.gameobjects.collider import Collider
from data.topdownshooter.content.levels.levelloader.levelloader import LevelLoader
from data.topdownshooter.content.objects.camera.shootercam import ShooterCamera
from data.topdownshooter.content.objects.chest.chest import Chest
from data.topdownshooter.content.objects.dummy.dummy import Dummy
from data.topdownshooter.content.objects.enemy.enemy import ShooterEnemy
from data.topdownshooter.content.objects.exp.exp import EXP
from data.topdownshooter.content.objects.hazard.magnet.magnet import Magnet
from data.topdownshooter.content.objects.player.player import ShooterPlayer
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
from data.topdownshooter.content.objects.turret.turret import Turret
from data.topdownshooter.content.objects.weapon.hitmarker.hitmarker import Hitmarker
from data.topdownshooter.content.objects.weapon.pickup.pickupweapon import PickupWeapon
from data.topdownshooter.content.objects.weapon.weapons.weapons import SMG, AutomaticRifle, ChainRifle, DevGun, ElectroLauncher, Enderpearl, GrenadeLauncher, LaserMachineGun, LaserPistol, LaserRifle, Revolver, RocketLauncher, Shotgun, SniperRifle, SpawnerWeapon, SplatGun
from data.topdownshooter.content.objects.widget.fadeout import FadeOut


class DevLevel(Level):
    def __init__(self, man, pde) -> None:
        self.ticks = 0
        super().__init__(man, pde)
        self.changebackground(r'data\topdownshooter\assets\sprites\backgrounds\bg.png')

        p = self.objectManager.add_object(ShooterPlayer(man=self.objectManager, pde=pde, position=[732/2, 412/2]))
        self.pde.game.player = p
        p.removeweapon()
        #self.objectManager.add_object(ShooterEnemy(man=self.objectManager, pde=pde, position=[732/2, 412/2], weapon=LaserMachineGun))
        itemlist = [SMG, AutomaticRifle, SniperRifle, LaserMachineGun, GrenadeLauncher, Shotgun, ElectroLauncher, SpawnerWeapon, Enderpearl, SplatGun, RocketLauncher, Revolver, ChainRifle, LaserPistol]

        for inx, w in enumerate(itemlist):
            weap = self.objectManager.add_object(obj=w(man=self.objectManager, pde=self.pde, owner=None, position=[0,0]))
            self.objectManager.add_object(PickupWeapon(man=self.objectManager, pde=self.pde, position=[(inx) * 64, 0], speed=[0, 0], weapon=weap))
            weap.deconstruct()

        lm = self.objectManager.add_object(LevelLoader(man=self.objectManager, pde=pde, position=[0,200],level="room2"))
        chest = self.objectManager.add_object(Chest(man=self.objectManager, pde=pde, position=[320,64], items=[DevGun]))
        dummy = self.objectManager.add_object(Dummy(man=self.objectManager, pde=pde, position=[320,-64]))

        t = self.objectManager.add_object(Turret(man=self.objectManager, pde=pde, position=[320,-128]))
