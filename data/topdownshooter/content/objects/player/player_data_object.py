from data.topdownshooter.content.objects.weapon.weapons.weapon import WeaponData
from data.topdownshooter.content.objects.weapon.weapons.weapons import AutoShotgun, Buckshot, DevGun, ElectroLauncher, FlamePistol, Friendship, Godray, LaserMachineGun, LooseChange, Musket, Pistol, RiskGun


class PlayerDataObject:
    def __init__(self):
        self.hp = 400
        self.maxhp = 400
        self.loadout = [WeaponData(LaserMachineGun)]
        self.currentWeapon = 1
        self.kills = 0