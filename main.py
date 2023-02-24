import pygame

pygame.init()
screen =pygame.display.set_mode((1920,1080),)
pygame.display.set_caption("new game")
#icon =pygame.image.load('images/icon.png')
square =pygame.Surface((500,400))
bg= pygame.image.load("image/bg.png")

running=True
while (running):
    
    screen.blit(bg(-100,-100))
    pygame.draw.circle(screen,'Red',(250,100),30)
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
            pygame.quit()
        

    