import random
from data.engine.actor.actor import Actor
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.widgets.button import Button
from data.topdownshooter.content.objects.weapon.weapons.weapon import WeaponData
from data.topdownshooter.content.objects.widget.infobox import InfoBox
import data.topdownshooter.content.objects.weapon.weapons.weapon_table as wt

class PickupWeapon(Actor):
    def __init__(self, man, pde, position=[0, 0], speed=[4, 4], rotation=0, weaponData=None):
        super().__init__(man, pde)
        self.weaponData = weaponData
        self.weaponDict = dict()
        if weaponData is not None:
            self.weaponDict = dict(self.weaponData.serialize(man=self.man, pde=self.pde))
        self.position = position
        self.checkForCollision = False
        self.checkForOverlap = True
        self.useCenterForPosition = True
        self.speed = speed
        self.rotation = rotation
        self.rotdir = random.choice([-0.35, 0.35])
        self.rotticks = 0
        self.rottime = 100
        self.hoverframes = 0
        self.moveable = False

        self.infobox = None

        self.replicate = False
        self.replication_package = 'tds'
        self.replication_id = 'pickup_weapon'
        self.replicable_attributes = {
            "position": list,
            "weaponDict": dict,
            "rotation": int
        }

    def construct(self):
        print(self.position)


        self.weapon = wt.weapon_table[self.weaponDict["weapon_id"]](man=self.man, pde=self.pde, position=[0,0], owner=None)
        self.weapon.upgrades = self.weaponDict["weapon_upgrades"].copy()
        self.man.add_object(self.weapon)

        self.scale = self.weapon.scale

        
        super().construct()
        
        sprite = self.weapon.components["Sprite"].path

        self.components['Sprite'] = SpriteComponent(owner=self, sprite=sprite, layer=1)
        self.components["Projectile"] = ProjectileComponent(owner=self, rotation=self.rotation, speed=self.speed)
        self.components["Button"] = Button(owner=self)
        self.components["Button"].whilehovered = self.whilehovered
        self.components["Button"].whilenothovered = self.whilenothovered

        self.weapon.deconstruct()

    def update(self):
        self.rotticks += 1
        if self.rotticks >= self.rottime:
            self.components["Projectile"].rotation += self.rotdir
        self.components["Projectile"].speed[0] -= 0.2
        self.components["Projectile"].speed[1] -= 0.2

        if self.components["Projectile"].speed[0] < 0:
            self.components["Projectile"].speed[0] = 0
        if self.components["Projectile"].speed[1] < 0:
            self.components["Projectile"].speed[1] = 0

    def whilehovered(self):
        self.hoverframes += 1
        if self.infobox is None and self.hoverframes >= 30:
            self.infobox = self.man.add_object(obj=InfoBox(man=self.man, pde=self.pde, weapon=self.weapon))
        return

    def whilenothovered(self):
        if self.infobox is not None:
            self.infobox.deconstruct()
            self.infobox = None
        self.hoverframes = 0
        return
    
    def onNetworkSpawn(self, data):
        print(data)
        super().onNetworkSpawn(data)
        

    def deconstruct(self):
        super().deconstruct() 
        if self.infobox is not None:
            self.infobox.deconstruct()