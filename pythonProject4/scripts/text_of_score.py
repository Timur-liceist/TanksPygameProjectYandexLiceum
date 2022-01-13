import pygame
class Text:
    def __init__(self, x, y, size_text, text):
        self.x = x
        self.size_text = size_text
        self.y = y
        self.text = text
    def render(self, screen):
        font = pygame.font.Font(None, self.size_text)
        text = font.render(self.text, True, "gold")
        text_x = self.x
        text_y = self.y
        # text_w = text.get_width()
        # text_h = text.get_height()
        screen.blit(text, (text_x, text_y))