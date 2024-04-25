from spade.agent import Agent
from Behaviours.EnterBusBehaviour import EnterBusBehaviour
from Behaviours.LeftBusBehaviour import LeftBusBehaviour
from Behaviours.NotifyPassengerRegisterBehaviour import NotifyPassengerRegisterBehaviour
from Behaviours.PassengerBehaviour import PassengerBehaviour
from Classes.Bus import Bus
from Classes.Passenger import Passenger
from Classes.Route import Route
from Classes.Station import Station
from Utils import Requests

class PassengerAgent(Agent):
    def __init__(self,sender,password, passenger: Passenger):
        super().__init__(sender,password)
        self.passenger = passenger
    async def setup(self):
        self.behaviour = PassengerBehaviour()
        self.add_behaviour(self.behaviour)
        self.insideBus = False

    def registerPassenger(self, passenger:Passenger):
        print('Client Agent: registerPassenger')
        b = NotifyPassengerRegisterBehaviour(passenger)
        self.add_behaviour(b)
        return 0

    def enterBus (self, passenger: Passenger, bus: Bus):
        print('Client Agent: enterBus')
        self.passenger.bus=bus
        b = EnterBusBehaviour(passenger,bus)
        self.add_behaviour(b)
        return 0
        
    def leftBus (self, passenger: Passenger, bus: Bus):
        print('Client Agent: leftBus')
        self.passenger.bus=None
        b = LeftBusBehaviour(passenger,bus)
        self.add_behaviour(b)
        return 0

    def recieveBusLocation (self, bus: Bus):
        print('Client Agent: recieveBus')
        if bus.location == self.passenger.initialStation.location:
            print("Bus is in the same station as the passenger.")
            self.insideBus = True
            self.enterBus(self.passenger,bus)
        elif self.insideBus:
            self.leftBus()
            self.insideBus = False
        else:
            print("Bus is not in the same station as the passenger.")

    def receivedMessage(self,msg):
        performative, body = Requests.read_message(msg)
        print(f"Passenger Agent #{self.passenger.idPassenger}: New Message with the performative {performative}.")
        if performative == Requests.get_performative_inform():
            if body['type'] == 'notification':
                bus = Bus.from_dict(body['bus'])
                self.recieveBusLocation(bus)
        else:
            print(f"Passenger Agent does not know how to handle this performative: {performative}.")
