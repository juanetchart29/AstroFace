class Player:
    def __init__(self, name):
        self.name = name
        self.ships = []

    def place_ship(self, ship):
        self.ships.append(ship)
