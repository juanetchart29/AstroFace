import pygame

class Board:
    def __init__(self, rows, cols,size_x,size_y):
        self.size = (size_x, size_y)
        self.rows = rows
        self.cols = cols
        self.grid_size = 40  # Each cell is 40x40 pixels
        self.board = [[None for _ in range(cols)] for _ in range(rows)]

        self.image = pygame.image.load("./assets/bg5.jpg")
        self.image = pygame.transform.scale(self.image, self.size)  # Ajustar tamaño
    def draw(self, screen):
        screen.blit(self.image, (0, 0))  # Dibujar imagen