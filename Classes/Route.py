from Classes.Station import Station, generateStation
from typing import List

class Route:
    def __init__(self,idRoute : int, stations : List[Station]):
        self.idRoute = idRoute
        self.stations = stations

    def to_dict(self):
        return {
            'idRoute' : self.idRoute,
            'stations' : [s.to_dict() for s in self.stations]
        }
    
    @classmethod
    def from_dict(cls, data):
        idRoute = data['idRoute']
        stations = data['stations']
        return Route(idRoute,[Station.from_dict(s) for s in stations])
    
    def hasStation(self,station : Station):
        ids = [s.idStation for s in self.stations]
        return station.idStation in ids

def generateRoute() -> Route:
    idRoute = 1
    stations = [generateStation(i,i,i) for i in range(10)]
    return Route(idRoute,stations)
    
