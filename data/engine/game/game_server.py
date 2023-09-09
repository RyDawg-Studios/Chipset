class GameServer:
    def __init__(self, pde):
        self.pde = pde

    def activate(self):
        self.pde.server_manager.server.onPlayerJoin_Dispatcher.bind(self.add_player)
        return

    def clearObjectManager(self):
        if self.pde.level_manager.level is not None:
            self.pde.level_manager.clearlevel()

    def update(self):
        pass

    def add_player(self, data):
        return

