class Component:
    def __init__(self, owner):
        self.owner = owner
        self.owner.man.add_object(obj=self)

    def update(self):
        return

    def deconstruct(self):
        self.owner.man.remove_object(self)

    def checkForOwner(self):
        return