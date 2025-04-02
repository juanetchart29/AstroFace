import pygame

class Settings:
    ship_speed = 10
    fps = 600
    asteroid_imgs = [
        "./assets/asteroid/asteroid1.png",
        "./assets/asteroid/asteroid2.png",
        "./assets/asteroid/asteroid3.png",
        "./assets/asteroid/asteroid4.png",
    ]
    debug = True
    # mode = "manual"
    mode = "video"
    def get_fullScreen_size():
        pygame.init()
        info_pantalla = pygame.display.Info()  
        return info_pantalla.current_w, info_pantalla.current_h