import pygame
window = display.set_mode((700, 500))
display.set_caption("Ping-Pong")
#background = transform.scale(image.load(''), (700, 500))
#window.feel('blue')
clock = time.Clock()
FPS = 60
game = True 
while game:
  
    for e in event.get():
        if e.tipe == QUIT:
            game = False
    display.update() 
    
clock.tick(FPS)
