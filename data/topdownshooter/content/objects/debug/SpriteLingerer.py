from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent


class SpriteLingerObject(Actor):
    def __init__(self, man, pde):
        self.scale=[32, 32]
        super().__init__(man, pde)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite='', layer=3)

    
    def update(self):
        return super().update()
        
