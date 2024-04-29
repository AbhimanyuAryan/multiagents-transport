from spade.agent import Agent
from Behaviours.ManagerBehaviour import ManagerBehaviour
from Behaviours.NotifyPassenger import NotifyPassengerBehaviour
from Behaviours.NotifyBusPassenger import NotifyBusPassengerBehaviour
from Behaviours.NotifyBusRoute import NotifyBusRouteBehaviour
from Behaviours.NotifyPassengerBusEnd import NotifyPassengerBusEndBehaviour
from Utils.Performative import Performative
from Utils.MessageBuilder import MessageBuilder
from Classes.Manager import Manager
from Classes.Bus import Bus
from Classes.Passenger import Passenger
from Classes.Route import Route
from typing import List

class ManagerAgent(Agent):
    async def setup(self):
        self.behaviour = ManagerBehaviour()
        self.add_behaviour(self.behaviour)
        self.manager : Manager = Manager()

    def registerBus(self, bus : Bus):
        print(f'Manager Agent: New Bus {bus.idBus}')
        self.manager.add_bus(bus)

    def registerPassenger(self, passenger : Passenger):
        print(f'Manager Agent: New Passenger {passenger.idPassenger}')
        self.manager.add_passenger(passenger)
        if self.manager.route_needs_bus(passenger.route):
            self.setRouteBus(passenger.route)

    def setRouteBus(self, route : Route):
        bus = self.manager.pick_random_bus_available()
        if(bus != None):
            print(f'Manager Agent: The bus {bus.idBus} has beed assigned to the route {route.idRoute}')
            b = NotifyBusRouteBehaviour(bus,route)
            self.add_behaviour(b)
        else:
            print('Manager Agent: There are no Buses Available. Please add more buses.')
        return 0

    def busStarted(self, bus : Bus , route : Route):
        print(f'Manager Agent: The bus {bus.idBus} started its route')
        self.manager.busStarted(bus, route)
        return 0
    
    def busEnded(self, bus : Bus , route : Route):
        passenger_to_notify = self.manager.get_passengers_bus(bus)
        self.manager.busEnded(bus)
        aux = [p.idPassenger for p in passenger_to_notify]
        print(f'Manager Agent: The bus {bus.idBus} ended its route. These passengers will be notified: {aux}')
        for p in passenger_to_notify:
            b = NotifyPassengerBusEndBehaviour(p,bus)
            self.add_behaviour(b)
        return 0
    
    def passengerEntered(self, passenger : Passenger , bus : Bus):
        print(f'Manager Agent: The passenger {passenger.idPassenger} has joined the bus {bus.idBus}')
        self.manager.passenger_entered(passenger,bus)
        b = NotifyBusPassengerBehaviour(bus,True)
        self.add_behaviour(b)
        return 0
    
    def passengerLeft(self, passenger : Passenger , bus : Bus):
        print(f'Manager Agent: The passenger {passenger.idPassenger} has left the bus {bus.idBus}')
        self.manager.passenger_left(passenger,bus)
        b = NotifyBusPassengerBehaviour(bus,False)
        self.add_behaviour(b)
        return 0

    def notifyBusLocation(self,passengers : List[Passenger], bus : Bus) :
        for p in passengers:
            b = NotifyPassengerBehaviour(p,bus)
            self.add_behaviour(b)
        return 0
    
    def updateBusLocation(self,bus : Bus):
        self.manager.update_bus_location(bus)
        passenger_to_notify = self.manager.get_passengers_route(bus.route)
        aux = [p.idPassenger for p in passenger_to_notify]
        print(f'Manager Agent: Received a new station for bus {bus.idBus}. These passengers will be notified: {aux}')
        self.notifyBusLocation(passenger_to_notify,bus)
        return 0
    
    def receivedMessage(self,msg):
        performative, body = MessageBuilder.read_message(msg)
        # print(f"Manager Agent: New Message with the performative {performative}")
        if performative == Performative.subscribe():
            if body['type'] == 'Passenger':
                passenger = Passenger.from_dict(body['data'])
                self.registerPassenger(passenger)
            elif body['type'] == 'Bus':
                bus = Bus.from_dict(body['data'])
                self.registerBus(bus)
        elif performative == Performative.confirm():
            bus = Bus.from_dict(body['bus'])
            route = Route.from_dict(body['route'])
            if body['action'] == 'start':
                self.busStarted(bus,route)
            elif body['action'] == 'end':
                self.busEnded(bus,route)
        elif performative == Performative.inform():
            if body['type'] == 'passenger':
                bus = Bus.from_dict(body['bus'])
                passenger = Passenger.from_dict(body['passenger'])
                if body['action'] == '+':
                    self.passengerEntered(passenger, bus)
                elif body['action'] == '-':
                    self.passengerLeft(passenger, bus)
            elif body['type'] == 'bus':
                bus = Bus.from_dict(body['bus'])
                self.updateBusLocation(bus)
        else:
            print(f'Manager Agent: Performative {performative} not supported.')
        return 0
