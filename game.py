import pygame
from board import Board
from player import Player
from ship import Ship
from settings import Settings
from asteroid import Asteroid

class Game:
    def __init__(self):

        self.last_time = pygame.time.get_ticks()  
        self.interval = 3000

        
        x_max, y_max = Settings.get_fullScreen_size()
        self.ship = Ship(x_max, y_max)
        pygame.init()
        self.screen = pygame.display.set_mode((x_max,y_max))
        pygame.display.set_caption("Battleship")
        self.speed = Settings.ship_speed
        self.clock = pygame.time.Clock()  # Control de FPS

        self.asteroid_list = []


        self.running = True
        self.player = Player("Player 1")
        self.enemy = Player("AI")

        self.board = Board(10, 10,x_max,y_max)  

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)


        pygame.quit()

    def create_asteroid(self):
            my_asteroid = Asteroid(self.x_max,self.y_max)
            self.asteroid_list.append(my_asteroid)


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

        if (self.last_time - pygame.time.get_ticks())> self.interval :
            self.create_asteroid()
    def render(self):
        self.board.draw(self.screen)
        self.ship.draw(self.screen)
        pygame.display.flip()
