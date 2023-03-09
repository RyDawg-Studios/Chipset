from data.engine.ai.ai_state import AIState
from data.engine.fl.world_fl import objectlookatposition, getpositionlookatvector
import random
from data.topdownshooter.content.ai.ai_target import AITarget
import pygame


class ShortAI(AIState):
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

        if self.owner.owner.pde.game.player is not None:
            self.destination = self.owner.owner.pde.game.player.position
            self.r = getpositionlookatvector(self.owner.owner, self.destination)
            self.owner.owner.movement = self.r




    def deconstruct(self):
        super().deconstruct()
        self.target.deconstruct()


