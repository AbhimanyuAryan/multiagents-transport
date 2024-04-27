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
    
    def __str__(self) -> str:
        return f'Station({self.idStation},{self.location[0]},{self.location[1]})'

def generateStation(idStation,x,y) -> Station:
    return Station(idStation,x,y)