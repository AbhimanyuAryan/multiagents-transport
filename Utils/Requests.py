from spade.message import Message
from Classes.Passenger import Passenger
from Classes.Bus import Bus
from Classes.Route import Route
import jsonpickle
import json

# The main goal of this file is to centralize the process of creating messages
# Every new message that you want to add, pls add it here

# returns a string that represent subscribe performatives
def get_performative_subscribe():
    return 'subscribe'

def get_performative_confirm():
    return 'confirm'

def get_performative_inform():
    return 'inform'

def get_performative_request():
    return 'request'

# returns the server saved on the file Data/util.json
def get_server():
    res = ''
    with open('Data/util.json','r') as f:
        data = json.load(f)
        res = data['server']
    return res

# Message Builder, shouldn't be used outside this file
def message_builder(receiver : str, performative : str, body):
    server = get_server()
    msg = Message(to=f'{receiver}@{server}')
    msg.set_metadata("perfomative",performative)
    msg.set_metadata("ontology","myOntology")
    msg.set_metadata("language","OWL-S")
    msg.body = jsonpickle.encode(body)
    return msg
    
# An example of a function that creates a message to register a passenger in the manager
def serializeRegisterPassenger(receiver:str, passenger : Passenger):
    # passenger -> implement serializePassenger
    performative = get_performative_subscribe()
    serializedPassenger = passenger.to_dict()
    body = {
        'type' : 'Passenger',
        'data' : serializedPassenger
    }
    return message_builder(receiver,performative,body)

# An example of a function that creates a message to register a bus in the manager
def serializeRegisterBus(receiver:str, bus : Bus):
    # bus -> implement serializedBus
    performative = get_performative_subscribe()
    serializedBus = bus.to_dict()
    body = {
        'type' : 'Bus',
        'data' : serializedBus
    }
    return message_builder(receiver,performative,body)

def serializeBusStart(receiver:str, bus : Bus, route : Route):
    # bus -> implement serializedBus
    performative = get_performative_confirm()
    serializedBus = bus.to_dict()
    serializedRoute = route.to_dict()
    body = {
        'action' : 'start',
        'bus' : serializedBus,
        'route' : serializedRoute
    }
    return message_builder(receiver,performative,body)
    
def serializeBusEnd(receiver:str, bus : Bus, route : Route):
    # bus -> implement serializedBus
    performative = get_performative_confirm()
    serializedBus = bus.to_dict()
    serializedRoute = route.to_dict()
    body = {
        'action' : 'end',
        'bus' : serializedBus,
        'route' : serializedRoute
    }
    return message_builder(receiver,performative,body)

def serializePassengerEntered(receiver:str, passenger : Passenger, bus : Bus):
    # bus -> implement serializedBus
    # passenger -> implement serializePassenger
    performative = get_performative_inform()
    serializedBus = bus.to_dict()
    serializePassenger = passenger.to_dict()
    body = {
        'type' : 'passenger',
        'action' : 'enter',
        'bus' : serializedBus,
        'passenger' : serializePassenger
    }
    return message_builder(receiver,performative,body)
    
def serializePassengerLeft(receiver:str, passenger : Passenger, bus : Bus):
    # bus -> implement serializedBus
    # passenger -> implement serializePassenger
    performative = get_performative_inform()
    serializedBus = bus.to_dict()
    serializePassenger = passenger.to_dict()
    body = {
        'type' : 'passenger',
        'action' : 'left',
        'bus' : serializedBus,
        'passenger' : serializePassenger
    }
    return message_builder(receiver,performative,body)


def serializeBusNewLocation(receiver:str, bus : Bus):
    # bus -> implement serializedBus
    performative = get_performative_confirm()
    serializedBus = bus.to_dict()
    body = {
        'type' : 'bus',
        'action' : 'new_location',
        'bus' : serializedBus
    }
    return message_builder(receiver,performative,body)

def read_message(msg):
    return msg.get_metadata('performative'), jsonpickle.decode(msg.body)

def serializeNotifyPassenger(receiver:str, bus : Bus):
    performative = get_performative_inform()
    serializedBus = bus.to_dict()
    body = {
        'type' : 'notification',
        'bus' : serializedBus
    }
    return message_builder(receiver,performative,body)

def serializeNotifyBusNewPassenger(receiver:str, bus : Bus):
    performative = get_performative_inform()
    serializedBus = bus.to_dict()
    body = {
        'type' : 'notification',
        'action' : '+',
        'bus' : serializedBus
    }
    return message_builder(receiver,performative,body)

def serializeNotifyBusPassengerLeft(receiver:str, bus : Bus):
    performative = get_performative_inform()
    serializedBus = bus.to_dict()
    body = {
        'type' : 'notification',
        'action' : '-',
        'bus' : serializedBus
    }
    return message_builder(receiver,performative,body)

def serializeNotifyBusRoute(receiver : str, route : Route):
    performative = get_performative_request()
    serializedBus = route.to_dict()
    body = {
        'route': serializedBus,
    }
    return message_builder(receiver,performative,body)