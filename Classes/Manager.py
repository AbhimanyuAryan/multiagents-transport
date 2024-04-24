import Route
import Classes.Passenger as Passenger
import Bus
import List

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
        print("Manager: add_passenger to do")

    def add_route(self,route : Route):
        self.routes[route.idRoute] = route

    def update_bus_location(self, bus : Bus):
        if self.buses.__contains__(bus.idBus):
            self.buses[bus.idBus] = bus
        else:
            print(f'Bus {bus.idBus} does not exist')

    def get_passengers_bus(self, bus : Bus) -> List[Passenger]:
        print("Manager: get_passengers_bus to do")
        return []
    
    def route_needs_bus(self, route : Route):
        buses_in_route = list(filter(lambda bus : bus.running and bus.route.idRoute == route.idRoute,self.buses.values()))
        buses_80_per = list()
