import pygame

class Button:
    def __init__(self, x, y, image, scale=1):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
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