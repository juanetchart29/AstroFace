import pygame
from board import Board
from player import Player
from ship import Ship
from settings import Settings
from asteroid import Asteroid



class Game:
    def __init__(self):
        self.fps = Settings.fps
        self.asteroid_last_time = pygame.time.get_ticks()  
        self.asteroid_interval = 1000
        self.level_timer = pygame.time.get_ticks()  
        self.level_interval = 10000
        self.inteligent_target_last_time = pygame.time.get_ticks()
        self.level = 8

        self.inteligent_target_interval = 4000
        
        self.x_max, self.y_max = Settings.get_fullScreen_size()
        self.ship = Ship(self.x_max, self.y_max, Settings.mode)
        pygame.init()
        self.screen = pygame.display.set_mode((self.x_max,self.y_max))
        pygame.display.set_caption("Battleship")
        self.speed = Settings.ship_speed
        self.clock = pygame.time.Clock()  # Control de FPS

        self.asteroid_list = []


        self.running = True
        self.player = Player("Player 1")
        self.enemy = Player("AI")

        self.board = Board(10, 10,self.x_max,self.y_max)  

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.fps)
            self.asteroid_manager()
            self.level_manager()



        pygame.quit()




    def level_manager(self):
        if pygame.time.get_ticks() - self.level_timer > self.level_interval:
            self.level_timer = pygame.time.get_ticks()
            self.level += 1

    def asteroid_manager(self):
        if pygame.time.get_ticks() - self.asteroid_last_time > self.asteroid_interval:
            self.asteroid_last_time = pygame.time.get_ticks()
            self.create_asteroid()
        if pygame.time.get_ticks() - self.inteligent_target_last_time > self.inteligent_target_interval:
            self.inteligent_target_last_time = pygame.time.get_ticks()
            self.create_asteroid(inteligent_target_x = self.ship.rect.x)
                   

    def create_asteroid(self, inteligent_target_x = None ):
        if inteligent_target_x is not None:
            my_asteroid = Asteroid(self.x_max,self.y_max, self.level,inteligent_target_x = inteligent_target_x)
        else: 
            my_asteroid = Asteroid(self.x_max,self.y_max, self.level,None )    
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

        for asteroid in self.asteroid_list:
            if asteroid.is_active:
                asteroid.update()
                if self.ship.rect.colliderect(asteroid.rect):  
                    self.handle_collision()
            else:
                self.asteroid_list.remove(asteroid)

    def handle_collision(self):
        if self.ship.lives <= 1:
            self.running = False
            print("Game Over")
        for asteroid in self.asteroid_list:
            if asteroid.is_active and self.ship.rect.colliderect(asteroid.rect):
                asteroid.reset()
                self.ship.lives -= 1

    def render(self):
        self.board.draw(self.screen, self.ship)
        self.ship.draw(self.screen)
        for asteroid in self.asteroid_list:
            asteroid.draw(self.screen)
        pygame.display.flip()
