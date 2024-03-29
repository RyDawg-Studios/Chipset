import pygame
from data.engine.input.input_manager import InputManager
import sys

class EventManager:
    def __init__(self, pde) -> None:
        self.active = False
        self.pde = pde
        self.events = {}
        self.net_events = {}
        self.net_queue = []

    def activate(self):
        return
        
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                self.pde.input_manager.manage_inputs(event)
        
        for event in self.net_queue.copy():
            if event['message_type'] == 'event':
                if event['message_data']['event_name'] in self.net_events:
                    self.net_events[event['message_data']['event_name']](event['message_data']['event_args'])
                    self.net_queue.remove(event)
        return

    def handle_netevent_client(self, event):
        self.net_queue.append(event)


    def handle_netevent_server(self, event, client):
        if event['message_type'] == 'event':
            if event['message_data']['event_name'] in self.net_events:
                self.net_events[event['message_data']['event_name']](event['message_data']['event_args'], client)