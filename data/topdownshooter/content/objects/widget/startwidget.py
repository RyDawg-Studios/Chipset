from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.widgets.button import Button


class StartButton(Actor):
    def __init__(self, man, pde, position=[0,0]):
        super().__init__(man, pde)
        self.position = position
        self.scale = [300, 150]
        self.components["Sprite"] = SpriteComponent(owner=self, sprite='', layer=0)
        self.components["Button"] = Button(owner=self, bind=self.click)

    def click(self):
        self.pde.game.loadMorphLevel()
