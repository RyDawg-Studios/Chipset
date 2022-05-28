class Game:
    def __init__(self, pde):
        self.pde = pde

    def activate(self):
        if self.pde.level_manager.level is not None:
            for object in list(self.pde.level_manager.level.objectManager.objects.values()):
                object.deconstruct()

    def update(self):
        pass

