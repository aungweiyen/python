import pygame
import random
import os

#color (rgb)
BLACK = (0,0,0)
WHITE = (255,255,255)

FPS = 90
WIDTH = 480
HEIGHT = 480

game_folder = os.pathdirname(__file__)
img_folder=os.path.join(game_folder,'img')
player_ing = pygame.image.load(os.path.join(img_folder, ' p1_jump.png')).convert()

pygame.init()
pygame.mixer_init()
screen = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("Wei Yen's Game V3")

class Player(pygame.sprite.Sprite):
    def __init__(self):
             pygame.sprite.Sprite.__init__(self)
             self.image= player_img
             self.image.setcolorkey(BLACK)
             self.react = self.image.get_rect()
             self.rect.center = (WIDTH/2,HEIGHT/2)
             
    def update(self):
        self.rect.x += 5
        self.y += self.y_speed
        if self.rect.bottom > HEIGHT -200:
            self.y_speed = -5
        if self_rect.top <200:
            self.y_speed = 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
            
all_sprites = pygame.sprite.Group()
player = Play()

all_sprites.add(player)

running = True

while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.Type == pygame.quit():
            running = False
    al_sprites.update()
    screen.fill(BLACK)
    
    
    
             
             
        
















class Player(PyGame.sprite.Sprites):
    def __init__(self):
        pygame.sprite.Sprites.__init__(self)
        
        
        def updtae(self):