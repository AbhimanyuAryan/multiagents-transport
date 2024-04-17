import jsonpickle
import random

class Station:
    def __init__(self,idstation : int,location_x : float,location_y : float):
        self.idStation = idstation
        self.location = (location_x,location_y)

def serializeStation(station : Station):
    send_json = {
        'idStation' : station.idStation,
        'location_x' : station.location[0],
        'location_y' : station.location[1]
    } 
    return jsonpickle.encode(send_json)

def deserializeStation(msg_body) -> Station:
   received_json = jsonpickle.decode(msg_body)
   idStation = received_json['idStation']
   location_x = received_json['location_x']
   location_y = received_json['location_y']
   return Station(idStation,location_x,location_y)

def generateStation(idStation) -> Station:
    return Station(idStation,random.uniform(0,20), random.uniform(0,20))