import jsonpickle
import Station
import List

from Station import serializeStation, deserializeStation, generateStation

class Route:
    def __init__(self,idRoute : int, stations : List[Station]):
        self.idRoute = idRoute
        self.stations = stations

def serializeRoute(route : Route):
    send_json = {
        'idRoute' : route.idRoute,
        'stations' : [serializeStation(s) for s in route.stations]
    } 
    return jsonpickle.encode(send_json)

def deserializeRoute(msg_body) -> Route:
   received_json = jsonpickle.decode(msg_body)
   idRoute = received_json['idRoute']
   stations = received_json['stations']
   return Route(idRoute,[deserializeStation(s) for s in stations])

def generateRoute() -> Route:
    idRoute = 1
    stations = [generateStation(i) for i in range(20)]
    return Route(idRoute,stations)
    
