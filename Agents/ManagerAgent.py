from spade.agent import Agent
from spade.message import Message
import jsonpickle
import threading
import List
from Behaviours.ManagerBehaviour import ManagerBehaviour
from Behaviours.NotifyPassenger import NotifyPassengerBehaviour
from Behaviours.NotifyBusPassenger import NotifyBusPassengerBehaviour
from Behaviours.NotifyBusRoute import NotifyBusRouteBehaviour
import Utils.Requests as Requests
from Classes.Manager import Manager
from Classes.Bus import Bus
from Classes.Passenger import Passenger
from Classes.Route import Route
from Classes.Station import Station

class ManagerAgent(Agent):
    async def setup(self):
        self.behaviour = ManagerBehaviour()
        self.add_behaviour(self.behaviour)
        self.manager : Manager = Manager()

    def registerBus(self, bus : Bus):
        self.manager.add_bus(bus)

    def registerPassenger(self, passenger : Passenger):
        self.manager.add_passenger(passenger)
        if self.manager.route_needs_bus(passenger.route):
            self.setRouteBus(passenger.route)

    def setRouteBus(self, route : Route):
        print('Manager Agent: setRouteBus')
        bus = self.manager.pick_random_bus_available()
        b = NotifyBusRouteBehaviour(bus,route)
        self.add_behaviour(b)
        return 0

    def busStarted(self, bus : Bus , route : Route):
        print('Manager Agent: busStarted')
        self.manager.busStarted(bus, route)
        return 0
    
    def busEnded(self, bus : Bus , route : Route):
        print('Manager Agent: busEnded')
        self.manager.busEnded(bus)
        return 0
    
    def passengerEntered(self, passenger : Passenger , bus : Bus):
        print('Manager Agent: passengerEntered to do')
        self.manager.passenger_entered(passenger,bus)
        b = NotifyBusPassengerBehaviour(bus,True)
        self.add_behaviour(b)
        return 0
    
    def passengerLeft(self, passenger : Passenger , bus : Bus):
        print('Manager Agent: passengerLeft to do')
        self.manager.passenger_left(passenger,bus)
        b = NotifyBusPassengerBehaviour(bus,False)
        self.add_behaviour(b)
        return 0

    def notifyBusLocation(self,passengers : List[Passenger], bus : Bus) :
        print('Manager Agent: notifyBusLocation')
        for p in passengers:
            b = NotifyPassengerBehaviour(p,bus)
            self.add_behaviour(b)
        return 0
    
    def updateBusLocation(self,bus : Bus):
        print('Manager Agent: notifyBusLocation to do')
        self.manager.update_bus_location(bus)
        passenger_to_notify = self.manager.get_passengers_bus(bus)
        self.notifyBusLocation(passenger_to_notify,bus)
        return 0
    
    def receivedMessage(self,msg):
        performative, body = Requests.read_message(msg)
        print(f"Manager Agent: New Message with the performative {performative}")
        if performative == Requests.get_performative_subscribe():
            if body['type'] == 'Passenger':
                print(f'Manager Agent: New Passenger')
                passenger = Passenger.from_dict(body['data'])
                self.registerPassenger(passenger)
            elif body['type'] == 'Bus':
                print(f'Manager Agent: New Bus')
                bus = Bus.from_dict(body['data'])
                self.registerBus(bus)
        elif performative == Requests.get_performative_confirm():
            bus = Bus.from_dict(body['bus'])
            route = Route.from_dict(body['route'])
            if body['action'] == 'start':
                print(f'Manager Agent: Bus started')
                self.busStarted(bus,route)
            elif body['action'] == 'end':
                print(f'Manager Agent: Bus ended')
                self.busEnded(bus,route)
        elif performative == Requests.get_performative_inform():
            if body['type'] == 'Passenger':
                bus = Bus.from_dict(body['bus'])
                passenger = Passenger.from_dict(body['passenger'])
                if body['action'] == 'enter':
                    print(f'Manager Agent: Passenger entered')
                    self.passengerEntered(passenger, bus)
                elif body['action'] == 'left':
                    print(f'Manager Agent: Passenger left')
                    self.passengerLeft(passenger, bus)
            elif body['type'] == 'Bus':
                bus = Bus.from_dict(body['bus'])
                print('Manager Agent: New Bus Location')
                self.updateBusLocation(bus)
        return 0
