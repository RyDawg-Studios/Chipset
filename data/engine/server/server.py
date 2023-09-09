import pickle
import sys, socket
import json
import hashlib
import threading
from data.engine.eventdispatcher.eventdispatcher import EventDispatcher
from data.engine.server.connection import Connection

class Server():
    def __init__(self, pde, server="192.168.1.102", port=8080, maxClients=2):
        self.pde = pde
        self.server = server
        self.port = port
        self.maxClients = maxClients
        self.clients = []

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.server, self.port))

        self.pde.event_manager.net_events["update_game_state"] = self.update_game_state
        self.pde.event_manager.net_events["input"] = self.handle_input
        self.pde.event_manager.net_events["mouse"] = self.handle_mouse



        self.onPlayerJoin_Dispatcher = EventDispatcher()

        print("Server Started, Awaiting Connection")

    def update(self):
        data = self.sock.recvfrom(1024)
        self.handle_data(data)
        for object in self.pde.level_manager.level.objectManager.objects:
            if object.replicate:
                self.emit_event({'message_type': 'event', 'message_data': {'event_name': 'spawn', 'event_args': [object.serialize()]}})


    def emit_event(self, data):
        for cli in self.clients:
            self.send_event(data, cli)

    def send_event(self, data, cli):
        print(f"Sending: {data} to {cli}")
        dump = json.dumps(data)
        event = bytes(dump, "utf-8")
        self.sock.sendto(event, cli)
    
    def client_thread(self, pde, conn, addr):
        return

    def handle_data(self, data):
        if data[1] not in self.clients:
            print(data)
            self.clients.append(data[1])
            self.handle_new_client(data[1])
            self.onPlayerJoin_Dispatcher.call(data)
        self.handle_event(data[0], data[1])   

    def handle_event(self, data, client):
            if data:
                data = json.loads(data)

                print(f"Receiving event: {data} from {client}")

                if data["message_type"] == 'ping':
                    print(data['message_data']['data'])
                elif data['message_type'] == 'event':
                    self.pde.event_manager.handle_netevent_server(data, client)


    def handle_new_client(self, address):
        print(f"New connection from {address}")       
        self.send_event({'message_type': 'ping', 'message_data': {'data': 'Welcome!', 'event_args': []}}, address)

    def update_game_state(self, data, client):
        for object in self.pde.level_manager.level.objectManager.objects:
            if object.replicate:
                self.send_event({'message_type': 'event', 'message_data': {'event_name': 'spawn', 'event_args': [object.serialize()]}}, client)
        
    def handle_input(self, data, client):
        self.pde.input_manager.handle_net_input(data, client)

    def handle_mouse(self, data, client):
        self.pde.input_manager.handle_net_mouse(data, client)
