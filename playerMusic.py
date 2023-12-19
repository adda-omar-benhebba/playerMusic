import pygame
from pygame import mixer
import os

pygame.init()
mixer.init()
fenetre = pygame.display.set_mode((600, 400))
icone_suivant = pygame.image.load('icon_suivant.png')
icone_volume_plus = pygame.image.load('icon_volume_plus.png')
icone_volume_moins = pygame.image.load('icon_volume_moins.png')
largeur_icone = 50
hauteur_icone = 50
icone_pause = pygame.transform.scale(icone_pause, (largeur_icone, hauteur_icone))
icone_suivant = pygame.transform.scale(icone_suivant, (largeur_icone, hauteur_icone))
icone_volume_plus = pygame.transform.scale(icone_volume_plus, (largeur_icone, hauteur_icone))
icone_volume_moins = pygame.transform.scale(icone_volume_moins, (largeur_icone, hauteur_icone))

pistes = ['music1.mp3', 'music2.mp3', 'music3.mp3']
index_piste = 0 
images = ['image1.png', 'image2.png', 'image3.png']

chemin_absolu = os.path.abspath(pistes[index_piste])
mixer.music.load(chemin_absolu) 
image = pygame.image.load(images[index_piste])
mixer.music.play()

continuer = True
while continuer:
    fenetre.blit(image, (0, 0)) 
    
    espace = 10  
    marge_bas = fenetre.get_height() // 2 - hauteur_icone // 2  
    debut = fenetre.get_width() // 2 - (4 * largeur_icone + 3 * espace) // 2  
    fenetre.blit(icone_pause, (debut, marge_bas))
    fenetre.blit(icone_suivant, (debut + espace + largeur_icone, marge_bas))
    fenetre.blit(icone_volume_plus, (debut + 2*espace + 2*largeur_icone, marge_bas))
    fenetre.blit(icone_volume_moins, (debut + 3*espace + 3*largeur_icone, marge_bas))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            continuer = False 
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            x, y = pygame.mouse.get_pos() 
            
            if debut <= x <= debut + largeur_icone and marge_bas <= y <= marge_bas + hauteur_icone:
              
                if mixer.music.get_busy(): 
                    mixer.music.pause() 
                else:
                    mixer.music.unpause() 
            elif debut + espace + largeur_icone <= x <= debut + 2*espace + 2*largeur_icone and marge_bas <= y <= marge_bas + hauteur_icone:
                
                index_piste = (index_piste + 1) % len(pistes)
                chemin_absolu = os.path.abspath(pistes[index_piste]) 
                mixer.music.load(chemin_absolu) 
                mixer.music.play() 
                image = pygame.image.load(images[index_piste])

            elif debut + 2*espace + 2*largeur_icone <= x <= debut + 3*espace + 3*largeur_icone and marge_bas <= y <= marge_bas + hauteur_icone:
                volume = min(1, mixer.music.get_volume() + 0.1) 
                mixer.music.set_volume(volume)

            elif debut + 3*espace + 3*largeur_icone <= x <= debut + 4*espace + 4*largeur_icone and marge_bas <= y <= marge_bas + hauteur_icone:
                
                volume = max(0, mixer.music.get_volume() - 0.1) 
                mixer.music.set_volume(volume) 

    pygame.display.flip()
    

pygame.quit()