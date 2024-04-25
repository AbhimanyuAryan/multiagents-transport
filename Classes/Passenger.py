from Classes.Bus import Bus
from Classes.Route import Route
from Classes.Station import Station


class Passenger:
    def __init__(self, idPassenger: int, route: Route, bus: Bus, initialStation: Station):
        self.idPassenger = idPassenger
        self.route = route
        self.bus = bus
        self.initialStation = initialStation

    def to_dict(self):
        return {
            'idPassenger': self.idPassenger,
            'route': self.route,
            'bus': self.bus,
            'initialStation':self.initialStation,
        }
    
    @classmethod
    def from_dict(cls,data):
        idPassenger = data['idPassenger']
        route = data['route']
        bus = data['bus']
        initialStation = data['initialStation']
        return Passenger(idPassenger,route,bus,initialStation)