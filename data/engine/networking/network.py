import socket
import json

class Network():
    def __init__(self, owner, server="", port=5050):
        self.owner = owner
        self.server = server
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = (self.server, self.port)
        self.connected = False

    def connect(self):
        try:
            self.client.connect(self.address)
            self.connected = True
        except Exception as e:
            print(e)
        return

    def disconnect(self):
        self.connected = False
        self.client.close()
        return

    def send_event(self, event={'message_type': 'ping', 'message_data': {'data': "Default Message!"}}):
        print(f"Sending Event: {event}")
        try:
            dump = json.dumps(event)
        except Exception as e:
            print(f"Failed to dump JSON: {e}")
        
        data = bytes(dump, 'utf-8')
        self.client.sendall(data)

    def update(self):
        try:
            data = self.client.recv(1024).decode('utf-8')
            if data:
                data = json.loads(data)

                print(f"Receiving event: {data}")

                if data["message_type"] == 'ping':
                    print(data['message_data']['data'])
                elif data['message_type'] == 'event':
                    self.owner.pde.event_manager.handle_netevent(data)
                if not data:
                    self.disconnect()
                    
        except Exception as e:
            print(f"Error receiving message. Data: {data} | Error: {e}")
