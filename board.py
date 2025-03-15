import pygame

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid_size = 40  # Each cell is 40x40 pixels
        self.board = [[None for _ in range(cols)] for _ in range(rows)]

    def draw(self, screen):
        screen.fill((0, 0, 255))  # RGB: (0, 0, 255) es azul puro