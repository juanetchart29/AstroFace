import random
import pygame

class Asteroid:
    def __init__(self, screen_width , screen_height,speed_level,inteligent_target_x, size=50, ):
        """
        Crea un asteroide que aparece en una posición aleatoria arriba de la pantalla
        y se mueve constantemente hacia abajo.
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.size = size
        self.speed = speed_level

        self.inteligent_target_x = inteligent_target_x
        self.is_active = True
        print(inteligent_target_x)
        if self.inteligent_target_x is not None:
            print("entre en el asteroide dirigido a la nave")

            self.x = inteligent_target_x + 20
        else:
            self.x = random.randrange(0, self.screen_width, 50) # cambiar posiciones random

        self.y = -size  # Siempre aparece arriba

        # Cargar imagen y definir el rectángulo para colisiones
        try:
            self.image = pygame.image.load("./assets/asteroid1.png")
            self.image = pygame.transform.scale(self.image, (size, size))
        except pygame.error:
            print("🚨 Error: No se pudo cargar la imagen. Verifica la ruta.")
            self.image = pygame.Surface((size, size))
            self.image.fill((150, 150, 150))  # Color gris de respaldo

        # Rect para colisiones
        self.rect = pygame.Rect(self.x, self.y, size, size)

    def update(self):
        """
        Mueve el asteroide hacia abajo y lo elimina si sale de la pantalla.
        """
        self.y += self.speed  # Mover hacia abajo
        self.rect.y = self.y  # Actualizar collider

        # Si el asteroide sale de la pantalla, reaparece arriba
        if self.y > self.screen_height:
            self.reset()

    def reset(self):
        self.is_active = False

    def draw(self, screen):
        """
        Dibuja el asteroide en la pantalla.
        """
        self.update()
        screen.blit(self.image, (self.x, self.y))

    def hit(self):
        """
        Función para manejar la colisión con la nave (puedes expandirla).
        """
        print("💥 ¡Colisión detectada con la nave!")
