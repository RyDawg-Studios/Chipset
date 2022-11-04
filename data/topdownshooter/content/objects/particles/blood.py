import random
from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent


class Blood(Actor):
    def __init__(self, man, pde, position=[0,0]):
        super().__init__(man, pde, position=position, scale=[16, 16], lifetime=360, checkForCollision=False, checkForOverlap=False)
        return

    def construct(self):
        super().construct()
        spritePath = random.choice([r"\\blood.png", r"\\d_blood.png", r"\\l_blood.png"])
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\objects\blood' + spritePath, layer=0)
        self.getcomponent("Sprite").sprite.rotation = random.randint(0, 360)



    def update(self):
        self.ticks += 1
        if self.ticks >= 300:
            self.components["Sprite"].sprite.opacity -= 5
        return