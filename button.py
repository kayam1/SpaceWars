import pygame
from settings import *

class Button:
    def __init__(self, image, x, y):
        self.image = image
        width = image.get_width()
        height = image.get_height()
        self.rect = self.image.get_rect()
        self.rect.topleft = (SCREEN_WIDTH * x - width // 2, SCREEN_HEIGHT * y - height // 2)
        self.clicked = False
        self.hovered = False
        self.last_mouse_state = False  # Track previous mouse state
        
    def draw(self, surface):
        # Check if mouse is hovering
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        surface.blit(self.image, (self.rect.x, self.rect.y))

        action = False
        mouse_pos = pygame.mouse.get_pos()
        current_mouse_pressed = pygame.mouse.get_pressed()[0]

        # Check for mouse release (toggle on release)
        if self.rect.collidepoint(mouse_pos):
            if self.last_mouse_state and not current_mouse_pressed:  # Mouse was pressed, now released
                action = True
                self.clicked = not self.clicked  # Toggle state
            
        # Update the last mouse state
        self.last_mouse_state = current_mouse_pressed
        
        return action