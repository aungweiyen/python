import pygame
import random

WIDTH=360
HEIGHT=480
FPS=60

GREEN=(0,204,0)
BLACK=(0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Wei Yen's Game V2")
clock=pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.rect.center=(WIDTH/4,HEIGHT/4)
       
    def update(self):
        self.rect.x += 80
        if self.rect.left > WIDTH:
            self.rect.right=0
            
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((150,150))
        self.image.fill(GREEN)
        self.rect=self.image.get_rect()
        self.rect.center=(WIDTH/4,HEIGHT/5)
       
    def update(self):
        self.rect.x += 80
        if self.rect.left > WIDTH:
            self.rect.right=0
            
class Player3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((150,150))
        self.image.fill(BLUE)
        self.rect=self.image.get_rect()
        self.rect.center=(WIDTH/4,HEIGHT/6)
       
    def update(self):
        self.rect.x += 80
        if self.rect.left > WIDTH:
            self.rect.right=0

all_sprites = pygame.sprite.Group()
player = Player()
player2 = Player2()
player3 = Player3()
player4 = Player4()
all_sprites.add(player)
all_sprites.add(player2)
all_sprites.add(player3)
running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    all_sprites.update()    
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()