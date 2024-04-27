from spade.message import Message
import jsonpickle
import json

class MessageBuilder:
    def setPerformative(self,performative : str):
        self.performative = performative
        return self
    def setReceiver(self,receiver : str):
        self.receiver = receiver
        return self
    def setBody(self, body):
        self.body = body
        return self
    
    # returns the server saved on the file Data/util.json
    def get_server():
        res = ''
        with open('Data/util.json','r') as f:
            data = json.load(f)
            res = data['server']
        return res

    def build(self):
        msg = Message(to=f'{self.performative}@{self.get_server()}')
        msg.set_metadata("performative",self.performative)
        msg.set_metadata("ontology","myOntology")
        msg.set_metadata("language","OWL-S")
        msg.body = jsonpickle.encode(self.body)
        return msg
    
    @classmethod
    def build_message(receiver : str, performative : str, body):
        msgBuilder = MessageBuilder()
        msgBuilder.setReceiver(receiver)
        msgBuilder.setPerformative(performative)
        msgBuilder.setBody(body)
        return msgBuilder.build()

    @classmethod
    def read_message(msg):
        return msg.get_metadata('performative'), jsonpickle.decode(msg.body)


    