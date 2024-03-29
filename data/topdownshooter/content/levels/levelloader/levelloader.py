from http.client import GATEWAY_TIMEOUT
import json

from data.engine.actor.actor import Actor
from data.engine.debug.debugObject import TestActor
from data.engine.object.object import Object
from data.topdownshooter.content.objects.enemy.enemy import ShooterEnemy
from data.topdownshooter.content.objects.gate.gate import LevelGate
from data.topdownshooter.content.objects.player.player import ShooterPlayer
from data.topdownshooter.content.tiles.tile import Tile


class LevelLoader(Actor):
    def __init__(self, man, pde, position=[0, 0], level="default"):
        super().__init__(man, pde)
        self.position=position
        self.scale =[0, 0]
        f = open(r"data\topdownshooter\data\leveldata.json")
        self.checkForCollision = False
        self.checkForOverlap = False
        self.levels = json.load(f)
        self.level = level
        self.tiles = []
        self.whitespace = []

        self.objects = {}

        self.tilekey = {'x': r'data\topdownshooter\assets\sprites\tiles\wall1.png'}


        self.placetiles()

    def placetiles(self):
        for rinx, row in enumerate(self.levels[self.level]["layers"][0]):
            for oinx, obj in enumerate(row):
                if obj == 'x':
                    o = self.man.add_object(obj=Tile(man=self.man, pde=self.pde, position=[(oinx*24) + 12 + self.position[0], (rinx*24+ 12)+ self.position[1]], sprite=self.tilekey[obj]))
                    self.tiles.append(o)
                elif obj == '#':
                    self.whitespace.append([(oinx*24) + 12 + self.position[0], (rinx*24+ 12)+ self.position[1]])
                else:
                    if obj in self.objects.keys():
                        self.objects[obj].append([(oinx*24) + 12 + self.position[0], (rinx*24+ 12)+ self.position[1]])
                    else:
                        self.objects[obj] = [[(oinx*24) + 12 + self.position[0], (rinx*24+ 12)+ self.position[1]]]



    def deconstruct(self, outer=None):
        for o in self.tiles:
            o.deconstruct()
        return super().deconstruct(outer=outer)

    
        
