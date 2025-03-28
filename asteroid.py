import random
import pygame

class Asteroid:
    def __init__(self, screen_width , screen_height, size=50):
        """
        Crea un asteroide que aparece en una posición aleatoria arriba de la pantalla
        y se mueve constantemente hacia abajo.
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.size = size
        self.speed = 6 #random.randint(2, 5)

        # Posición inicial (aleatoria en X, arriba de la pantalla)
        # self.x = random.randint(0, max(0, screen_width - size))
        self.x = self.x = random.choice([50, 150, 250, 350, 450, 550])

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
        self.rect.y = self.y  # Actualizar colisión

        # Si el asteroide sale de la pantalla, reaparece arriba
        if self.y > self.screen_height:
            self.reset()

    def reset(self):
        """
        Reinicia el asteroide arriba con nueva posición X y velocidad.
        """
        self.x = self.x = random.choice([50, 150, 250, 350, 450, 550])
        self.y = -self.size  # Aparece arriba
        self.speed = random.randint(2, 5)
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        """
        Dibuja el asteroide en la pantalla.
        """
        print(self.x,self.y)
        self.update()
        screen.blit(self.image, (self.x, self.y))

    def hit(self):
        """
        Función para manejar la colisión con la nave (puedes expandirla).
        """
        print("💥 ¡Colisión detectada con la nave!")
