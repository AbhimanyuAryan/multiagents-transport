import Route

class Bus:
    def __init__(self, idBus: int, route: Route, location: tuple, running: bool):
        self.idBus = idBus
        self.route = route
        self.location = location
        self.running = running

    def register_bus(self, bus):
        # Implement bus registration logic here
        pass

    def set_route(self, route):
        # Implement route setting logic here
        pass

    def starting_route(self, route):
        # Implement starting route logic here
        pass

    def end_route(self, route):
        # Implement ending route logic here
        pass

    def update_location(self, location):
        # Implement location update logic here
        pass
