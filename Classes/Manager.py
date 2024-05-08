from Classes.Route import Route, generateRoute
from Classes.Passenger import Passenger
from Classes.Bus import Bus
import random
from typing import List

class Manager:
    def __init__(self):
        self.buses = {}
        self.passengers = {}
        route = generateRoute()
        self.routes = {route.idRoute : route}

    def add_bus(self,bus : Bus):
        self.buses[bus.idBus] = bus

    def add_passenger(self,passenger : Passenger):
        self.passengers[passenger.idPassenger] = passenger

    def add_route(self,route : Route):
        self.routes[route.idRoute] = route

    def update_bus_location(self, bus : Bus):
        if self.buses.__contains__(bus.idBus):
            self.buses[bus.idBus] = bus
        else:
            print(f'Bus {bus.idBus} does not exist')

    def get_passengers_bus(self, bus : Bus) -> List[Passenger]:
        return [p for p in self.passengers.values() if p.bus != None and p.bus.idBus == bus.idBus]
    
    def get_passengers_route(self, bus : Bus) -> List[Passenger]:
        route = bus.route
        return [p for p in self.passengers.values() if (p.bus == None and p.route.idRoute == route.idRoute) or p.bus.idBus == bus.idBus]
    
    
    def route_needs_bus(self, route : Route):
        buses_in_route = [b for b in self.buses.values() if b.running and b.route.idRoute == route.idRoute]
        buses_80_per = [b for b in buses_in_route if b.get_occupancy() >= 0.8]
        passenger_at_route = [p for p in self.passengers.values() if p.bus == None and route.idRoute == p.route.idRoute]
        if len(buses_in_route) > 0:
            last_station = min([route.getIndexStation(b.current_station) for b in buses_in_route])
            for p in passenger_at_route:
                if route.getIndexStation(p.initialStation) < last_station:
                    return True
        return len(buses_in_route) == 0 or (len(buses_80_per) == len(buses_in_route) and len(passenger_at_route) > 20)

    def passenger_entered(self, passenger : Passenger, bus : Bus):
        self.buses[bus.idBus].add_passenger()
        self.passengers[passenger.idPassenger] = passenger

    def passenger_left(self, passenger : Passenger, bus : Bus):
        self.buses[bus.idBus].remove_passenger()
        self.passengers[passenger.idPassenger] = passenger
        del self.passengers[passenger.idPassenger]

    def busEnded(self, bus : Bus):
        self.buses[bus.idBus].reset()
        ids = []
        for p in self.passengers.values():
            if p.bus != None and p.bus.idBus == bus.idBus:
                ids.append(p.idPassenger)
        for id in ids:
            del self.passengers[id]

    def busStarted(self, bus : Bus, route : Route):
        self.buses[bus.idBus].route = route
        self.buses[bus.idBus].running = True

    def pick_random_bus_available(self):
        buses_available = list(filter(lambda bus : not bus.running,self.buses.values()))
        if(len(buses_available) > 0):
            index = random.randint(0,len(buses_available) - 1)
            buses_available[index].running = True
            return buses_available[index]
        else:
            return None

