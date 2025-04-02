import random
import pygame
from settings import Settings

class Asteroid:
    def __init__(self, screen_width, screen_height, speed_level, inteligent_target_x, size=50):
        """
        Crea un asteroide que aparece en una posición aleatoria arriba de la pantalla
        y se mueve constantemente hacia abajo con animación.
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.size = size
        self.speed = speed_level
        self.is_active = True

        # Posición inicial
        self.x = inteligent_target_x if inteligent_target_x is not None else random.randrange(0, self.screen_width, 50)
        self.y = -size  

        # Cargar imágenes de la animación desde Settings.asteroid_imgs
        self.frames = [pygame.image.load(img) for img in Settings.asteroid_imgs]
        self.frames = [pygame.transform.scale(img, (size, size)) for img in self.frames]
        
        self.frame_index = 0  # Índice del frame actual
        self.animation_speed = 20  # Cambia cada 5 ciclos de update
        self.frame_counter = 0  # Contador de ciclos

        # Rect para colisiones
        self.rect = pygame.Rect(self.x, self.y, size, size)

    def update(self):
        """
        Mueve el asteroide y actualiza la animación.
        """
        self.y += self.speed  # Mover hacia abajo
        self.rect.y = self.y  # Actualizar collider

        # Actualizar animación
        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.frame_index = (self.frame_index + 1) % len(self.frames)  # Cambia al siguiente frame
            self.frame_counter = 0  # Reiniciar contador

        # Si el asteroide sale de la pantalla, lo desactiva
        if self.y > self.screen_height:
            self.reset()

    def reset(self):
        """ Desactiva el asteroide. """
        self.is_active = False

    def draw(self, screen):
        """ Dibuja el asteroide animado en la pantalla. """
        self.update()
        screen.blit(self.frames[self.frame_index], (self.x, self.y))

        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

    

