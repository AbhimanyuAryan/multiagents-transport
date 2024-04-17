import Route
import Client
import Bus

from Route import generateRoute

class Manager:
    def __init__(self):
        self.buses = {}
        self.clients = {}
        route = generateRoute()
        self.routes = {route.idRoute : route}

    def add_bus(self,bus : Bus):
        print("Manager: add_bus to do")

    def add_client(self,client : Client):
        print("Manager: add_client to do")

    def add_route(self,route : Route):
        self.routes[route.idRoute] = route