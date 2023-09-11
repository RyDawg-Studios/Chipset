from data.topdownshooter.content.objects.player.net_shooter_player import NetShooterPlayer
from data.topdownshooter.content.objects.player.player import ShooterPlayer
from data.topdownshooter.content.objects.shooterentity.player_puppet import ShooterPuppet
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
from data.topdownshooter.content.objects.weapon.pickup.pickupweapon import PickupWeapon
from data.topdownshooter.content.objects.weapon.weapons.weapon import Weapon


object_table = {
    'controllable_player': NetShooterPlayer,
    'shooter_player': ShooterPuppet,
    'pickup_weapon': PickupWeapon,
    'weapon': Weapon
}