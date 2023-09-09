import pygame
from data.engine.component.component import Component

class NetPlayerController(Component):
    def __init__(self, owner, client) -> None:
        super().__init__(owner)
        self.inpman = self.owner.pde.input_manager
        self.client = client
        self.owner.pde.player_manager.net_controllers[self.client] = self

    def update(self):
        self.manage_input()
        super().update()

    def manage_input(self):
        pass

    def on_joystick(self, event):
        pass

    def update_debug(self):
        pass

    def on_input(self, input):
        if input == pygame.K_F1:
            self.owner.pde.level_manager.level.objectManager.printobjects()
            
    def on_mouse(self, button):
        pass

    def deconstruct(self):
        self.owner.pde.player_manager.net_controllers.pop(self)
        return super().deconstruct()