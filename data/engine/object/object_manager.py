import pygame


class ObjectManager:

    def __init__(self, pde) -> None:
        self.objects = {}
        self.pde = pde
    

    def add_object(self, obj):
        self.objects[str(obj)] = obj
        return obj

    def remove_object(self, obj):
        try:
            self.objects.pop(str(obj))
        except:
            pass


    def update(self):
        for obj in list(self.objects.values()):
            if not obj.paused:
                obj.update()
                for component in list(obj.components.values()):
                    component.update()
            #if hasattr(obj, 'owner'):
                #print(f'Object {obj.__class__.__name__} Owner {obj.owner.__class__.__name__}')

    def clear(self):
        for obj in list(self.objects.values()):
            obj.deconstruct()



    def getPlayers(self):
        for obj in list(self.objects.values()):
            for comp in obj.components:
                if comp == "PlayerController":
                    return obj



