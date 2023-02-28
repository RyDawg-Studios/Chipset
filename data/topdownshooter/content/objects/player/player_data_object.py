from data.topdownshooter.content.objects.weapon.weapons.weapons import DevGun, ElectroLauncher, Pistol, RiskGun


class PlayerDataObject:
    def __init__(self):
        self.hp = 400
        self.maxhp = 400
        self.loadout = [Pistol]