class Game:
    def __init__(self, pde):
        self.pde = pde

    def activate(self):
        for level in self.pde.level_manager.levels.values():
            for object in list(level.objectManager.objects.values()):
                object.deconstruct()

    def update(self):
        pass

