import pygame

from data.engine.quadtree.Quadtree import QuadTree
from data.engine.quadtree.range import Rectangle
from data.engine.networking import pde_network_table as nt


class ObjectManager:

    def __init__(self, pde) -> None:
        self.objects = []
        self.pde = pde
        self.clearing = False

        self.quadsize = 16

        self.quadtree = QuadTree(self.quadsize, Rectangle(pygame.Vector2(0, 0), pygame.Vector2(self.pde.config_manager.config["config"]["dimensions"])), pde=self.pde)

        self.pde.event_manager.net_events["spawn"] = self.deserializeNetObject

    def add_object(self, obj):
        if obj not in self.objects:
            self.objects.append(obj)
            obj.construct()

        return obj

    def remove_object(self, obj, outer=None):
        if obj in self.objects:
            self.objects.remove(obj)
            return True
        else:
            return False

    def update(self):
        self.quadtree = QuadTree(self.quadsize, Rectangle(pygame.Vector2(0, 0), pygame.Vector2(self.pde.config_manager.config["config"]["dimensions"])), pde=self.pde)
        for obj in list(self.objects):
            self.quadtree.insert(obj)
            
        for obj in list(self.objects):
            if not obj.paused:
                obj.update()
                for component in list(obj.components.values()):
                    component.update()


        if self.pde.config_manager.config["config"]["debugMode"]:
            self.quadtree.Show(screen=self.pde.display_manager.screen)

    def clear(self):
        for obj in self.objects:
            obj.deconstruct()
            
        self.objects = []

        self.quadtree = QuadTree(self.quadsize, Rectangle(pygame.Vector2(0, 0), pygame.Vector2(self.pde.config_manager.config["config"]["dimensions"])), pde=self.pde)

    def printobjects(self):
        print("----------------< Objects >----------------")
        i=0
        for o in self.objects:
            print(o)
            i += 1
        print(f"Count: {i}")
        
    def getPlayers(self):
        for obj in list(self.objects.values()):
            for comp in obj.components:
                if comp == "PlayerController":
                    return obj

    def deserializeNetObject(self, data):
        obj = self.pde.replication_tables[data[0]["package_id"]].object_table[data[0]['object_id']](man=self, pde=self.pde)
        for attr in data[0]['attributes']:
                setattr(obj, attr, data[0]['attributes'][attr])
        self.add_object(obj)


        return obj



