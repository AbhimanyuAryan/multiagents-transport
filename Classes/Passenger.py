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
        if self.bus != None:
            value = self.bus.to_dict()
        else:
            value = None
        return {
            'idPassenger': self.idPassenger,
            'route': self.route.to_dict(),
            'bus':value,
            'initialStation':self.initialStation.to_dict(),
        }
    
    @classmethod
    def from_dict(cls,data):
        idPassenger = data['idPassenger']
        route = Route.from_dict(data['route'])
        if data['bus'] != None:
            bus = Bus.from_dict(data['bus'])
        else:
            bus = None
        initialStation = Station.from_dict(data['initialStation'])
        return Passenger(idPassenger,route,bus,initialStation)