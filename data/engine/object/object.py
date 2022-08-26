import struct


class Object:
    def __init__(self, man, pde):
        self.man = man
        self.pde = pde
        self.components = {}
        self.scroll = True
        self.replicate = False
        self.pausable = True
        self.paused = False

    def pause(self):
        if self.pausable:
            self.paused = True

    def removecomponent(self, component):
        self.components.pop(component)

    def update(self):
        return

    def deconstruct(self, outer=None):
        self.pause()
        self.man.remove_object(self, outer)
        for component in self.components.values():
            component.deconstruct()
            component = None

    def serialize(self, data=None):
        return struct.pack(data)
        
    def deserialize(self):
        return

    


