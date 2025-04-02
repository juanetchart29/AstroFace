import pygame

class Board:
    def __init__(self, rows, cols, size_x, size_y):
        self.size = (size_x, size_y)
        self.rows = rows
        self.cols = cols
        self.grid_size = 40  # Cada celda es de 40x40 píxeles
        self.board = [[None for _ in range(cols)] for _ in range(rows)]

        # Cargar imagen de fondo
        self.image = pygame.image.load("./assets/bg5.jpg")
        self.image = pygame.transform.scale(self.image, self.size)  # Ajustar tamaño

        # Inicializar contador de vidas
        self.lives = 3  
        self.font = pygame.font.Font(None, 36)  # Fuente predeterminada de Pygame

    def draw(self, screen, ship):
        screen.blit(self.image, (0, 0))  # Dibujar imagen de fondo

        # Dibujar contador de vidas en la esquina superior derecha
        lives_text = self.font.render(f"Vidas: {ship.lives}", True, (255, 255, 255))  
        screen.blit(lives_text, (self.size[0] - 120, 10))  # Ajustar la posición

    def lose_lives(self):
        """Método para restar una vida"""
        if self.lives > 0:
            self.lives -= 1
