from spade.message import Message
from Classes.Passenger import Passenger
from Classes.Bus import Bus
from Classes.Route import Route
from Utils.Performative import Performative
from Utils.MessageBuilder import MessageBuilder

# The main goal of this file is to centralize the process of creating messages
# Every new message that you want to add, pls add it here

# Tested
def serializeRegisterPassenger(receiver:str, passenger : Passenger):
    performative = Performative.subscribe()
    serializedPassenger = passenger.to_dict()
    body = {
        'type' : 'Passenger',
        'data' : serializedPassenger
    }
    return MessageBuilder.build_message(receiver,performative,body)

# Not Tested
def serializeRegisterBus(receiver:str, bus : Bus):
    performative = Performative.subscribe()
    serializedBus = bus.to_dict()
    body = {
        'type' : 'Bus',
        'data' : serializedBus
    }
    return MessageBuilder.build_message(receiver,performative,body)

# Not Tested
def serializeBusStart(receiver:str, bus : Bus, route : Route):
    performative = Performative.confirm()
    serializedBus = bus.to_dict()
    serializedRoute = route.to_dict()
    body = {
        'action' : 'start',
        'bus' : serializedBus,
        'route' : serializedRoute
    }
    return MessageBuilder.build_message(receiver,performative,body)
    
# Not Tested
def serializeBusEnd(receiver:str, bus : Bus, route : Route):
    performative = Performative.confirm()
    serializedBus = bus.to_dict()
    serializedRoute = route.to_dict()
    body = {
        'action' : 'end',
        'bus' : serializedBus,
        'route' : serializedRoute
    }
    return MessageBuilder.build_message(receiver,performative,body)

# Not Tested
def serializePassengerEntered(receiver:str, passenger : Passenger, bus : Bus):
    performative = Performative.inform()
    serializedBus = bus.to_dict()
    serializePassenger = passenger.to_dict()
    body = {
        'type' : 'passenger',
        'action' : 'enter',
        'bus' : serializedBus,
        'passenger' : serializePassenger
    }
    return MessageBuilder.build_message(receiver,performative,body)

# Not Tested
def serializePassengerLeft(receiver:str, passenger : Passenger, bus : Bus):
    performative = Performative.inform()
    serializedBus = bus.to_dict()
    serializePassenger = passenger.to_dict()
    body = {
        'type' : 'passenger',
        'action' : 'left',
        'bus' : serializedBus,
        'passenger' : serializePassenger
    }
    return MessageBuilder.build_message(receiver,performative,body)

# Not Tested
def serializeBusNewLocation(receiver:str, bus : Bus):
    performative = Performative.confirm()
    serializedBus = bus.to_dict()
    body = {
        'type' : 'bus',
        'action' : 'new_location',
        'bus' : serializedBus
    }
    return MessageBuilder.build_message(receiver,performative,body)

# Not Tested
def serializeNotifyPassenger(receiver:str, bus : Bus):
    performative = Performative.inform()
    serializedBus = bus.to_dict()
    body = {
        'type' : 'notification',
        'bus' : serializedBus
    }
    return MessageBuilder.build_message(receiver,performative,body)

# Not Tested
def serializeNotifyBusNewPassenger(receiver:str, bus : Bus):
    performative = Performative.inform()
    serializedBus = bus.to_dict()
    body = {
        'type' : 'notification',
        'action' : '+',
        'bus' : serializedBus
    }
    return MessageBuilder.build_message(receiver,performative,body)

# Not Tested
def serializeNotifyBusPassengerLeft(receiver:str, bus : Bus):
    performative = Performative.inform()
    serializedBus = bus.to_dict()
    body = {
        'type' : 'notification',
        'action' : '-',
        'bus' : serializedBus
    }
    return MessageBuilder.build_message(receiver,performative,body)

# Not Tested
def serializeNotifyBusRoute(receiver : str, route : Route):
    performative = Performative.request()
    serializedBus = route.to_dict()
    body = {
        'route': serializedBus,
    }
    return MessageBuilder.build_message(receiver,performative,body)