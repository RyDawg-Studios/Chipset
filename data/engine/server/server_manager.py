from data.engine.server.server import Server
import threading


class ServerManager():
    def __init__(self, pde):
        self.pde = pde
        self.active = False
        self.server = None
        
    def server_thread(self):
        self.server = Server(pde=self.pde, server="127.0.0.1")

        while True:
            self.server.update()

    def activate(self):
        print("Server Manager Active")
        t = threading.Thread(target=self.server_thread)
        t.start()

    def update(self):
        for object in self.pde.level_manager.level.objectManager.objects:
            if object.replicate:
                self.server.emit_event({'message_type': 'event', 'message_data': {'event_name': 'spawn', 'event_args': [object.serialize()]}})
        return

    def disconnect(self):
        return