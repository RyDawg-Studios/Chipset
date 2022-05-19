from data.engine.debug.debugObject import SpinProjectile, TestActor, TestPlayer
from data.engine.level.level import Level
from data.engine.util.gameobjects.collider import Collider
from data.topdownshooter.content.levels.levelloader.levelloader import LevelLoader
from data.topdownshooter.content.objects.camera.shootercam import ShooterCamera
from data.topdownshooter.content.objects.debug.SpriteLingerer import SpriteLingerObject
from data.topdownshooter.content.objects.enemy.enemy import ShooterEnemy
from data.topdownshooter.content.objects.exp.exp import EXP
from data.topdownshooter.content.objects.player.player import ShooterPlayer
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
from data.topdownshooter.content.objects.weapon.hitmarker.hitmarker import Hitmarker
from data.topdownshooter.content.objects.weapon.pickup.pickupweapon import PickupWeapon
from data.topdownshooter.content.objects.weapon.weapons.weapons import SMG, AutomaticRifle, DevGun, ElectroLauncher, Enderpearl, GrenadeLauncher, LaserMachineGun, LingerTest, Shotgun, SniperRifle, SpawnerWeapon


class DevLevel(Level):
    def __init__(self, man, pde) -> None:
        self.ticks = 0
        super().__init__(man, pde)
        self.changebackground(r'data\topdownshooter\assets\sprites\backgrounds\bg.png')
        p = self.objectManager.add_object(ShooterPlayer(man=self.objectManager, pde=pde, position=[320, 140]))
        p.removeweapon()


        for inx, w in enumerate([SMG, AutomaticRifle, SniperRifle, LaserMachineGun, GrenadeLauncher, Shotgun, ElectroLauncher, DevGun, SpawnerWeapon, Enderpearl]):
            weap = w(man=self.objectManager, pde=self.pde, owner=None)
            self.objectManager.add_object(PickupWeapon(man=self.objectManager, pde=self.pde, position=[(inx) * 64, 0], speed=[0, 0], weapon=weap))
            weap.deconstruct()

        lm = self.objectManager.add_object(LevelLoader(man=self.objectManager, pde=pde, position=[0,200],level="room2"))
