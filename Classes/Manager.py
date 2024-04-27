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
        route = bus.route
        return list(filter(lambda passenger : route.idRoute == passenger.route.idRoute,self.passengers.values()))
    
    def route_needs_bus(self, route : Route):
        buses_in_route = list(filter(lambda bus : bus.running and bus.route.idRoute == route.idRoute,self.buses.values()))
        buses_80_per = list(filter(lambda bus : bus.get_occupancy(), buses_in_route))
        passenger_at_route = list(filter(lambda passenger : route.idRoute == passenger.route.idRoute,self.passengers.values()))
        return len(buses_in_route) == 0 or (len(buses_80_per) == len(buses_in_route) and len(passenger_at_route) > 40)

    def passenger_entered(self, passenger : Passenger, bus : Bus):
        self.buses[bus.idBus].add_passenger()
        self.passengers[passenger.idPassenger] = passenger

    def passenger_left(self, passenger : Passenger, bus : Bus):
        self.buses[bus.idBus].remove_passenger()
        self.passengers[passenger.idPassenger] = passenger

    def busEnded(self, bus : Bus):
        self.buses[bus.idBus].reset()
        for p in self.passengers.values():
            if p.bus != None and p.bus.idBus == bus.idBus:
                p.leave_bus(bus)

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

