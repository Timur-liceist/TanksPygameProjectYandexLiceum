import os
import sys
import pygame
import requests
import pygame_gui

coords = [37.530887, 55.703118]
mashtab = 0.002
map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords[0]},{coords[1]}&spn={mashtab},{mashtab}&l=map"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)
pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
run = True
manager = pygame_gui.UIManager((800, 600))
step = 0.0005
upping = False
downing = False
lefting = False
righting = False
type_map = "Схема"
clock = pygame.time.Clock()
combobox = pygame_gui.elements.UIDropDownMenu(manager=manager,
                                              relative_rect=pygame.Rect((10, 10), (125, 30)),
                                              options_list=["Гибрид", "Спутник", "Схема"],
                                              starting_option="Схема")
dic = {"Гибрид": "sat,skl", "Спутник": "sat", "Схема": "map"}
while run:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == combobox:
                    type_map = event.text
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:

                print(1)
                mashtab *= 1.5
                map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords[0]},{coords[1]}&spn={mashtab},{mashtab}&l={dic[type_map]}"
                response = requests.get(map_request)
                if not response:
                    # mashtab *= 0.01
                    break
            if event.key == pygame.K_PAGEDOWN:
                print(2)
                mashtab /= 1.5
                map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords[0]},{coords[1]}&spn={mashtab},{mashtab}&l={dic[type_map]}"
                response = requests.get(map_request)
                if not response:
                    # mashtab += 0.01
                    mashtab *= 1.5
                    break
            if event.key == pygame.K_UP:
                upping = True
            if event.key == pygame.K_DOWN:
                downing = True
            if event.key == pygame.K_LEFT:
                lefting = True
            if event.key == pygame.K_RIGHT:
                righting = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                upping = False
            if event.key == pygame.K_DOWN:
                downing = False
            if event.key == pygame.K_LEFT:
                lefting = False
            if event.key == pygame.K_RIGHT:
                righting = False

        manager.process_events(event)

    manager.update(time_delta)
    if upping:
        coords[1] += step * mashtab * 70
    if lefting:
        coords[0] -= step * mashtab * 90
    if righting:
        coords[0] += step * mashtab * 90
    if downing:
        coords[1] -= step * mashtab * 70
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords[0]},{coords[1]}&spn={mashtab},{mashtab}&l={dic[type_map]}"
    response = requests.get(map_request)
    if not response:
        mashtab -= 0.1
        break
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen.blit(pygame.image.load(map_file), (0, 0))
    manager.draw_ui(screen)
    pygame.display.flip()
pygame.quit()
os.remove(map_file)
