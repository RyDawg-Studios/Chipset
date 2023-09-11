import random
from types import NoneType
from data.engine.level.level import Level
from data.topdownshooter.content.levels.levelloader.levelloader import LevelLoader
from data.topdownshooter.content.levels.levelloader.room import Room
from data.topdownshooter.content.objects.camera.shootercam import ShooterCamera
from data.topdownshooter.content.objects.hazard.hole.hole import Hole
from data.topdownshooter.content.objects.levelgenerator.level_generator import LevelGenerator
from data.topdownshooter.content.objects.player.player import ShooterPlayer
from data.topdownshooter.content.objects.turret.turret import Turret
from data.topdownshooter.content.objects.weapon.weapons.weapons import DevGun, Pistol
from data.topdownshooter.content.objects.widget.shooterwidget import ShooterWidget



class GeneratedLevel(Level):
    def __init__(self, man, pde):
        super().__init__(man, pde)
        self.changebackground(r'data\topdownshooter\assets\sprites\backgrounds\bg.png')




        l = self.objectManager.add_object(LevelGenerator(man=self.objectManager, pde=pde, position=[0,0], scale=[10, 10], complexity=self.pde.game.currentRoomNumber))
        l.generate_procedural_room()
        pos = random.choice(l.whitespace)
        p = self.objectManager.add_object(ShooterPlayer(man=self.objectManager, pde=pde, position=l.get_spawnpoint(), hp=self.pde.game.playerData.hp))

        self.pde.game.ui = self.pde.display_manager.userInterface.add_object(ShooterWidget(man=self.pde.display_manager.userInterface, pde=self.pde, owner=p))

        cam = self.objectManager.add_object(ShooterCamera(man=self.objectManager, pde=pde, position=p.position, target=p))


        pd = self.pde.game.playerData

        p.weapons = pd.loadout
        p.currentweapon = pd.currentWeapon
        p.switchweapon(p.currentweapon)
        


    def deconstruct(self):
        self.pde.game.ui.deconstruct()
        self.pde.display_manager.userInterface.clear()
        return super().deconstruct()


