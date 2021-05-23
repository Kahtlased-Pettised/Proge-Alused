import pygame
ekraan = pygame.display.set_mode((1920,1080))
amogus = pygame.image.load("amogus.png")

LAIUS = 1920
KÕRGUS = 1080


kell = pygame.time.Clock()
pygame.init()

amogus_x = 50
amogus_y = 50
kiirus_x = 0.5
kiirus_y = 0.5

"""font = pygame.font.SysFont("Comic Sans MS", 24)
tekst = font.render("SUS", True, (255,0,0))
ekraan.blit(tekst, (100,50))"""

while True:
    dt = kell.tick(60)
    print(dt)
    sisend = pygame.event.poll()
    if sisend.type == pygame.QUIT:
        print("Vajutasid ristile!")
        break
    amogus_x += kiirus_x * dt
    amogus_y += kiirus_y * dt
    if amogus_x + amogus.get_width() > LAIUS:
        kiirus_x = -0.5
       # amogus = pygame.transform.flip(amogus,)
    elif amogus_x < 0:
        kiirus_x = 0.5
       
    if amogus_y + amogus.get_height() > KÕRGUS:
        kiirus_y = -0.5
    elif amogus_y < 0:
        kiirus_y = 0.5
   
    ekraan.fill((155,89,182))
    ekraan.blit(amogus, (amogus_x,amogus_y))
    pygame.display.flip()
pygame.quit()