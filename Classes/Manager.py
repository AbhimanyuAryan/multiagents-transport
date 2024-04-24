from Classes.Route import Route
from Classes.Passenger import Passenger
from Classes.Bus import Bus
import List
import random

from Route import generateRoute

class Manager:
    def __init__(self):
        self.buses = {}
        self.passengers = {}
        route = generateRoute()
        self.routes = {route.idRoute : route}

    def add_bus(self,bus : Bus):
        self.buses[bus.idBus] = bus

    def add_passenger(self,passenger : Passenger):
        self.passenger[passenger.idPassenger] = passenger

    def add_route(self,route : Route):
        self.routes[route.idRoute] = route

    def update_bus_location(self, bus : Bus):
        if self.buses.__contains__(bus.idBus):
            self.buses[bus.idBus].location = bus.location
        else:
            print(f'Bus {bus.idBus} does not exist')

    def get_passengers_bus(self, bus : Bus) -> List[Passenger]:
        return list(filter(lambda p: p.bus != None and p.bus.idBus == bus.idBus,self.passengers.values))
    
    def route_needs_bus(self, route : Route):
        buses_in_route = list(filter(lambda bus : bus.running and bus.route.idRoute == route.idRoute,self.buses.values()))
        buses_80_per = list(filter(lambda bus : bus.capacity > 80, buses_in_route))
        passenger_at_route = list(filter(lambda passenger : route.hasStation(passenger.station)))
        return len(buses_80_per) > len(buses_in_route) - 2 and len(passenger_at_route) > 40 

    def passenger_entered(self, passenger : Passenger, bus : Bus):
        self.buses[bus.idBus].passengers += 1
        self.passengers[passenger.idPassenger].bus = bus

    def passenger_left(self, passenger : Passenger, bus : Bus):
        self.buses[bus.idBus].passengers -= 1
        self.passengers[passenger.idPassenger].bus = None

    def bus_ended(self, bus : Bus):
        self.buses[bus.idBus].route = None
        self.buses[bus.idBus].running = False

    def bus_started(self, bus : Bus, route : Route):
        self.buses[bus.idBus].route = route
        self.buses[bus.idBus].running = True

    def pick_random_bus_available(self):
        buses_available = list(filter(lambda bus : not bus.running,self.buses.values()))
        index = random.randint(0,len(buses_available) - 1)
        return buses_available[index]

