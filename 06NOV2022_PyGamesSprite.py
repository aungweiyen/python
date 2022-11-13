import pygame

GREY=(32,32,32)
BLACK=(0,0,0)
WIDTH=360
HEIGHT=480

FPS=60
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Wei Yen's Game")
clock=pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(BLACK)
        self.rect=self.image.get_rect()
        self.rect.center=(WIDTH/3,HEIGHT/3)
       
    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right=0
 
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    all_sprites.update()
    screen.fill(GREY)
    all_sprites.draw(screen)
       
       
    pygame.display.flip()

pygame.quit()


