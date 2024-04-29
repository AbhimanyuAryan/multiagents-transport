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
        self.insideBus = 0

    def registerPassenger(self, passenger:Passenger):
        print(f'Passenger Agent {self.passenger.idPassenger}: Registering the Passenger')
        b = NotifyPassengerRegisterBehaviour(passenger)
        self.add_behaviour(b)
        return 0

    def enterBus (self, bus: Bus):
        print(f"Passenger {self.passenger.idPassenger}: Notified manager to enter a bus.")
        self.passenger.bus=bus
        b = EnterBusBehaviour(self.passenger,bus)
        self.add_behaviour(b)
        return 0
        
    def leftBus (self):
        print(f"Passenger {self.passenger.idPassenger}: Notified manager to leave a bus.")
        b = LeftBusBehaviour(self.passenger,self.passenger.bus)
        self.add_behaviour(b)
        self.stop()
        return 0

    def recieveBusLocation (self, bus: Bus):
        if self.insideBus == 0 and bus.current_station.location == self.passenger.initialStation.location:
            print(f"Passenger Agent {self.passenger.idPassenger}: Bus is in the same station as the passenger.")
            self.insideBus = 1
            self.enterBus(bus)
        elif self.insideBus == 4:
            print(f"Passenger Agent {self.passenger.idPassenger}: Leaving the bus")
            self.leftBus()
            self.insideBus = 0
        else:
            if self.insideBus != 0:
                self.insideBus += 1
            print(f"Passenger Agent {self.passenger.idPassenger}: Bus {bus.idBus} is on another Station.")
    
    def leaveBus(self,bus : Bus):
        print(f'Passenger Agent {self.passenger.idPassenger}: Leaving the Bus')
        self.stop()

    def receivedMessage(self,msg):
        performative, body = MessageBuilder.read_message(msg)
        # print(f"Passenger Agent {self.passenger.idPassenger}: New Message with the performative {performative}.")
        if performative == Performative.inform():
            if body['type'] == 'notification':
                bus = Bus.from_dict(body['bus'])
                self.recieveBusLocation(bus)
            elif body['type'] == 'end_bus':
                bus = Bus.from_dict(body['bus'])
                self.leaveBus(bus)
        else:
            print(f"Passenger Agent {self.passenger.idPassenger}: This performative: {performative} is not supported.")
