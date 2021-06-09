import pygame
import random
ekraan = pygame.display.set_mode((1920,1080))
amogus = pygame.image.load("amogus.png")
beebi = pygame.image.load("baby_amogus.png")
vaenlane = pygame.image.load("vaenlane.png")

LAIUS = 1920
KÕRGUS = 1080

kell = pygame.time.Clock()
pygame.init()

skoor = 0

KIIRUS = 0.5
kiirus_x = 0
kiirus_y = 0

amogus_x = 1000
amogus_y = 900

beebi_x = 0
beebi_y = 0

vaenlane_x = 0
vaenlane_y = 0 

mäng_käib = True

font = pygame.font.SysFont("Comic Sans MS", 24)
tekst = font.render("Skoor: " + str(skoor),True, (255,0,0))

def b_juhustlik_punkt():
        x = random.randint(0, LAIUS - beebi_rect.w)
        y = 0
        return x,y
def v_juhustlik_punkt():
        x = random.randint(0, LAIUS - vaenlane_rect.w)
        y = 0
        return x,y
    

while mäng_käib:
    dt = kell.tick(60)
    
    
    for sisend in pygame.event.get():
        if sisend.type == pygame.QUIT:
            print("Vajutasid ristile!")
            mäng_käib = False
          
    vajutatud = pygame.key.get_pressed()      
    
    if vajutatud[pygame.K_RIGHT]:
        kiirus_x += KIIRUS
    
    if vajutatud[pygame.K_LEFT]:
        kiirus_x += -KIIRUS
        
    """if kiirus_x and kiirus_y:
        kiirus_x /= 2**0.5
        kiirus_y /= 2**0.5"""
        
    amogus_x += kiirus_x #* dt
    amogus_y += kiirus_y #* dt
    
    if amogus_x + amogus.get_width() > LAIUS:
        kiirus_x = 0
        amogus_x = LAIUS - amogus.get_width()
    if amogus_x + amogus.get_width() < 0:
        kiirus_x = 0
        amogus_x = 0
          
    ekraan.fill((155,89,182))
    beebi_rect = ekraan.blit(beebi, (beebi_x,beebi_y))
    amogus_rect = ekraan.blit(amogus, (amogus_x,amogus_y))
    vaenlane_rect = ekraan.blit(vaenlane, (vaenlane_x,vaenlane_y))
    
    beebi_y += 5
    vaenlane_y += 5
    
    if amogus_rect.colliderect(vaenlane_rect):
        vaenlane_x, vaenlane_y = v_juhustlik_punkt()
        skoor -= 1
        tekst = font.render("Skoor: " + str(skoor), True, (255,0,0))
        print("Vaenlane")
        break
        
    if vaenlane_y > KÕRGUS:
        vaenlane_x, vaenlane_y = v_juhustlik_punkt()
    
    if amogus_rect.colliderect(beebi_rect):
        beebi_x, beebi_y = b_juhustlik_punkt()
        skoor += 1
        tekst = font.render("Skoor: " + str(skoor), True, (255,0,0))
        print("Beebi")
        
    if beebi_y > KÕRGUS:
        beebi_x, beebi_y = b_juhustlik_punkt()
        
    ekraan.blit(tekst, (0,0))
    pygame.display.flip()
    
pygame.quit()