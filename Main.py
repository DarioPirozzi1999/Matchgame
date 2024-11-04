import pygame
pygame.init()

screen = pygame.display.set_mode((800,800))
screen.fill("black")

font = pygame.font.SysFont("Times New Roman", 50)

candyCrush= pygame.image.load("CandyCrush.jpg")
subwaySurfers= pygame.image.load("SubwaySurfers.png")
ludo = pygame.image.load("ludo.png")
templeRun = pygame.image.load("TempleRun.png")
pixelGun = pygame.image.load("PixelGun.png")
pixelGun2 = pygame.transform.scale(pixelGun, (90, 90))
tCandyCrush = font.render("Candy Crush",True,  (255,255,255))
tSubwaySurfers = font.render("Subway Surfers",True,  (255,255,255))
tLudo = font.render("Ludo",True,  (255,255,255))
tTempleRun = font.render("Temple Run",True,  (255,255,255))
tPixelGun = font.render("Pixel Gun", True, (255,255,255))
screen.blit(subwaySurfers, (200,200))
screen.blit(candyCrush, (200,300))
screen.blit(ludo, (200, 400))
screen.blit(templeRun, (200, 500))
screen.blit(pixelGun2, (200,600))
screen.blit(tTempleRun, (400, 200))
screen.blit(tLudo, (400, 400))
screen.blit(tCandyCrush, (400, 500))
screen.blit(tSubwaySurfers, (400, 600))
screen.blit(tPixelGun, (400, 300))

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            pygame.draw.circle(screen, (255,255,255), pos, 10, 0)
        if event.type ==  pygame.MOUSEBUTTONUP:
            position2 = pygame.mouse.get_pos()
            pygame.draw.line(screen, (255, 255, 255), pos, position2, 5)
            pygame.draw.circle(screen, (255,255,255), position2, 10, 0)



