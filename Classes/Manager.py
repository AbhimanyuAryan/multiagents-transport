import Route
import Client
import Bus
import List

from Route import generateRoute

class Manager:
    def __init__(self):
        self.buses = {}
        self.clients = {}
        route = generateRoute()
        self.routes = {route.idRoute : route}

    def add_bus(self,bus : Bus):
        self.buses[bus.idBus] = bus

    def add_client(self,client : Client):
        print("Manager: add_client to do")

    def add_route(self,route : Route):
        self.routes[route.idRoute] = route

    def update_bus_location(self, bus : Bus):
        if self.buses.__contains__(bus.idBus):
            self.buses[bus.idBus] = bus
        else:
            print(f'Bus {bus.idBus} does not exist')

    def get_clients_bus(self, bus : Bus) -> List[Client]:
        print("Manager: get_clients_bus to do")
        return []
    
    def route_needs_bus(self, route : Route):
        buses_in_route = list(filter(lambda bus : bus.running and bus.route.idRoute == route.idRoute,self.buses.values()))
        buses_80_per = list()
