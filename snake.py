import pygame
import random
pygame.init()


def lines():
    pygame.draw.line(screen, white, (20, 20), (20, height-20))
    pygame.draw.line(screen, white, (20, 20), (width - 20, 20))
    pygame.draw.line(screen, white, (20, height-20), (width - 20, height-20))
    pygame.draw.line(screen, white, (width - 20, 20), (width - 20, height-20))


def snake(h, lista):
    c = (100, 255, 0)
    for i in lista:
        pygame.draw.rect(screen, c, [i[0], i[1], h, h])
        if c == (100, 255, 0):
            c = (100, 200, 0)
        elif c == (100, 200, 0):
            c = (10, 150, 0)
        elif c == (10, 150, 0):
            c = (100, 255, 0)


clock = pygame.time.Clock()

width = 1000
height = 600
white = (255, 255, 255)
wonsz = pygame.image.load('snake.png')


krok = 10
x_change = 0
y_change = 0
length_wonsz = 0
snake_List = []

delta = 0.0
box = pygame.Rect(width/2.0, height/2.0, krok, krok)
max_tps = 120.0
food_x = round(random.randrange(20, width - 30) / 10.0) * 10
food_y = round(random.randrange(20, height - 30) / 10.0) * 10
count = 0

czcionka = pygame.font.SysFont('comicsans', 50)

napis2 = czcionka.render('Przegrałeś!', True, (255, 255, 255))

pygame.display.set_caption('Moja pierwsza gra w Python')  # title
screen = pygame.display.set_mode((width, height))
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            game_over = True

    lines()

    pygame.draw.rect(screen, (255, 0, 0), box)
    food = pygame.draw.rect(screen, (0, 0, 255), (food_x, food_y, krok, krok))

    pygame.display.update()
    # Ticking
    delta += clock.tick()/5000.0
    while delta > 1/max_tps:
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            y_change = krok
            x_change = 0
        elif pygame.key.get_pressed()[pygame.K_UP]:
            y_change = -krok
            x_change = 0
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            x_change = krok
            y_change = 0
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            x_change = -krok
            y_change = 0

        box.x += x_change
        box.y += y_change
        screen.fill((0, 0, 0))

        if box.x < 20 or box.x >= width - 20 or box.y >= height - 20 or box.y < 20:
            screen.fill((0, 0, 0))
            screen.blit(napis2, (width/2.0-60, height/2.0))
            screen.blit(wonsz, (20, 20))
            pygame.display.update()
            print('Przegrałeś!')
            pygame.time.wait(1000)
            box.x = width/2.0
            box.y = height/2.0
            x_change = 0
            y_change = 0
            count = 0
            length_wonsz = 0
            snake_List = []

        if box.x == food_x and box.y == food_y:
            print('YUMMY!')
            count += 1
            length_wonsz += 1
            print('Twój wynik: ', count)
            food_x = round(random.randrange(20, width - 30) / 10.0) * 10
            food_y = round(random.randrange(20, height - 30) / 10.0) * 10
        napis = czcionka.render('Twój wynik: ' + str(count), True, (255, 255, 255))
        screen.blit(napis, (40, 50))
        snake_Head = [box.x, box.y]
        snake_List.append(snake_Head)
        snake(krok, snake_List)

        if len(snake_List) > length_wonsz:
            del snake_List[0]

        delta -= 1/max_tps
quit()
