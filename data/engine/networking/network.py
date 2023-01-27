import socket
import json

class Network():
    def __init__(self, owner, server="", port=5050):
        self.owner = owner
        self.server = server
        self.port = port
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address = (self.server, self.port)
        self.connected = False


    def send_event(self, event):
        self.connection.sendto(event, self.connection)

    def update(self):
        try:
            data = self.connection.recvfrom(1024).decode('utf-8')
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
