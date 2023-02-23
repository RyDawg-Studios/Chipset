from data.topdownshooter.content.objects.weapon.weapons.weapons import DevGun, Pistol


class PlayerDataObject:
    def __init__(self):
        self.hp = 400
        self.maxhp = 400
        self.loadout = [Pistol]