from data.engine.level.level import Level
from data.engine.widgets.element.e_button import ButtonElement
from data.engine.widgets.element.e_sprite import SpriteElement
from data.topdownshooter.content.levels.DevLevel import DevLevel
from data.topdownshooter.content.levels.GeneratedLevel import GeneratedLevel
from data.topdownshooter.content.levels.ServerLevels.ServerLevel import ServerLevel
from data.topdownshooter.content.levels.TestLevel import TestLevel


class MainMenu(Level):
    def __init__(self, man, pde):
        super().__init__(man, pde)
        self.changebackground(r'data\topdownshooter\assets\sprites\backgrounds\bg.png')

        logo = self.objectManager.add_object(SpriteElement(man=self.objectManager, pde=self.pde, position=[320, 100], scale=[196, 52], useCenterForPosition=True, sprite=r"data\topdownshooter\assets\sprites\ui\menu\logobg.png"))

        debug = self.objectManager.add_object(ButtonElement(man=self.objectManager, pde=self.pde, position=[480, 260], scale=[196, 52], useCenterForPosition=True, sprite=r"data\topdownshooter\assets\sprites\ui\menu\debug.png", bind=self.load_debug))
        start = self.objectManager.add_object(ButtonElement(man=self.objectManager, pde=self.pde, position=[160, 260], scale=[196, 52], useCenterForPosition=True, sprite=r"data\topdownshooter\assets\sprites\ui\menu\start.png", bind=self.load_main))



    def load_debug(self):
        self.pde.network_manager.activate()
        self.pde.game.changelevel(TestLevel)
    
    def load_main(self):
        self.pde.game.changelevel(GeneratedLevel)
