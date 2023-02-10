import json
from data.engine.object.object import Object


class Upgrade(Object):
    def __init__(self, man, pde, weapon, id=None):
        #----------< Data Info >----------#
        self.id = id
        if self.id is not None:
            upgradedata = json.load(open(r"data\topdownshooter\data\upgradedata.json"))[self.id]

            self.name = upgradedata["textinfo"]["name"]
            self.description = upgradedata["textinfo"]["desc"]
            self.sprite = upgradedata["spriteinfo"]["sprite"]

        else:
            self.name = "Default Upgrade Name"
            self.description = "Default Upgrade Description"
            self.sprite = ''
            
        self.weapon = weapon
        super().__init__(man, pde)

    def update(self):
        return super().update()

    def onAltShot(self, target):
        return

    def onShot(self, bullet, target):
        return bullet, target

    def onHit(self, bullet, damage, object):
        return bullet, damage, object

    def onBulletUpdate(self, bullet):
        return bullet

    def onBulletDestruction(self, bullet):
        return bullet

    