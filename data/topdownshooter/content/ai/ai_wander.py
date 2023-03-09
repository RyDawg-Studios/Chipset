from data.engine.ai.ai_state import AIState
from data.engine.fl.world_fl import objectlookatposition, getpositionlookatvector
import random
from data.topdownshooter.content.ai.ai_target import AITarget
import pygame


class WanderAI(AIState):
    def __init__(self, man, pde, owner):
        super().__init__(man, pde, owner)
        self.target = man.add_object(AITarget(man=man, pde=pde, position=[random.randint(0, self.pde.config_manager.config["config"]["dimensions"][0]), random.randint(0, self.pde.config_manager.config["config"]["dimensions"][1])]))
        self.waitticks = 0
        self.destination = self.target.position
        self.waitticks = 0
        self.waittime = random.randint(0, 40)
        self.travelticks = 0
        self.r = 0

    def update(self):
        super().update()
        if pygame.Vector2.distance_to(pygame.Vector2(self.owner.owner.position), pygame.Vector2(self.target.position)) < 5:
            self.waitticks += 1
            self.owner.owner.movement = [0, 0]
            if self.waitticks >= self.waittime:
                self.picknewlocation()
        else:
            self.travelticks += 1
            if self.travelticks >= 100:
                self.picknewlocation()
            self.r = getpositionlookatvector(self.owner.owner, self.destination)
            self.owner.owner.movement = self.r


    def picknewlocation(self):
        self.waitticks = 0
        self.target.deconstruct()
        self.target = self.man.add_object(AITarget(man=self.man, pde=self.pde, position=[random.randint(0, self.pde.config_manager.config["config"]["dimensions"][0]), random.randint(0, self.pde.config_manager.config["config"]["dimensions"][1])]))
        self.destination = self.target.position
        self.travelticks = 0

    def deconstruct(self):
        self.target.deconstruct()
        return super().deconstruct()


