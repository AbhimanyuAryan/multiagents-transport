from spade.agent import Agent
from Behaviours.BusBehaviour import BusBehaviour
from Behaviours.CurrentBusLocationUpdate import CurrentBusLocationUpdate
from Behaviours.NotifyManagerBusEnded import NotifyManagerBusEnd
from Behaviours.NotifyManagerBusStarted import NotifyManagerBusStarted
from Behaviours.UpdateBusLocation import UpdateBusLocation
from Classes.Bus import Bus
from Classes.Route import Route
from Classes.Passenger import Passenger
from Utils.Performative import Performative
from Utils.MessageBuilder import MessageBuilder

class BusAgent(Agent):
    def __init__(self,sender,password,bus : Bus):
        super().__init__(sender,password)
        self.bus = bus

    async def setup(self):
        self.behaviour = BusBehaviour()
        self.add_behaviour(self.behaviour)
    
    def startBus(self):
        print('Bus Agent: startBus')
        self.bus.running = True
        self.add_behaviour(UpdateBusLocation())
        self.add_beahviour(NotifyManagerBusStarted())
        
    def endBus(self):
        print('Bus Agent: endBus')
        self.bus.running = False
        self.add_behaviour(NotifyManagerBusEnd())

    def passengerEntered(self, passenger: Passenger):
        print('Bus Agent: passengerEntered')
        self.bus.passengers.append(passenger)

    def updateLocation(self):
        route = self.bus.route
        current_station_index = route.stations.index(self.bus.current_station)
        next_station_index = current_station_index + 1
        if next_station_index < len(route.stations):
            self.add_behaviour(CurrentBusLocationUpdate())
            self.bus.current_station = route.stations[next_station_index]
            return True
        else:
            print("Bus reached the last station.")
            self.endBus()
            return False

    def passengerLeft(self, passenger: Passenger):
        print('Bus Agent: passengerLeft')
        self.bus.passengers.remove(passenger)

    # Manager gives route to the bus
    def setRoute(self, route: Route):
        self.bus.route = route
        self.startBus()

    def receivedMessage(self, msg):
        performative, body = MessageBuilder.read_message(msg)
        print(f"Bus Agent #{self.bus.idBus}: New Message with the performative {performative}.")
        if performative == Performative.request():
            route = Route.from_dict(body['route'])
            self.setRoute(route)
        elif performative == Performative.inform():
            if body['type'] == 'passenger':
                action = body['action']
                if action == '+':
                    print(f'Bus Agent: Received notification that a passenger entered.')
                    self.passengerEntered(Passenger.from_dict(body['passenger']))
                elif action == '-':
                    print(f'Bus Agent: Received notification that a passenger left.')
                    self.passengerLeft(Passenger.from_dict(body['passenger']))
        return 0
