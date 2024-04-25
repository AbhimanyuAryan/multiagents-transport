from Classes.Route import Route
from Classes.Passenger import Passenger
from Classes.Station import Station

class Bus:
    def __init__(self, idBus: int, capacity: int, route: Route, current_station: Station):
        self.idBus = idBus
        self.capacity = capacity
        self.route = route
        self.current_station = current_station
        self.passengers = []
        self.running = False

    def to_dict(self):
        return {
            'idBus': self.idBus,
            'capacity': self.capacity,
            'route': self.route.to_dict(),
            'current_station': self.current_station.to_dict(),
            'running': self.running
        }

    @classmethod
    def from_dict(cls, data):
        idBus = data['idBus']
        capacity = data['capacity']
        route = Route.from_dict(data['route'])
        current_station = Station.from_dict(data['current_station'])
        running = data['running']
        bus = cls(idBus, capacity, route, current_station)
        bus.running = running
        return bus
