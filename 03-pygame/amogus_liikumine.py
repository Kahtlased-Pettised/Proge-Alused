import pygame
import random
ekraan = pygame.display.set_mode((1920,1080))
amogus = pygame.image.load("amogus.png")

LAIUS = 1920
KÕRGUS = 1080


kell = pygame.time.Clock()
pygame.init()

beebi = pygame.image.load("baby_amogus.png")

beebi_x = 300
beebi_y = 200
skoor = 0

gravi = 0.01
hüpe = 1
mäng_käib = True
amogus_x = 50
amogus_y = 50
kiirus_x = 0
kiirus_y = 0
KIIRUS = 0.5
font = pygame.font.SysFont("Comic Sans MS", 24)
tekst = font.render("Skoor: " + str(skoor),True, (255,0,0))

def beebi_juhustlik_punkt():
        x = random.randint(0, LAIUS - beebi_rect.w)
        y = random.randint(0, KÕRGUS - beebi_rect.h)
        return x,y

while mäng_käib:
    dt = kell.tick(60)
    #print(dt)
   
    for sisend in pygame.event.get():
        if sisend.type == pygame.QUIT:
            print("Vajutasid ristile!")
            mäng_käib = False
        elif sisend.type == pygame.KEYDOWN:
            if sisend.key == pygame.K_UP:
                kiirus_y = - hüpe
        elif sisend.type == pygame.MOUSEBUTTONDOWN:
            klõpsu_asukoht = pygame.mouse.get_pos()
            print("Klõps: "+ str(klõpsu_asukoht))
            if beebi_rect.collidepoint(klõpsu_asukoht):
                beebi_x, beebi_y = beebi_juhustlik_punkt()
           
    kiirus_x = 0
    kiirus_y += gravi
           
    vajutatud = pygame.key.get_pressed()
   
    if vajutatud[pygame.K_UP]:
        kiirus_y += -KIIRUS
    if vajutatud[pygame.K_DOWN]:
        kiirus_y += KIIRUS
           
    if vajutatud[pygame.K_RIGHT]:
        kiirus_x += KIIRUS
   
    if vajutatud[pygame.K_LEFT]:
        kiirus_x += -KIIRUS
       
    if kiirus_x and kiirus_y:
        kiirus_x /= 2**0.5
        kiirus_y /= 2**0.5
       
   
   
        """elif sisend.type == pygame.KEYDOWN:
            if sisend.key == pygame.K_RIGHT:
                kiirus_x = KIIRUS
            elif sisend.key == pygame.K_LEFT:
                kiirus_x = -KIIRUS
            elif sisend.key == pygame.K_UP:
                kiirus_y = -KIIRUS
            elif sisend.key == pygame.K_DOWN:
                kiirus_y = KIIRUS
        elif sisend.type == pygame.KEYUP:
            if sisend.key == pygame.K_UP or sisend.key == pygame.K_DOWN:
                kiirus_y = 0
            elif sisend.key == pygame.K_LEFT or sisend.key == pygame.K_RIGHT:
                kiirus_x = 0"""
               
    amogus_x += kiirus_x * dt
    amogus_y += kiirus_y * dt
 
    if amogus_y + amogus.get_height() > KÕRGUS:
        kiirus_y = 0
        amogus_y = KÕRGUS - amogus.get_height()
 
 
    ekraan.fill((155,89,182))
    beebi_rect = ekraan.blit(amogus, (amogus_x,amogus_y))
    amogus_rect = ekraan.blit(beebi, (beebi_x,beebi_y))
   
    if amogus_rect.colliderect(beebi_rect):
        beebi_x, beebi_y = beebi_juhustlik_punkt()
        skoor += 1
        #print(skoor)
        tekst = font.render("Skoor: " + str(skoor), True, (255,0,0))
   
    ekraan.blit(tekst, (0,0))
    pygame.display.flip()
   
pygame.quit()