from spade.agent import Agent
from spade.message import Message
from Behaviours.BusBehaviour import BusBehaviour
from Behaviours.NotifyPassengerLeft import NotifyPassengerLeftBehaviour
from Behaviours.NotifyPassengerEntered import NotifyPassengerEnteredBehaviour
from Classes.Bus import Bus
from Classes.Route import Route
from Classes.Passenger import Passenger
from Classes.Station import Station
from Utils import Requests

class BusAgent(Agent):
    async def setup(self):
        self.behaviour = BusBehaviour()
        self.add_behaviour(self.behaviour)
    
    def createBus(self, idBus: int, capacity: int, route: Route, current_station: Station):
        self.bus = Bus(idBus, capacity, route, current_station)

    def startBus(self):
        print('Bus Agent: startBus')
        self.bus.running = True

    def endBus(self):
        print('Bus Agent: endBus')
        self.bus.running = False

    def passengerEntered(self, passenger: Passenger):
        print('Bus Agent: passengerEntered')
        self.bus.passengers.append(passenger)

    def passengerLeft(self, passenger: Passenger):
        print('Bus Agent: passengerLeft')
        self.bus.passengers.remove(passenger)

    def notifyPassengerLeft(self):
        print('Bus Agent: notifyPassengerLeft')
        b = NotifyPassengerLeftBehaviour(self.bus.passengers)
        self.add_behaviour(b)

    def notifyPassengerEntered(self):
        print('Bus Agent: notifyPassengerEntered')
        b = NotifyPassengerEnteredBehaviour(self.bus.passengers)
        self.add_behaviour(b)

    def receivedMessage(self, msg):
        performative, body = Requests.read_message(msg)
        print(f"Bus Agent #{self.bus.idBus}: New Message with the performative {performative}.")
        if performative == Requests.get_performative_confirm():
            if body['action'] == 'start':
                print(f'Bus Agent: Received start signal.')
                self.startBus()
            elif body['action'] == 'end':
                print(f'Bus Agent: Received end signal.')
                self.endBus()
        elif performative == Requests.get_performative_inform():
            if body['type'] == 'passenger':
                action = body['action']
                if action == 'enter':
                    print(f'Bus Agent: Received notification that a passenger entered.')
                    self.passengerEntered(Passenger.from_dict(body['passenger']))
                elif action == 'left':
                    print(f'Bus Agent: Received notification that a passenger left.')
                    self.passengerLeft(Passenger.from_dict(body['passenger']))
        return 0
