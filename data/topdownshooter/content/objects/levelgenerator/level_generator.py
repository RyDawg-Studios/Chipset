import random

import pygame
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import getpointdistance, normal_cut
from data.topdownshooter.content.levels.levelloader.levelloader import LevelLoader
from data.topdownshooter.content.objects.enemy.default_enemy import DefaultEnemy
from data.topdownshooter.content.objects.hazard.hole.hole import Hole
from data.topdownshooter.content.objects.weapon.weapons.weapons import SMG, AutoShotgun, AutomaticRifle, ChainRifle, DevGun, ElectroLauncher, Enderpearl, FlamePistol, Flamethrower, GrenadeLauncher, LaserMachineGun, LaserPistol, LaserRifle, LooseChange, Musket, Pistol, Revolver, RiskGun, RocketLauncher, Shotgun, SniperRifle, SpawnerWeapon, SplatGun
from data.topdownshooter.content.tiles.tile import Tile
import math


class LevelGenerator(Actor):
    def __init__(self, man, pde, position=[], scale=[], checkForOverlap=False, checkForCollision=False, useCenterForPosition=False, lifetime=-1, complexity=1):
        super().__init__(man, pde, position, scale, checkForOverlap, checkForCollision, useCenterForPosition, lifetime)
        self.complexity = complexity
        self.tiles = []
        self.rects = []
        self.fullrects = []
        self.whitespace = []
        self.points = []
        self.safetiles = []
        self.enemies = []
        self.weaponladder = [Pistol, Revolver, LaserPistol, SMG, AutomaticRifle, Musket, Shotgun, LooseChange, GrenadeLauncher, FlamePistol, LaserMachineGun, SniperRifle, RocketLauncher, ChainRifle, AutoShotgun, Flamethrower]


    def generate_points(self):
        for i in range(3):
            self.points.append([random.randint(0, self.scale[0]*2), random.randint(0, self.scale[1]*2)])

    def generate_rects(self):
        for point in self.points:
            rect = []
            x = random.randint(10, 15)
            y = random.randint(10, 15)

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
                
    def generate_safe_spawnpoints(self):
        safe = []
        for point in self.whitespace:
            for rect in self.rects:
                for tile in rect:
                    if getpointdistance(tile[0], tile[1], point[0], point[1]) > 16:
                        safe.append(point)
        
        self.safetiles = safe


    def generate_enemy_spawnpoints(self):
        for i in range(self.generate_enemy_count(complexity=self.complexity)):
            n = self.man.add_object(DefaultEnemy(man=self.man, pde=self.pde, position=self.get_spawnpoint(), weapon=self.weaponladder[abs(round(normal_cut(self.complexity-1, 1, 1)))]))
            n.onDeathEvent.bind(self.on_enemy_killed)
            self.enemies.append(n)


    def get_spawnpoint(self):
        point = random.choice(self.safetiles)

        return [point[0]*16+8, point[1]*16+8]

    def generate_enemy_count(self, complexity):
        waves = complexity**(1/3)
        return round(waves)
    
    def generate_obstacles(self):
        for i in range(0, round(self.complexity**(1/3)) + 2):
            point = random.choice(self.whitespace)
            l = LevelLoader(man=self.man, pde=self.pde, position=pygame.Vector2(point[0], point[1])*16, level=random.choice(["o_med_block", "o_big_cross"]))

            

    def on_enemy_killed(self, enemy, killer):
        n = enemy
        if enemy in self.enemies:
            self.enemies.remove(enemy)
        
        if len(self.enemies) == 0:
            self.man.add_object(Hole(man=self.man, pde=self.pde, position=n.position))



    def construct(self):
        super().construct()
        self.generate_points()
        self.generate_rects()
        self.generate_tiles()
        self.generate_safe_spawnpoints()
        self.generate_enemy_spawnpoints()
        #self.generate_obstacles()
