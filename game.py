import pygame
from board import Board
from player import Player
from ship import Ship
from settings import Settings

class Game:
    def __init__(self):
        self.ship = Ship(0, 600)
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Battleship")
        self.speed = Settings.ship_speed
        self.clock = pygame.time.Clock()  # Control de FPS


        self.running = True
        self.player = Player("Player 1")
        self.enemy = Player("AI")

        self.board = Board(10, 10)  

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)


        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:  
                # Capturar clic del mouse y obtener coordenadas
                mouse_x, mouse_y = pygame.mouse.get_pos()
                grid_x = mouse_x
                grid_y = mouse_y 
                print(f"Clic en coordenadas vectoriales: ({grid_x}, {grid_y})")

    def update(self):
        keys = pygame.key.get_pressed()  # Obtiene el estado de las teclas en cada frame
        if keys[pygame.K_LEFT]:
            self.ship.move(-self.speed, 0)
        if keys[pygame.K_RIGHT]:
            self.ship.move(self.speed, 0)
        if keys[pygame.K_UP]:
            self.ship.move(0, -self.speed)
        if keys[pygame.K_DOWN]:
            self.ship.move(0, self.speed)

    def render(self):
        self.screen.fill((0, 0, 50))  # Dark blue background
        self.board.draw(self.screen)
        self.ship.draw(self.screen)
        pygame.display.flip()
