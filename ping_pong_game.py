import pygame
window = display.set_mode((700, 500))
display.set_caption("Ping-Pong")
#background = transform.scale(image.load(''), (700, 500))
#window.feel('blue')
clock = time.Clock()
FPS = 60
class GameSprite(sprite.Sprite):
        def __init__(self, image_pl, x_pl, y_pl, speed_pl):
            super().__init__()
            self.image = transform.scale(image.load(image_pl), (80, 80))
            self.rect = self.image.get_rect()
            self.rect.x = x_pl
            self.rect.y = y_pl
            self.speed = speed_pl
        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))
            
class Player(GameSprite):
        def update(self):
            keys_pressed = key.get_pressed()
            if keys_pressed[K_RIGHT] and self.rect.y < 635:
                self.rect.y += self.speed
            if keys_pressed[K_LEFT] and self.rect.y > 0:
                self.rect.y -= self.speed 
class Ball(gameSprite):
        def update(self):
                if self.rect.y  == 
player = Player('player', 20, 200, 10)
player2 = Player('player', 560, 200, 10)
ball = Ball('ball', 100, 100, 20)
game = True 
while game:
   
    for e in event.get():
        if e.tipe == QUIT:
            game = False
    player.reset()
    player2.reset()
    display.update() 
    clock.tick(FPS)
