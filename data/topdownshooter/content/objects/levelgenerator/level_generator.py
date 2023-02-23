import random

import pygame
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import getpointdistance
from data.topdownshooter.content.tiles.tile import Tile


class LevelGenerator(Actor):
    def __init__(self, man, pde, position=[], scale=[], checkForOverlap=False, checkForCollision=False, useCenterForPosition=False, lifetime=-1, complexity=0):
        super().__init__(man, pde, position, scale, checkForOverlap, checkForCollision, useCenterForPosition, lifetime)
        self.complexity = complexity
        self.tiles = []
        self.rects = []
        self.fullrects = []
        self.whitespace = []
        self.points = []

    def generate_points(self):
        for i in range(8):
            self.points.append([random.randint(0, self.scale[0]*2), random.randint(0, self.scale[1]*2)])

    def generate_rects(self):
        for point in self.points:
            rect = []
            x = random.randint(8, 12)
            y = random.randint(8, 12)

            o = [point[0]-x, point[1]+y]

            w = x*2
            h = y*2

            for i in range(1, h+1):
                for j in range(1, w+1):
                    if (i==1 or i==h or j==1 or j==w):
                        rect.append([j-o[1], i+o[0]])
                    else:
                        self.whitespace.append([j-o[1], i+o[0]])

            self.rects.append(rect)

        for frect in self.fullrects:
            for rect in self.rects:
                for point in frect:
                    if point not in rect:
                        self.whitespace.append(point)

    def generate_tiles(self):
        for rect in self.rects:
            for tile in rect:
                if tile not in self.whitespace:
                    self.man.add_object(obj=Tile(man=self.man, pde=self.pde, position=[tile[0]*16 + 16, tile[1]*16 + 16], sprite=r'data\topdownshooter\assets\sprites\tiles\wall1.png'))

    def generate_safe_spawnpoint(self):
        safe = []
        for point in self.whitespace:
            for rect in self.rects:
                for tile in rect:
                    if getpointdistance(tile[0], tile[1], point[0], point[1]) > 64:
                        safe.append(point)

        point = random.choice(safe)
        return [point[0]*16 + 8, point[1]*16 + 8]



    def construct(self):
        super().construct()
        self.generate_points()
        self.generate_rects()
        self.generate_tiles()