from data.topdownshooter.content.objects.weapon.weapons.weapons import AutoShotgun, DevGun, ElectroLauncher, FlamePistol, Friendship, Godray, LooseChange, Musket, Pistol, RiskGun


class PlayerDataObject:
    def __init__(self):
        self.hp = 400
        self.maxhp = 400
        self.loadout = [Pistol]