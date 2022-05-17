from data.engine.object.object import Object


class Upgrade(Object):
    def __init__(self, man, pde, weapon):
        self.weapon = weapon
        super().__init__(man, pde)

    def update(self):
        return super().update()

    def onShot(self, b):
        return b

    