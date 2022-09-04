from data.engine.level.level import Level
from data.topdownshooter.content.objects.player.player import ShooterPlayer
from data.topdownshooter.content.objects.weapon.pickup.pickupweapon import PickupWeapon
from data.topdownshooter.content.objects.weapon.weapons.weapons import LaserMachineGun, SpawnerWeapon
from data.topdownshooter.content.levels.levelloader.levelloader import LevelLoader


class TestLevel(Level):
    def __init__(self, man, pde) -> None:
        self.ticks = 0
        super().__init__(man, pde)
        self.changebackground(r'data\topdownshooter\assets\sprites\backgrounds\bg.png')

        p = self.objectManager.add_object(ShooterPlayer(man=self.objectManager, pde=pde, position=[320, 140]))
        p.removeweapon()

        itemlist = [LaserMachineGun, SpawnerWeapon]

        for inx, w in enumerate(itemlist):
            weap = self.objectManager.add_object(obj=w(man=self.objectManager, pde=self.pde, owner=None, position=[64, 64]))
            self.objectManager.add_object(PickupWeapon(man=self.objectManager, pde=self.pde, position=[(inx+1) * 64, 64], speed=[0, 0], weapon=weap))
            weap.queuedeconstruction()
        

        lm = self.objectManager.add_object(LevelLoader(man=self.objectManager, pde=pde, position=[0,0],level="room1"))

