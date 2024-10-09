import pygame

pygame.font.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("space invaders")
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
border = pygame.Rect(WIDTH//2-5,0,10,HEIGHT)

HEALTH_FONT =  pygame.font.SysFont("ariel",45)
WINNER_FONT =  pygame.font.SysFont("comicsans",100)

FPS = 60
VELOCITY = 5

BULLET_VELOCITY = 7
MAX_BULLET = 3
SHIP_WIDTH = 55
SHIP_HEIGHT = 40

y_ship_image = pygame.image.load("assets/spaceship_yellow.png")
y_ship_image = pygame.transform.scale(y_ship_image,(SHIP_WIDTH,SHIP_HEIGHT))
yellow_ship = pygame.transform.rotate(y_ship_image,90)

r_ship_image = pygame.image.load("assets/spaceship_red.png")
r_ship_image = pygame.transform.scale(r_ship_image,(SHIP_WIDTH,SHIP_HEIGHT))
red_ship = pygame.transform.rotate(r_ship_image,270)

space_image = pygame.image.load("assets/space.png")
space = pygame.transform.scale(space_image,(WIDTH,HEIGHT))

def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    screen.blit(space,(0,0))
    pygame.dreaw.rect(screen,BLACK,border)
    red_health_text = HEALTH_FONT.render("health:"+str(red_health),1,WHITE)
    yellow_health_text = HEALTH_FONT.render("Health:"+str(yellow_health),1,WHITE)
    screen.blit(red_health_text,(WIDTH-red_health_text.get_width()-10,10))
    screen.blit(yellow_health_text,(10,10))
    screen.blit(red_ship,(red_ship.x,red_ship.y))
    screen.blit(yellow_ship,(yellow_ship.x,yellow_ship.y))

    for bullet in red_bullets:
        pygame.draw.rect(screen,RED,bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(screen,YELLOW,bullet)

# yellow awsd

def yellow_movement(keys_pressed,yellow_ship):
    if keys_pressed[pygame.K_a] and yellow_ship.x - VELOCITY > 0:
        yellow_ship.x -= VELOCITY
    if keys_pressed[pygame.K_d] and yellow_ship.x + VELOCITY + yellow_ship.width < border.x :
        yellow_ship.x += VELOCITY
    if keys_pressed[pygame.K_w] and yellow_ship.y - VELOCITY > 0:
        yellow_ship.y -= VELOCITY
    if keys_pressed[pygame.K_s] and yellow_ship.y + VELOCITY + yellow_ship.HEIGHT - 15:
        yellow_ship.y += VELOCITY




