import pygame
from data.engine.player.player_controller import PlayerController

class ShooterController(PlayerController):
    def __init__(self, owner):
        super().__init__(owner)
        self.resetPos = True

    def on_input(self, input):
        if input == pygame.K_l:
            self.owner.pde.game.activate()
        if input == pygame.K_LSHIFT:
            self.owner.dodging = True
        if input == pygame.K_LALT:
            self.owner.altShot(target=self.owner.pde.input_manager.mouse_position)
        if input == pygame.K_f:
            self.owner.interact()
        if input == pygame.K_q:
            self.owner.cycleweapon()
        if input == pygame.K_k:
            self.owner.dead = True
        if input == pygame.K_m:
            self.owner.spawnmagnet()
        if input == pygame.K_j:
            self.owner.pde.network_manager.activate()

        return super().on_input(input)

    def manage_input(self):

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
        
        return super().manage_input()