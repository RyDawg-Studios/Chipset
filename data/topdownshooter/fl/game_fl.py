import random
from data.topdownshooter.content.objects.weapon.weapons.weapons import SMG, AutomaticRifle, ElectroLauncher, GrenadeLauncher, LaserMachineGun, Shotgun, SniperRifle


def chooseRandomWeapon():
    w = random.choice([SMG, AutomaticRifle, SniperRifle, LaserMachineGun, GrenadeLauncher, Shotgun, ElectroLauncher])
    return w