from spade.agent import Agent
from spade.message import Message
import jsonpickle
import threading
import List
from Behaviours.ManagerBehaviour import ManagerBehaviour
from Utils.Requests import MakeRequest
from Classes.Manager import Manager
from Classes.Bus import Bus
from Classes.Client import Client
from Classes.Route import Route
from Classes.Station import Station

class ManagerAgent(Agent):
    async def setup(self):
        self.makerequest = MakeRequest('WRITE YOU SERVER HERE')
        self.behaviour = ManagerBehaviour()
        self.add_behaviour(self.behaviour)
        self.manager : Manager = Manager()

    def registerBus(self, bus : Bus):
        self.manager.add_bus(bus)

    def registerClient(self, client : Client):
        self.manager.add_client(client)

    def setRouteBus(self, route : Route):
        print('Manager Agent: setRouteBus to do')
        return 0

    def busStarted(self, bus : Bus , route : Route):
        print('Manager Agent: busStarted to do')
        return 0
    
    def busEnded(self, bus : Bus , route : Route):
        print('Manager Agent: busEnded to do')
        return 0
    
    def clientEntered(self, client : Client , bus : Bus):
        print('Manager Agent: clientEntered to do')
        return 0
    
    def clientLeft(self, client : Client , bus : Bus):
        print('Manager Agent: clientLeft to do')
        return 0

    def notifyBusLocation(self,clients : List[Client], bus : Bus) :
        print('Manager Agent: notifyBusLocation to do')
        return 0
    
    def updateBusLocation(self,bus : Bus):
        print('Manager Agent: notifyBusLocation to do')
        return 0
    
    def receivedMessage(self,msg):
        performative = msg.get_metadata('performative')
        print(f"Manager Agent: New Message with the performative {performative}")
        body = jsonpickle.decode(msg.body)
        if performative == self.makerequest.get_performative_subscribe():
            if body['type'] == 'Client':
                print(f'Manager Agent: New Client to do')
                # client = Client()
                # self.registerClient(client)
            elif body['type'] == 'Bus':
                print(f'Manager Agent: New Bus to do')
                # bus = Bus()
                # self.registerBus(bus)
        return 0
