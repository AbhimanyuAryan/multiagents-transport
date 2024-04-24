import jsonpickle
import random

class Station:
    def __init__(self,idstation : int,location_x : float,location_y : float):
        self.idStation = idstation
        self.location = (location_x,location_y)

    def to_dict(self):
        return {
            'idStation' : self.idStation,
            'location_x' : self.location[0],
            'location_y' : self.location[1]
        }
    
    @classmethod
    def from_dict(cls, data):
        idStation = data['idStation']
        location_x = data['location_x']
        location_y = data['location_y']
        return Station(idStation,location_x,location_y)

def generateStation(idStation) -> Station:
    return Station(idStation,random.uniform(0,20), random.uniform(0,20))