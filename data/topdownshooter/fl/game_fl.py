import random
from data.topdownshooter.content.objects.weapon.weapons.weapons import SMG, AutomaticRifle, GrenadeLauncher, LaserMachineGun, Shotgun, SniperRifle


def chooseRandomWeapon():
    w = random.choice([SMG, AutomaticRifle, SniperRifle, LaserMachineGun, GrenadeLauncher, Shotgun])
    return w