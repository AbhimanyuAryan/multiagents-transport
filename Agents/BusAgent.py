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
        # Object should contain the route
        # Oneshot behaviour to notify Manager

    def endBus(self):
        print('Bus Agent: endBus')
        self.bus.running = False
        # Object should contain the route
        # Oneshot behaviour to notify Manager

    def passengerEntered(self, passenger: Passenger):
        print('Bus Agent: passengerEntered')
        self.bus.passengers.append(passenger)

    def updateLocation(self):
        # every 5 second update the location in a thread
        print('Bus Agent: updateLocation')
        # route has list of station
        # if statusBus == true
        # increment the route.station index in list in a thread 

    def passengerLeft(self, passenger: Passenger):
        print('Bus Agent: passengerLeft')
        self.bus.passengers.remove(passenger)

    # Manager gives route to the bus
    def setRoute(self, route: Route):
        self.bus.route = route

    def receivedMessage(self, msg):
        performative, body = Requests.read_message(msg)
        print(f"Bus Agent #{self.bus.idBus}: New Message with the performative {performative}.")
        if performative == Requests.get_performative_request():
            # pass itself is assigned to route
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
