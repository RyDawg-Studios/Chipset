import pygame
from data.engine.player.player_controller import PlayerController

class NetShooterController(PlayerController):
    def __init__(self, owner):
        super().__init__(owner)
        self.resetPos = True
        self.axis = [0, 0, 0, 0, 0, 0]

        self.inpman.on_input_event.bind(self.on_keydown)
        self.inpman.on_output_event.bind(self.on_keyup)

    def on_input(self, input):
        super().on_input(input)

        if input == pygame.K_l or input == 4:
            self.owner.pde.game.restart()
        if input == pygame.K_LSHIFT:
            self.owner.dodging = True
        if input == pygame.K_LALT or input == 8:
            self.owner.altShot(target=self.owner.pde.input_manager.mouse_position)
        if input == pygame.K_f or input == 2:
            self.owner.interact()
        if input == pygame.K_q:
            self.owner.cycleweapon()
        if input == pygame.K_k:
            self.owner.dead = True
        if input == pygame.K_m:
            self.owner.spawnmagnet()
        if input == pygame.K_u:
            self.owner.openUpgradeSelectionUI()

        

        if input in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6]:
            print([pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6].index(input)+1)
            self.owner.switchweapon([pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6].index(input)+1)


    def manage_input(self):
        super().manage_input()

        if pygame.K_RIGHT in self.owner.pde.input_manager.key_inputs or pygame.K_d in self.owner.pde.input_manager.key_inputs:
            self.owner.movement[0] = 1
        elif pygame.K_LEFT in self.owner.pde.input_manager.key_inputs or pygame.K_a in self.owner.pde.input_manager.key_inputs:
            self.owner.movement[0] = -1
        else:
            self.owner.movement[0] = 0
        if pygame.K_UP in self.owner.pde.input_manager.key_inputs or pygame.K_w in self.owner.pde.input_manager.key_inputs:
            self.owner.movement[1] = -1
        elif pygame.K_DOWN in self.owner.pde.input_manager.key_inputs or pygame.K_s in self.owner.pde.input_manager.key_inputs:
            self.owner.movement[1] = 1
        else:
            self.owner.movement[1] = 0

        if pygame.K_SPACE in self.owner.pde.input_manager.key_inputs:
            self.owner.shootweapon(self.owner.pde.input_manager.mouse_position)
        
    
    def on_joystick(self, event):
        if event.axis <= 6:
            self.axis[event.axis] = event.value

        if self.axis[4] > 0.5:
            self.owner.dodging = True

        

        return super().on_joystick(event)
    
    def update(self):
        super().update()
        if len(self.inpman.joysticks) > 0:
            self.owner.movement = [round(self.axis[0]), round(self.axis[1])]

            if self.axis[5] > .5:
                if self.owner.weapon is not None:
                    self.owner.shootweapon(target=pygame.Vector2(self.owner.weapon.position) + (pygame.Vector2(self.axis[2], self.axis[3])*35))

    def on_keydown(self, data):
        self.owner.pde.network_manager.network.send_event({'message_type': 'event', 'message_data': {'event_name': 'input', 'event_args': [data, True]}})

    
    def on_keyup(self, data):
        self.owner.pde.network_manager.network.send_event({'message_type': 'event', 'message_data': {'event_name': 'input', 'event_args': [data, False]}})
