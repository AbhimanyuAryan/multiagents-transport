from Classes.Route import Route
from Classes.Station import Station

class Bus:
    def __init__(self, idBus: int, capacity: int, route: Route, current_station: Station):
        self.idBus = idBus
        self.capacity = capacity
        self.route = route
        self.current_station = current_station
        self.passengers = 0
        self.running = False

    def to_dict(self):
        if self.route != None:
            route = self.route.to_dict()
        else:
            route = None
        if self.current_station != None:
            station = self.current_station.to_dict()
        else:
            station = None
        return {
            'idBus': self.idBus,
            'capacity': self.capacity,
            'route': route,
            'current_station': station,
            'running': self.running
        }

    @classmethod
    def from_dict(cls, data):
        idBus = data['idBus']
        capacity = data['capacity']
        if data['route'] != None:
            route = Route.from_dict(data['route'])
        else:
            route = None
        if data['current_station'] != None:
            current_station = Station.from_dict(data['current_station'])
        else:
            current_station = None
        running = data['running']
        bus = cls(idBus, capacity, route, current_station)
        bus.running = running
        return bus
    
    def add_passenger(self):
        self.passengers+=1

    def remove_passenger(self):
        self.passengers-=1

    def __str__(self) -> str:
        return f'Bus{self.idBus}{self.current_station.location}'
    
    def reset(self):
        self.running = False
        self.passengers = 0
        self.route = None
        self.current_station = None
