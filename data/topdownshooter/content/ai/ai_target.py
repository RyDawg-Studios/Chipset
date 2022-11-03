from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.actor.actor import Actor

class AITarget(Actor):
    def __init__(self, man, pde, position):
        super().__init__(man, pde)
        self.position = position
        self.checkForCollision = False

    def construct(self):
        super().construct()
        if self.pde.config_manager.config["config"]["debugMode"]:
            self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\mariohitbox.png', layer=4)



    