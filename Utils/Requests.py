from spade.message import Message
import Client
import Bus
import jsonpickle
import json

# The main goal of this file is to centralize the process of creating messages
# Every new message that you want to add, pls add it here

# returns a string that represent subscribe performatives
def get_performative_subscribe():
    return 'subscribe'


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
    
# An example of a function that creates a message to register a client in the manager
def serializeRegisterClient(receiver:str, client : Client):
    # client -> implement serializeClient
    performative = get_performative_subscribe()
    serializedClient = ''
    body = {
        'type' : 'Client',
        'data' : serializedClient
    }
    return message_builder(receiver,performative,body)

# An example of a function that creates a message to register a bus in the manager
def serializeRegisterBus(receiver:str, bus : Bus):
    # bus -> implement serializedBus
    performative = get_performative_subscribe()
    serializedBus = ''
    body = {
        'type' : 'Bus',
        'data' : serializedBus
    }
    return message_builder(receiver,performative,body)
