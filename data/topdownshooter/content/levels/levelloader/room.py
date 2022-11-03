from data.engine.actor.actor import Actor

from data.topdownshooter.content.levels.levelloader.levelloader import LevelLoader
from data.topdownshooter.content.objects.camera.shootercam import ShooterCamera





class Room(LevelLoader):
    def __init__(self, man, pde, position=[0, 0], level="room1"):
        super().__init__(man, pde, position=position, level=level)

    def construct(self):
        super().construct()
        self.cameraMarker = self.man.add_object(obj=Actor(man=self.man, pde=self.pde, position=[0,0], checkForCollision=False, useCenterForPosition=True))
        self.camera = None
        for rinx, row in enumerate(self.levels[self.level]["layers"][1]):
            for oinx, obj in enumerate(row):
                if obj != '#':
                    self.cameraMarker.rect.center = [(oinx*32)+32 + self.position[0], (rinx*32+ 16)+ self.position[1]]
                    self.camera = self.man.add_object(obj=ShooterCamera(man=self.man, pde=self.pde, position=self.cameraMarker.rect.center, target=self.cameraMarker))




    
        
