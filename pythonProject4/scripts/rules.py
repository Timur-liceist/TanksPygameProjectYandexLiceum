import pygame
from scripts.variables_for_menu import color_before
class Rules:
    def __init__(self, x, y, w, h):
        # (240,150,0)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.visible = False
        self.text_of_rules = list(map(lambda x: x.rstrip("\n"), open("data/rules_for_game.txt", "r", encoding="utf-8").readlines()))

        print(self.text_of_rules)
    def render(self, screen):
        if self.visible:
            # print(self.text_of_rules)
            pygame.draw.rect(screen, color_before, (self.x, self.y, self.w, self.h), 0)
            pygame.draw.rect(screen, (240,150,0), (self.x, self.y, self.w, self.h), 10)
            font = pygame.font.Font(None, 20)
            text = self.text_of_rules
            text_x, text_y = 30, 50
            for i in text:
                text = font.render(i, True, "black")
                text_w = text.get_width()
                text_h = text.get_height()
                screen.blit(text, (text_x, text_y))
                text_y += 15
    def set_visible(self, value):
        self.visible = value