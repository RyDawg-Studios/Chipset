import pygame
from data.topdownshooter.content.objects.player.net_shooter_controller import NetShooterController
from data.topdownshooter.content.objects.player.player import ShooterPlayer
import data.engine.fl.world_fl as wfl
from data.topdownshooter.content.objects.weapon.weapons.weapon import WeaponData
import data.topdownshooter.content.objects.weapon.weapons.weapon_table as wt

class NetShooterPlayer(ShooterPlayer):
    def __init__(self, man, pde, position=[0,0], hp=400):
        super().__init__(man, pde, position, hp)
        self.controller = NetShooterController(owner=self)

        self.pde.event_manager.net_events["add_weapon"] = self.addNetWeapon

    def addNetWeapon(self, data):
        print(f"\n {data} \n")
        wd = WeaponData(weaponClass=wt.weapon_table[data[0]['weapon_id']], upgrades=[])
        self.addweapon(wd)
        

    def onNetworkUpdate(self, data):
        super().onNetworkUpdate(data)
        net_pos = pygame.Vector2(data['attributes']['position'][0])
        if wfl.getpointdistance(self.rect.centerx, self.rect.centery, net_pos[0], net_pos[1]) != 0:
            self.rect.center = pygame.Vector2(net_pos)
