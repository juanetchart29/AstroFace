import pygame

class Settings:
    ship_speed = 10
    def get_fullScreen_size():
        pygame.init()
        info_pantalla = pygame.display.Info()  
        return info_pantalla.current_w, info_pantalla.current_h