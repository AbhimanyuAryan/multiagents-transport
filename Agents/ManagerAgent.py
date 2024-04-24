from spade.agent import Agent
from spade.message import Message
import jsonpickle
import threading
import List
from Behaviours.ManagerBehaviour import ManagerBehaviour
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
        self.manager.add_(passenger)
        # see if there is more bus to the passenger route

    def setRouteBus(self, route : Route):
        print('Manager Agent: setRouteBus to do')
        # set the route at the bus
        # send a message to the bus
        return 0

    def busStarted(self, bus : Bus , route : Route):
        print('Manager Agent: busStarted to do')
        # set the route at the bus
        # set running = true
        return 0
    
    def busEnded(self, bus : Bus , route : Route):
        print('Manager Agent: busEnded to do')
        # remove the route from the bus
        # set running = false
        return 0
    
    def passengerEntered(self, passenger : Passenger , bus : Bus):
        print('Manager Agent: passengerEntered to do')
        # notify the bus new passenger
        # increase the number of passengers at the bus
        # set bus at the passenger
        return 0
    
    def passengerLeft(self, passenger : Passenger , bus : Bus):
        print('Manager Agent: passengerLeft to do')
        # notify the bus one passenger left
        # decrease the number of passengers at the bus
        # remove bus at the passenger
        return 0

    def notifyBusLocation(self,passengers : List[Passenger], bus : Bus) :
        # send a message to all the passengers of the new bus location
        print('Manager Agent: notifyBusLocation to do')
        return 0
    
    def updateBusLocation(self,bus : Bus):
        # finish get_passengers_bus
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
                print(f'Manager Agent: New Passenger to do')
                # self.registerPassenger(passenger)
            elif body['type'] == 'Bus':
                print(f'Manager Agent: New Bus to do')
                # self.registerBus(bus)
        elif performative == Requests.get_performative_confirm():
            if body['action'] == 'start':
                print(f'Manager Agent: Bus started to do')
                # self.busStarted(bus,route)
            elif body['action'] == 'end':
                print(f'Manager Agent: Bus ended to do')
                # self.busEnded(bus,route)
        elif performative == Requests.get_performative_inform():
            if body['type'] == 'passenger':
                if body['action'] == 'enter':
                    print(f'Manager Agent: Passenger entered to do')
                    # self.passengerEntered(passenger, bus)
                elif body['action'] == 'left':
                    print(f'Manager Agent: Passenger left to do')
                    # self.passengerLeft(passenger, bus)
            elif body['type'] == 'bus':
                print('Manager Agent: New Bus Location to do')
                # self.updateBusLocation(bus)
        return 0
