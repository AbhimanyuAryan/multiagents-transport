from spade.agent import Agent
from Behaviours.EnterBusBehaviour import EnterBusBehaviour
from Behaviours.LeftBusBehaviour import LeftBusBehaviour
from Behaviours.NotifyPassengerRegisterBehaviour import NotifyPassengerRegisterBehaviour
from Behaviours.PassengerBehaviour import PassengerBehaviour
from Classes.Bus import Bus
from Classes.Passenger import Passenger
from Utils.Performative import Performative
from Utils.MessageBuilder import MessageBuilder

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

    def enterBus (self, bus: Bus):
        self.passenger.bus=bus
        b = EnterBusBehaviour(self.passenger,bus)
        self.add_behaviour(b)
        return 0
        
    def leftBus (self):
        b = LeftBusBehaviour(self.passenger,self.passenger.bus)
        self.add_behaviour(b)
        self.passenger.bus=None
        return 0

    def recieveBusLocation (self, bus: Bus):
        if bus.current_station.location == self.passenger.initialStation.location:
            print("Bus is in the same station as the passenger.")
            self.insideBus = True
            self.enterBus(bus)
        elif self.insideBus:
            print("Leaving the bus")
            self.leftBus()
            self.insideBus = False
        else:
            print(f"Bus {bus.current_station.location} is not in the same station as the passenger {self.passenger.initialStation.location}.")

    def receivedMessage(self,msg):
        performative, body = MessageBuilder.read_message(msg)
        print(f"Passenger Agent #{self.passenger.idPassenger}: New Message with the performative {performative}.")
        if performative == Performative.inform():
            if body['type'] == 'notification':
                bus = Bus.from_dict(body['bus'])
                self.recieveBusLocation(bus)
            elif body['type'] == 'end_bus':
                print('Passenger Agent: Leaving the Bus')
                bus = Bus.from_dict(body['bus'])
                self.passenger.leave_bus(bus)
        else:
            print(f"Passenger Agent does not know how to handle this performative: {performative}.")
