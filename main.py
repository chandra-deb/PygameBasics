import pygame

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runnnner")
font = pygame.font.Font('font/Pixeltype.ttf', 50)

clock = pygame.time.Clock()

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
font_surface = font.render("Runnner", False, "blue")
snail_surface = pygame.image.load('graphics/snail/snail1.png')

snail_xpos = 800
snail_ypos = 290

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # screen.blit()
    screen.blits([
        (sky_surface,(0,0)),
        (ground_surface,(0,300)),
        (font_surface,(350,50)),
        (snail_surface,(snail_xpos,snail_ypos)),
        ])
    
    if(snail_xpos < -50):
        snail_xpos = 800
    else:
        snail_xpos -= 5

    pygame.display.update()

    # This is the max FPS
    clock.tick(60)