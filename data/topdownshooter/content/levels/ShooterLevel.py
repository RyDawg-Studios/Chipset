from data.engine.debug.debugObject import SpinProjectile, TestActor, TestPlayer
from data.engine.level.level import Level
from data.engine.util.gameobjects.collider import Collider
from data.topdownshooter.content.levels.levelloader.levelloader import LevelLoader
from data.topdownshooter.content.objects.camera.shootercam import ShooterCamera
from data.topdownshooter.content.objects.enemy.enemy import ShooterEnemy
from data.topdownshooter.content.objects.exp.exp import EXP
from data.topdownshooter.content.objects.player.player import ShooterPlayer
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
from data.topdownshooter.content.objects.weapon.hitmarker.hitmarker import Hitmarker
from data.topdownshooter.content.objects.weapon.pickup.pickupweapon import PickupWeapon
from data.topdownshooter.content.objects.weapon.weapons.weapons import LaserMachineGun, SniperRifle


class ShooterLevel(Level):
    def __init__(self, man, pde) -> None:
        self.ticks = 0
        super().__init__(man, pde)
        self.changebackground(r'data\topdownshooter\assets\sprites\backgrounds\bg.png')
        lm = self.objectManager.add_object(LevelLoader(man=self.objectManager, pde=pde, position=[0,0],level="room"))
        p = self.objectManager.add_object(ShooterPlayer(man=self.objectManager, pde=pde, position=[320, 240]))
        e = self.objectManager.add_object(ShooterEnemy(man=self.objectManager, pde=pde, position=[100, 100], weapon=LaserMachineGun))

