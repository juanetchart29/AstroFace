import pygame

class Ship:
    def __init__(self, x, y, size=40, color=(200, 0, 0)):
        """
        Representa un barco en el tablero.
        
        :param x: Posición en la grilla (columna).
        :param y: Posición en la grilla (fila).
        :param size: Tamaño del barco en píxeles.
        :param color: Color del barco.
        """
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, screen):
        """
        Dibuja el barco como un cuadrado en el tablero.
        """
        rect = pygame.Rect(self.x + self.size, self.y + self.size, self.size, self.size)
        pygame.draw.rect(screen, self.color, rect)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        print(self.x,self.y)