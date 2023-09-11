import pygame

from data.engine.server.player.server_player_controller import ServerPlayerController

class ServerShooterController(ServerPlayerController):
    def __init__(self, owner, client=(0,0)):
        super().__init__(owner, client)
        self.resetPos = True
        self.axis = [0, 0, 0, 0, 0, 0]

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

        if pygame.K_RIGHT in self.key_inputs or pygame.K_d in self.key_inputs:
            self.owner.movement[0] = 1
        elif pygame.K_LEFT in self.key_inputs or pygame.K_a in self.key_inputs:
            self.owner.movement[0] = -1
        else:
            self.owner.movement[0] = 0
        if pygame.K_UP in self.key_inputs or pygame.K_w in self.key_inputs:
            self.owner.movement[1] = -1
        elif pygame.K_DOWN in self.key_inputs or pygame.K_s in self.key_inputs:
            self.owner.movement[1] = 1
        else:
            self.owner.movement[1] = 0

        if pygame.K_SPACE in self.key_inputs:
            self.owner.shootweapon(self.owner.pde.input_manager.mouse_position)
    
    def on_joystick(self, event):
        super().on_joystick(event)
        if event.axis <= 6:
            self.axis[event.axis] = event.value

        if self.axis[4] > 0.5:
            self.owner.dodging = True

        return

    
    def update(self):
        super().update()
        if len(self.inpman.joysticks) > 0:
            self.owner.movement = [round(self.axis[0]), round(self.axis[1])]

            if self.axis[5] > .5:
                if self.owner.weapon is not None:
                    self.owner.shootweapon(target=pygame.Vector2(self.owner.weapon.position) + (pygame.Vector2(self.axis[2], self.axis[3])*35))