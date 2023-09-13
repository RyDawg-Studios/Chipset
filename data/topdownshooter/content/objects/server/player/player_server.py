from data.engine.actor.actor import Actor

from data.engine.sprite.sprite_component import SpriteComponent

from data.topdownshooter.content.objects.player.player import ShooterPlayer
from data.topdownshooter.content.objects.server.player.server_shooter_controller import ServerShooterController

class ShooterPlayerServer(ShooterPlayer):
    def __init__(self, man, pde, client=(0,0), position=[0,0]):
        super().__init__(man, pde, position=position)
        self.client = client

        self.controller = ServerShooterController(owner=self, client=self.client)

    def server_replicate_object(self, server, client):
        super().server_replicate_object(server, client)
        server.send_event({'message_type': 'event', 'message_data': {'event_name': 'spawn', 'event_args': [self.serialize()]}}, client)
        server.emit_event({'message_type': 'event', 'message_data': {'event_name': 'spawn', 'event_args': [self.serialize(_id = 'shooter_player')]}}, [client])

    def pickupweapon(self, obj):
        super().pickupweapon(obj)
        self.pde.server_manager.server.send_event({'message_type': 'event', 'message_data': {'event_name': 'add_weapon', 'event_args': [self.weapon.serialize()]}}, self.client)
        self.pde.server_manager.server.emit_event({'message_type': 'event', 'message_data': {'event_name': 'add_puppet_weapon', 'event_args': [self.weapon.serialize(), self.hash]}}, [self.client])

